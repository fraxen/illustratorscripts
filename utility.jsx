/**********************************************************

Hugo Ahlenius
All Rights Reserved
http://nordpil.com/

General utility functions

DESCRIPTION
	dispAlert Displays an alert, if Growl is installed, it will use that
	doTheBat  - Executes batch file
**********************************************************/

function dispAlert(message, title, icon, priority) {
	if (typeof title === 'undefined') { title = 'Illustrator ' + $.fileName.split('/').pop(); }
	if (typeof icon === 'undefined') { icon = 'c:\\home\\hugo\\bin\\icon_illustrator.png'; }
	if (typeof priority === 'undefined') { priority = 1; }
	if (typeof message === 'undefined') { message = 'Illustrator ' + $.fileName.split('/').pop(); }
	if (new File('C:\\ProgramX86\\system\\growl\\Growl.exe').exists) {
		// Growl is installed, create batch file and run that
		execBatchfile('start Growlnotify.exe /p:' + priority + ' /t:"' + title + '" /ai:' + icon + ' "' + message + '"');
	} else {
		// Fall back to basic javascript alert
		alert(title + '\n\n' + message);
	}
}

function execBatchfile ( _data ) {     
	// Modified from https://forums.adobe.com/thread/470608
	try    
	{    
        var now = new Date();
		var nowString = now.getFullYear() + '_' + zeroPad(now.getMonth()+1,2) + '_'  + zeroPad(now.getDate(),2) + '-' + zeroPad(now.getHours(),2) + '_'  + zeroPad(now.getMinutes(),2);
		var _file = new File($.getenv('temp') + '/illy' + nowString +'.bat');    
		_file.open( 'w' );     
		_file.encoding = 'UTF-8';     
		_file.writeln ( _data );     
		_file.close();     
		var myVBScript = "Set WshShell = CreateObject(\"WScript.Shell\")\r";    
		myVBScript += 'WshShell.Run chr(34) & CreateObject(\"WScript.Shell\").ExpandEnvironmentStrings(\"%Temp%\") & \"\\illy' + nowString  + '.bat\" & Chr(34), 0\r';    
		myVBScript += "Set WshShell = Nothing\r";  
		myVBScript += "\r";    
		_file = new File($.getenv('temp') + '/illy' + nowString +'.vbs');    
		_file.open( 'w' );     
		_file.encoding = 'UTF-8';     
		_file.writeln ( myVBScript );     
		_file.close();     
		_file.execute();    
    } catch (e) {
		alert(e);  
	}    
}  
function zeroPad(num,count)
{
	var numZeropad = num + '';
	while(numZeropad.length < count) {
		numZeropad = "0" + numZeropad;
	}
return numZeropad;
}
