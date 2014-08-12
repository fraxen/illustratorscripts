/* jshint ignore:start */
/* global app,dispAlert,Compatibility,UserInteractionLevel,File,confirm */
/* global ExternalObject,XMPMeta,XMPConst,prompt,zeroPad,XMPUtils,XMPFile,$ */
/* global ExportType,execBatchfile,Folder,PDFSaveOptions,CompressionQuality */
/* global EPSSaveOptions,ExportOptionsPNG24,IllustratorSaveOptions */
/**********************************************************
Hugo Ahlenius
 
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

**********************************************************/
#target Illustrator-18.064
#includepath (new File($.fileName)).parent 
#include 'utility.jsx'
alert($.fileName)
/* jshint ignore:end */

var saveVersion = Compatibility.ILLUSTRATOR17;
var doPngResize = true;

/*********************************************************

getNewName: Function to get the new file name. The primary
name is the same as the source file.

**********************************************************/

function getNewName(docName, destFolder, newExt, maxLen) {
	var ext =  newExt; // new extension for file
	var newName = "";
	if (isNaN(maxLen)) { maxLen = 1000; }
	
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
	return new File( destFolder + '/' + newName );
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


if (!(app.finalSaveNoPrompt)) {
	dispAlert('Starting saving...','Illustrator finalsave.js');
}

var now = new Date();
var nowString = '';

if (app.activeDocument.XMPString.match('for CS3') === 'for CS3') {
	saveVersion = Compatibility.ILLUSTRATOR13;
}

if (app.activeDocument.XMPString.match('for CS2') === 'for CS2') {
	saveVersion = Compatibility.ILLUSTRATOR12;
}

if (app.activeDocument.XMPString.match('noPngResize') === 'noPngResize') {
	doPngResize = false;
}
// Main Code [Execution of script begins here]
var progFiles = "c:\\program";

// uncomment to suppress Illustrator warning dialogs
app.userInteractionLevel = UserInteractionLevel.DONTDISPLAYALERTS;

var i, sourceDoc, targetFileEPS, targetFilePDF, targetFileAI, targetFileTemp;

var destFolder = null;
// Get the destination to save the files
destFolder = app.activeDocument.fullName.path;
sourceDoc = app.activeDocument;
var originalName = sourceDoc.name;
// {{{ METADATA STUFF
// Check if an old metadata file exists...
var metaFile = new File(getNewName(originalName,destFolder, '.xml'));
if ( metaFile.exists ) {
	if ( confirm( 'Delete existing xml metadata file', true ) ) { metaFile.remove(); }
}

// Load the XMP Script library
var xmpLib = new ExternalObject( 'lib:AdobeXMPScript' );
//Create an XMPMeta object from the active documents XMPString:
var docXmp = new XMPMeta( app.activeDocument.XMPString );
//Make a copy that we can work with:
var myXmp = new XMPMeta( docXmp.serialize() );
var myNamespace = 'http://nordpil.com/';  
var myPrefix = 'nordpil:';  
XMPMeta.registerNamespace( myNamespace, myPrefix );  
//Make our changes:

// Test if we need to add defaults, and propmt for values
if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'creator[1]' ) ) {
	var now = new Date();
	var mTitle = prompt ('Title', myXmp.getProperty( XMPConst.NS_DC, 'title[1]' ) );
	var mCreator = prompt( 'Author', 'Hugo Ahlenius, Nordpil');
	var mDescription = prompt( 'Caption/description', '');
	var mNotes = prompt( 'Notes/instructions', '');
	var mProjection = prompt( 'Projection', '');
	var mSources = prompt( 'Sources (separate by semicolon)', '');
	var mKeywords = prompt( 'Keywords (separate by semicolon)', '');
	myXmp.setProperty( XMPConst.NS_DC, 'title/*[1]', mTitle );
	if ( mCreator.length ) {
		if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'creator' ) ) {
			myXmp.setProperty( XMPConst.NS_DC, 'creator', null, XMPConst.PROP_IS_ARRAY );
		}
		myXmp.setProperty( XMPConst.NS_DC, 'creator/*[1]', mCreator );
	}
	if ( mDescription.length ) {
		if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'description' ) ) {
			myXmp.setProperty( XMPConst.NS_DC, 'description', null, XMPConst.PROP_IS_ARRAY );
		}
		myXmp.setProperty( XMPConst.NS_DC, 'description/*[1]', mDescription );
	}
	myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'AuthorsPosition', 'Designer' );
	myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'CaptionWriter', 'Hugo Ahlenius, Nordpil' );
	myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'Credit', 'Hugo Ahlenius, Nordpil ' + now.getFullYear() );
	myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'City', 'Stockholm' );
	myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'State', 'Stockholm' );
	myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'Country', 'Sweden' );
	if ( mNotes.length ) { myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'Instructions', mNotes ); }
	myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'Source', 'Source' ); // source
	myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'DateCreated', now.getFullYear() + '/' + zeroPad(now.getMonth()+1,2) + '/'  + zeroPad(now.getDate(),2) );
	if ( mKeywords.length ) {
		if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'subject' ) ) {
			myXmp.setProperty( XMPConst.NS_DC, 'subject', null, XMPConst.PROP_IS_ARRAY );
		}
		var keys = mKeywords.split(';');
		for ( var i = 0; i<( keys.length ); i++ ) {
			myXmp.setProperty( XMPConst.NS_DC, 'subject/*[' + (i+1) + ']', keys[i] );
		}
	}
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr', 'c/o SRC; Kräftriket 2b' );
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrCity', 'Stockholm' );
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrRegion', 'Stockholm' );
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrPcode', 'SE-10691' );
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrCtry', 'Stockholm' );
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiTelWork', '+46-757575284' );
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiEmailWork', 'hugo.ahlenius@nordpil.com' );
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiUrlWork', 'http://nordpil.com' );
	myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CountryCode', 'SE' );
	if ( mProjection.length ) { myXmp.setProperty( myNamespace, 'projection', mProjection ); }
	if ( mSources.length ) {
		var sources = mSources.match(/("[^"]*")|[^;]+/g);
		if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'datasources' ) ) {
			myXmp.setProperty( myNamespace, 'datasources', null, XMPConst.PROP_IS_ARRAY );
		}
		for ( var i = 0; i<( sources.length ); i++ ) {
			myXmp.setProperty( myNamespace, 'datasources/*[' + (i+1) + ']', sources[i] );
		}
	}
	//Append the modified xmp to the original xmp object:
	XMPUtils.appendProperties( myXmp, docXmp, XMPConst.APPEND_REPLACE_OLD_VALUES );
	//Create a File object of the active document so we can use .fsName (XMPFile seems to be picky):
	var myDocFile = new File( app.activeDocument.fullName );
	//Open the active document for writing:
	var docRef = new XMPFile( myDocFile.fsName, XMPConst.FILE_UNKNOWN, XMPConst.OPEN_FOR_UPDATE );
	//Check that we can write the xmp before writing it
	docRef.putXMP( docXmp );
	docRef.closeFile( XMPConst.CLOSE_UPDATE_SAFELY );
	myDocFile.close();
	xmpLib.unload();
	var thisFileName = app.activeDocument.fullName;
	app.activeDocument.close();
	app.open(thisFileName);
	sourceDoc = app.activeDocument;
}
/// }}}

// }}}
// First Save as illustrator file in temp dir
targetFileAI = app.activeDocument.fullName;
var nowString = now.getFullYear() + '_' + zeroPad(now.getMonth()+1,2) + '_'  + zeroPad(now.getDate(),2) + '-' + zeroPad(now.getHours(),2) + '_'  + zeroPad(now.getMinutes(),2);
targetFileTemp = getNewName (originalName, $.getenv('temp'), nowString);
sourceDoc.saveAs (targetFileTemp, getAIOptions());

// The save for web/png...
var targetFilePNG = getNewName(originalName, destFolder, '');
var targetFilePNG2 = getNewName(originalName, destFolder, '');
var tempFile = new File(targetFilePNG2.fullName + '.png');
if (tempFile.exists) { tempFile.remove(); }
sourceDoc.exportFile (targetFilePNG, ExportType.PNG24, getPNGOptions());

// Then export to pdf
targetFilePDF = getNewName(originalName, destFolder, '.pdf');
var tempFile = new File(targetFilePDF);
if (tempFile.exists) { tempFile.remove(); }
if (doPngResize) { sourceDoc.saveAs(targetFilePDF, getPDFOptions()); }

// Then export to eps
targetFileEPS = getNewName(originalName, destFolder, '.eps');
var tempFile = new File(targetFileEPS);
if (tempFile.exists) { tempFile.remove(); }
if (doPngResize) { sourceDoc.saveAs(targetFileEPS, getEPSOptions()); }


// Fix the bitmaps - trim and create thumb
var pngFolder = targetFilePNG.fsName.replace(/\\[^\\]*$/,'');
var pngFileName = targetFilePNG.fsName.replace(/.*\\/,'');
var fBatch = 'if EXIST "' + pngFolder + '\\' + targetFilePDF.displayName.replace(/.pdf/,'-01.pdf') + '" move "' + pngFolder + '\\' + targetFilePDF.displayName.replace(/.pdf/,'-01.pdf') + '" "' + pngFolder + '\\' + targetFilePDF.displayName + '"\r';
fBatch += 'if NOT EXIST "' + pngFolder + '\\' + pngFileName + '.png" (\r';
fBatch += '   IF EXIST "' + pngFolder + '\\' + pngFileName.replace(/ /g,'-') + '.png" mv "' + pngFolder + '\\' + pngFileName.replace(/ /g,'-') + '.png" "' + pngFolder + '\\' + pngFileName + '.png"\r';
fBatch += '   IF EXIST "' + pngFolder + '\\' + pngFileName.replace(/\.[^\.]*$/g,'') + '.png" mv "' + pngFolder + '\\' + pngFileName.replace(/\.[^\.]*$/g,'') + '.png" "' + pngFolder + '\\' + pngFileName + '.png"\r';
fBatch += ')\r';

fBatch += 'if EXIST "' + targetFilePNG2.fsName + '.jpg" del "' + targetFilePNG2.fsName + '.jpg"\r';

if (!doPngResize) {
    fBatch += progFiles + '\\graphics\\imagemagick\\convert.exe -trim "' + targetFilePNG.fsName + '.png" "' + targetFilePNG2.fsName + '.png"\r';
} else {
    fBatch += 'copy ' + targetFilePNG.fsName + '.png" "' + targetFilePNG2.fsName + '.png"\r';
}
fBatch += progFiles + '\\graphics\\imagemagick\\convert.exe -background white -flatten +repage -antialias -quality 85 -support 0.9 -gamma 0.95 -filter Mitchell -resize x350 "' + targetFilePNG2.fsName + '.png" "' + targetFilePNG2.fsName + '.jpg"\r';
if (targetFilePNG.fsName !== targetFilePNG2.fsName) { fBatch += 'del "' + targetFilePNG.fsName + '.png"\r'; }
execBatchfile(fBatch);

// The save as illustrator again
sourceDoc.saveAs (targetFileAI, getAIOptions());

targetFilePNG.changePath(targetFilePNG2.fullName + '.png');

var alertString ='';
if (!(app.finalSaveNoPrompt)) {
	alertString = targetFileEPS.fsName + '\\n' + targetFilePDF.fsName + '\\n' + targetFileTemp.fsName  + '\\n';
	if (targetFilePNG.exists) {
		alertString = alertString + targetFilePNG2.fsName + '.png\\n' + targetFilePNG2.fsName + '.jpg';
	} else {
		alertString = alertString + '-----------------\\nBITMAP FILES WERE *NOT* SAVED, PLEASE INVESTIGATE RESOLUTION....';
	}
	alertString = alertString + '\\n-----------------\\nin folder: ' + new Folder(destFolder).fsName;
	alertString = alertString.replace(/\\/,'\\\\');
	dispAlert(alertString,"Illustrator finalsave.js");
}



// vim: ft=javascript
