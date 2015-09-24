/* jshint ignore:start */
/* global Folder, prompt, app, $, dispAlert */
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
#target Illustrator
#includepath (new File($.fileName)).parent
#include 'utility.jsx'
#include '../zExtendables/extendables.jsx'
/* jshint ignore:end */
var workFolder = Folder.selectDialog('Path to folder to convert all files'),
	aiFiles = workFolder.getFiles(prompt('Pattern for conversion, e.g. "*.ai" or "*.eps" etc','*.ai','Pattern'));

// This is used by finalsave.js to prevent prompts
app.finalSaveNoPrompt = true;

var msgFinal = 'Folder: ' + workFolder.fsName.replace(/\\n/g,"\\\\n") + "\\n\\n";

for (var i = 0; i<(aiFiles.length); i++){
	// Loop over all the files, open the file, run 'finalsave.js' and close
	app.open(aiFiles[i]);
	/* jshint ignore:start */
	#include 'finalsave.jsx'
	/* jshint ignore:end */
	app.activeDocument.close();
	msgFinal = msgFinal + aiFiles[i].name + '\\n';
	//$.writeln ('Converted ' + (i+1) + '/' + aiFiles.length + ' - ' + aiFiles[i].name);
	dispAlert('Converted ' + (i+1) + '/' + aiFiles.length + ' - ' + aiFiles[i].name);
	$.sleep (2000);
}

dispAlert(msgFinal);

app.finalSaveNoPrompt = false;
