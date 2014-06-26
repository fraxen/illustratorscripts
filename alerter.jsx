/**********************************************************

Hugo Ahlenius
All Rights Reserved
http://nordpil.com/

alerter.js

DESCRIPTION
	Displays an alert, if Growl is installed, it will use that
**********************************************************/

function dispAlert(message, title, icon, priority) {
	if (typeof title === 'undefined') { title = 'Illustrator ' + $.fileName.split('/').pop(); }
	if (typeof icon === 'undefined') { icon = 'c:\\home\\hugo\\bin\\icon_illustrator.png'; }
	if (typeof priority === 'undefined') { priority = 1; }
	if (typeof message === 'undefined') { 'Illustrator ' + $.fileName.split('/').pop(); }
	if (new File('C:\\ProgramX86\\system\\growl\\Growl.exe').exists) {
		// Growl is installed, create batch file and run that
		var fBatch = new File ($.getenv('temp') + '/alerter.bat');
		fBatch.open('w:');
		fBatch.writeln ('start Growlnotify.exe /p:' + priority + ' /t:"' + title + '" /ai:' + icon + ' "' + message + '"');
		fBatch.close();
		fBatch.execute();
	} else {
		// Fall back to basic javascript alert
		alert(title + '\n\n' + message);
	};
}

