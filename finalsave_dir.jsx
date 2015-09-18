/**********************************************************

Hugo Ahlenius
All Rights Reserved
http://nordpil.com/

finalsave_dir.js

DESCRIPTION
	Runs 'finalsave.js' on all files in a specified directory
	This file is depending on that script, and it needs to
	reside in the same folder.
 
**********************************************************/
#include '/c/Users/hugoa/config/Application Data/illustrator_scripts/Nordpil'
var workFolder = Folder.selectDialog('Path to folder to convert all files');
var aiFiles = workFolder.getFiles(prompt('Pattern for conversion, e.g. "*.ai" or "*.eps" etc','*.ai','Pattern'));

// This is used by finalsave.js to prevent prompts
app.finalSaveNoPrompt = true;

var msgFinal = 'Folder: ' + workFolder.fsName.replace(/\\n/g,"\\\\n") + "\\n\\n";

for (var i = 0; i<(aiFiles.length); i++){
	// Loop over all the files, open the file, run 'finalsave.js' and close
	app.open(aiFiles[i]);
	#include 'finalsave.jsx'
	app.activeDocument.close();
	msgFinal = msgFinal + aiFiles[i].name + '\\n';
	//$.writeln ('Converted ' + (i+1) + '/' + aiFiles.length + ' - ' + aiFiles[i].name);
	var fBatch = new File ($.getenv('temp') + '/finalsavedir.bat');
	fBatch.open('w:');
	fBatch.writeln ('start Growlnotify.exe /p:-1 /t:"Illustrator finalsave_dir.js" /ai:c:\\users\\hugoa\\bin\\icon_illustrator.png "Converted ' + (i+1) + '/' + aiFiles.length + ' - ' + aiFiles[i].name + '"');
	fBatch.close();
	fBatch.execute();
	$.sleep (2000);
}

var fBatch = new File ($.getenv('temp') + '/finalsavedir.bat');
fBatch.open('w:');
fBatch.writeln ('start Growlnotify.exe /p:2 /t:"Illustrator finalsave_dir.js" /ai:c:\\users\\hugoa\\bin\\icon_illustrator.png "' + msgFinal + '"');
fBatch.close();
fBatch.execute();
app.finalSaveNoPrompt = false;


function zeroPad(num,count)
{
	var numZeropad = num + '';
	while(numZeropad.length < count) {
		numZeropad = "0" + numZeropad;
	}
return numZeropad;
}
