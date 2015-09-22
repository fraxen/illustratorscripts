/**********************************************************

Hugo Ahlenius
All Rights Reserved
http://nordpil.com/

General utility functions

DESCRIPTION
	dispAlert Displays an alert, if Growl is installed, it will use that
	doTheBat  - Executes batch file
**********************************************************/
/* global $, File, alert */
/* jshint latedef: false */
/* exported dispAlert, ungroup, execBatchfile */


function dispAlert(message, title, icon, priority) {
	if (typeof title === 'undefined') { title = 'Illustrator ' + $.fileName.split('/').pop(); }
	if (typeof icon === 'undefined') { icon = 'c:\\users\\hugoa\\bin\\icon_illustrator.png'; }
	if (typeof priority === 'undefined') { priority = 1; }
	if (typeof message === 'undefined') { message = 'Illustrator ' + $.fileName.split('/').pop(); }
	if (new File('C:\\Program Files (x86)\\Growl for Windows\\growlnotify.exe').exists) {
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

/**
    APPLIES TO THE FUNCTIONS BELOW, ACQUIRED FROM http://www.cyworld.com/be2u/2801831
 *	all group to ungroup v.1 - CS, CS2,CS3,CS4
 *
 *	Author: Nokcha (netbluew@gmail.com)
 *	
 *	This Script  is Can be easily  ungrouping to all group items in the Document.
 *
 *
 * JS code (c) copyright: Jiwoong Song ( netbluew@nate.com )
 * Copyright (c) 2009 netbluew@nate.com
 * All rights reserved.
 *
 * This code is derived from software contributed to or originating on wundes.com
 *
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *        This product includes software developed by netbluew@nate.com
 *        and its contributors.
 * 4. Neither the name of wundes.com nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY WUNDES.COM AND CONTRIBUTORS
 * ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
 * TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE FOUNDATION OR CONTRIBUTORS
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */


function ungroup(obj)
{
	var elements = getChildAll(obj);
	if(elements.length<1){
		obj.remove();
		return;
	}else{
		for(var i=0;i<elements.length;i++)
		{
			try{
				if(elements[i].parent.typename !== 'Layer') {
					elements[i].moveBefore(obj);
				}
				if(elements[i].typename === 'GroupItem') {
					ungroup(elements[i]);
				}
			}catch(e){

			}
		}
	}
}

function getChildAll(obj)
{
	var childsArr = [];
	for(var i=0;i<obj.pageItems.length;i++) {
		childsArr.push(obj.pageItems[i]);
	}
	return childsArr;
}

