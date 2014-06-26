#target Illustrator
/**********************************************************

Hugo Ahlenius
December 2006
All Rights Reserved
fraxinus@oxel.net
http://www.oxel.net/
$Id: finalsave.jsx 1371 2013-10-17 10:05:31Z hugo $

finalsave.js

DESCRIPTION
	Based on the SaveDocsAsPDF.jsx script from Adobe Systems
	Copyright 2005 - see that file for full details

	This script saves the document as illustrator, pdf, eps
	png and a lower resolution jpg

	It is dependant on ImageMagick, for trimming and bitmap
	conversion/preparation.

	If the variable app.finalSaveNoPrompt is set to true
	it will not do a popup when the conversion is done,
	to enable batch conversion (see 'finalsave_dir.js')
o
**********************************************************/

var saveVersion = Compatibility.ILLUSTRATOR17;

var now = new Date;
var nowString = new String;
var doPngResize = true;

if (app.activeDocument.XMPString.match('for CS3') == 'for CS3') {
	var saveVersion = Compatibility.ILLUSTRATOR13;
}

if (app.activeDocument.XMPString.match('for CS2') == 'for CS2') {
	var saveVersion = Compatibility.ILLUSTRATOR12;
}

if (app.activeDocument.XMPString.match('noPngResize') == 'noPngResize') {
	doPngResize = false
}
// Main Code [Execution of script begins here]
var progFiles = "c:\\program";

// uncomment to suppress Illustrator warning dialogs
app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;

var i, files, fileType, sourceDoc, targetFileEPS, targetFilePDF, targetFileJPEG, pdfSaveOpts, targetFileAI, targetFileTemp;

var destFolder = null;
// Get the destination to save the files
destFolder = app.activeDocument.fullName.path;
sourceDoc = app.activeDocument;
var originalName = sourceDoc.name;

// {{{ METADATA STUFF
// Check if a metadata file exists...
var metaFile = new File(getNewName(originalName,destFolder, '.xml'));
if (!metaFile.exists) {
	metaFile.open('w:');
	metaFile.writeln('<?xml version="1.0" encoding="utf-8" ?><!DOCTYPE graphicdoc SYSTEM "http://nordpil.com/graphicdoc.dtd" >');
	metaFile.writeln('<graphicdoc>');
	metaFile.writeln('\t<title>' + originalName +'</title>');
	metaFile.writeln('\t<notes><![CDATA[');
	metaFile.writeln('\t]]></notes>');
	metaFile.writeln('\t<caption></caption>');
	metaFile.writeln('\t<originator>Hugo Ahlenius, Nordpil, ' + now.getFullYear() + '</originator>');
	metaFile.writeln('\t<credit>Hugo Ahlenius, Nordpil, ' + now.getFullYear() + '</credit>');
	metaFile.writeln('\t<projection></projection>');
	metaFile.writeln('\t<sources>');
	metaFile.writeln('\t\t<source></source>');
	metaFile.writeln('\t</sources>');
	metaFile.writeln('</graphicdoc>');
}
metaFile.close();
var xmpString = app.activeDocument.XMPString;
// }}}

// First Save as illustrator file in temp dir
targetFileAI = app.activeDocument.fullName;
var nowString = now.getFullYear() + '_' + zeroPad(now.getMonth()+1,2) + '_'  + zeroPad(now.getDate(),2) + '-' + zeroPad(now.getHours(),2) + '_'  + zeroPad(now.getMinutes(),2);
targetFileTemp = getNewName (originalName, $.getenv('temp'), nowString);
sourceDoc.saveAs (targetFileTemp, getAIOptions());

// The save for web/png...
targetFilePNG = getNewName(originalName, destFolder, '');
targetFilePNG2 = getNewName(originalName, destFolder, '');
var tempFile = new File(targetFilePNG2.fullName + '.png');
if (tempFile.exists) tempFile.remove();
sourceDoc.exportFile (targetFilePNG, ExportType.PNG24, getPNGOptions());

// Then export to pdf
targetFilePDF = getNewName(originalName, destFolder, '.pdf');
var tempFile = new File(targetFilePDF);
if (tempFile.exists) tempFile.remove();
if (doPngResize) sourceDoc.saveAs(targetFilePDF, getPDFOptions());

// Then export to eps
targetFileEPS = getNewName(originalName, destFolder, '.eps');
var tempFile = new File(targetFileEPS);
if (tempFile.exists) tempFile.remove();
if (doPngResize) sourceDoc.saveAs(targetFileEPS, getEPSOptions());


// Fix the bitmaps - trim and create thumb
var fBatch = new File (getNewName(originalName + nowString, $.getenv('temp'),'.bat'));
var pngFolder = targetFilePNG.fsName.replace(/\\[^\\]*$/,'');
var pngFileName = targetFilePNG.fsName.replace(/.*\\/,'');
fBatch.open('w:');
fBatch.writeln ('if EXIST "' + pngFolder + '\\' + targetFilePDF.displayName.replace(/.pdf/,'-01.pdf') + '" move "' + pngFolder + '\\' + targetFilePDF.displayName.replace(/.pdf/,'-01.pdf') + '" "' + pngFolder + '\\' + targetFilePDF.displayName + '"');
fBatch.writeln ('if NOT EXIST "' + pngFolder + '\\' + pngFileName + '.png" (');
fBatch.writeln ('   IF EXIST "' + pngFolder + '\\' + pngFileName.replace(/ /g,'-') + '.png" mv "' + pngFolder + '\\' + pngFileName.replace(/ /g,'-') + '.png" "' + pngFolder + '\\' + pngFileName + '.png"');
fBatch.writeln ('   IF EXIST "' + pngFolder + '\\' + pngFileName.replace(/\.[^\.]*$/g,'') + '.png" mv "' + pngFolder + '\\' + pngFileName.replace(/\.[^\.]*$/g,'') + '.png" "' + pngFolder + '\\' + pngFileName + '.png"');
fBatch.writeln (')');

fBatch.writeln ('if EXIST "' + targetFilePNG2.fsName + '.jpg" del "' + targetFilePNG2.fsName + '.jpg"');

if (!doPngResize) {
    fBatch.writeln (progFiles + '\\graphics\\imagemagick\\convert.exe -trim "' + targetFilePNG.fsName + '.png" "' + targetFilePNG2.fsName + '.png"');
} else {
    fBatch.writeln ('copy ' + targetFilePNG.fsName + '.png" "' + targetFilePNG2.fsName + '.png"');
}
fBatch.writeln (progFiles + '\\graphics\\imagemagick\\convert.exe -background white -flatten +repage -antialias -quality 85 -support 0.9 -gamma 0.95 -filter Mitchell -resize x350 "' + targetFilePNG2.fsName + '.png" "' + targetFilePNG2.fsName + '.jpg"');
if (targetFilePNG.fsName != targetFilePNG2.fsName) fBatch.writeln ('del "' + targetFilePNG.fsName + '.png"');
fBatch.close();
fBatch.execute();


// The save as illustrator again
sourceDoc.saveAs (targetFileAI, getAIOptions());

targetFilePNG.changePath(targetFilePNG2.fullName + '.png');

var alertString ='';
if (!(app.finalSaveNoPrompt)) {
	alertString = targetFileEPS.fsName + '\\n' + targetFilePDF.fsName + '\\n' + targetFileTemp.fsName  + '\\n';
	if (targetFilePNG.exists) 
		alertString = alertString + targetFilePNG2.fsName + '.png\\n' + targetFilePNG2.fsName + '.jpg';
		
	else {
		alertString = alertString + '-----------------\\nBITMAP FILES WERE *NOT* SAVED, PLEASE INVESTIGATE RESOLUTION....';
	}
	alertString = alertString + '\\n-----------------\\nin folder: ' + new Folder(destFolder).fsName;
	alertString = alertString.replace(/\\/,'\\\\');
	var fBatch = new File (getNewName(originalName + nowString, $.getenv('temp'),'2.bat'));
	fBatch.open('w:');
	fBatch.writeln ('start Growlnotify.exe /p:0 /t:"Illustrator finalsave.js" /ai:c:\\home\\hugo\\bin\\icon_illustrator.png "' + alertString + '"');
	fBatch.close();
	fBatch.execute();
}



/*********************************************************

getNewName: Function to get the new file name. The primary
name is the same as the source file.

**********************************************************/

function getNewName(docName, destFolder, newExt, maxLen) {
	var ext =  newExt; // new extension for file
	var newName = "";
	if (isNaN(maxLen)) maxLen = 1000;
	
	// if name has no dot (and hence no extension,
	// just append the extension
	if (docName.indexOf('.') < 0) {
		newName = docName + ext;
	} else {
		var dot = docName.lastIndexOf('.');  
		newName += docName.substring(0, dot);
		newName += ext;
	}
	
	newName = newName.substring(0,maxLen);
	
	// Create a file object to save the output
	saveInFile = new File( destFolder + '/' + newName );
	return saveInFile;
}




/*********************************************************

getPDFOptions: Function to set the PDF saving options of the 
files using the PDFSaveOptions object.

**********************************************************/

function getPDFOptions()
{
	// Create the PDFSaveOptions object to set the PDF options
	var pdfSaveOpts = new PDFSaveOptions();
	
	// Setting PDFSaveOptions properties. Please see the JavaScript Reference
	// for a description of these properties.
	// Add more properties here if you like
	pdfSaveOpts.acrobatLayers = true;
	pdfSaveOpts.colorBars = false;
	pdfSaveOpts.colorCompression = CompressionQuality.AUTOMATICJPEGHIGH;
	pdfSaveOpts.compressArt = true; //default
	pdfSaveOpts.embedICCProfile = true;
	pdfSaveOpts.enablePlainText = true;
	pdfSaveOpts.generateThumbnails = true; // default
	pdfSaveOpts.optimization = true;
	pdfSaveOpts.pageInformation = false;
	pdfSaveOpts.artboardRange = '1';
	pdfSaveOpts.viewAfterSaving = false;
	
	// uncomment to view the pdfs after conversion.
	// pdfSaveOpts.viewAfterSaving = true;
	

	return pdfSaveOpts;
}





/*********************************************************

getEPSOptions: Function to set the EPS saving options of the 
files using the EPSSaveOptions object.

**********************************************************/

function getEPSOptions()
{
	// Create the EPSSaveOptions object to set the EPS options
	var EPSSaveOpts = new EPSSaveOptions();
	
	// Setting EPSSaveOptions properties. Please see the JavaScript Reference
	// for a description of these properties.
	// Add more properties here if you like
	EPSSaveOpts.embedlinkedfiles = true;
	EPSSaveOpts.flattenoutput = true;
	EPSSaveOpts.includeDocumentThumbnails = true;
	EPSSaveOpts.epspreview = 'COLORTIFF';
	EPSSaveOpts.compatibility = saveVersion;
	
	// uncomment to view the EPSs after conversion.
	// EPSSaveOpts.viewAfterSaving = true;
	

	return EPSSaveOpts;
}




/*********************************************************

getPNGOptions: Function to set the PNG saving options of the 
files using the PNGSaveOptions object.

**********************************************************/

function getPNGOptions()
{
	// Create the PNGSaveOptions object to set the PNG options
	var PNGSaveOpts = new ExportOptionsPNG24();
	
	// Setting PNGSaveOptions properties. Please see the JavaScript Reference
	// for a description of these properties.
	// Add more properties here if you like
	PNGSaveOpts.antiAliasing = true;
	PNGSaveOpts.artBoardClipping = true;
    
	PNGSaveOpts.horizontalScale = 300;
	PNGSaveOpts.verticalScale = 300;
    if (!doPngResize) {
        PNGSaveOpts.horizontalScale = 100;
        PNGSaveOpts.verticalScale = 100;
    	PNGSaveOpts.artboardRange = '1';
    }
	PNGSaveOpts.transparency = true;
	
	// uncomment to view the PNGs after conversion.
	
    PNGSaveOpts.viewAfterSaving = true;

	return PNGSaveOpts;
}

/*********************************************************

getJPEGOptions: Function to set the JPEG saving options of the 
files using the JPEGSaveOptions object.

**********************************************************/

function getJPEGOptions()
{
	// Create the JPEGSaveOptions object to set the JPEG options
	var JPEGSaveOpts = new ExportOptionsJPEG();
	
	// Setting JPEGSaveOptions properties. Please see the JavaScript Reference
	// for a description of these properties.
	// Add more properties here if you like
	JPEGSaveOpts.antiAliasing = true;
	JPEGSaveOpts.horizontalScale = 120;
	JPEGSaveOpts.verticalScale = 120;
	JPEGSaveOpts.qualitySetting = 85;
	
	
	// uncomment to view the JPEGs after conversion.
	// JPEGSaveOpts.viewAfterSaving = true;
	

	return JPEGSaveOpts;
}




/*********************************************************

getAIOptions: Function to set the AI saving options of the 
files using the AISaveOptions object.

**********************************************************/

function getAIOptions()
{
	// Create the AISaveOptions object to set the AI options
	var AISaveOpts = new IllustratorSaveOptions();
	
	AISaveOpts.compatibility = saveVersion;
	
	// Setting AISaveOptions properties. Please see the JavaScript Reference
	// for a description of these properties.
	// Add more properties here if you like

	return AISaveOpts;
}

function zeroPad(num,count)
{
	var numZeropad = num + '';
	while(numZeropad.length < count) {
		numZeropad = "0" + numZeropad;
	}
return numZeropad;
}

// vim: ft=javascript
