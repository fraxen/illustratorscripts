/* {{{ COMMENT
	Convert selected objects from point type objects to area type objects
	If none are selected, it will convert all unlocked point type objects

	Note that I have seen some odd issues, maybe bugs:
		zOrderPosition returns an "Internal Error"
		also error 1346458189

	By Hugo Ahlenius, Nordpil
	http://nordpil.com
}}} */ 

#includepath '/c/users/hugoa/config/Application Data/illustrator_cs5_settings/Scripts/Nordpil'
#include 'utility.jsx'

var oldText,newRect,newText,targetZOrder,i,j;
var changeCount = 0;

function updateToDo (arrToDo, textObj) {
	// Function to add a text object, if valid, to the array of items to do
	if (textObj.typename == "TextFrame" && textObj.kind == TextType.POINTTEXT && !textObj.locked) arrToDo.push(textObj);
}

var mySelection = activeDocument.selection;
if (mySelection.length == 0) mySelection = activeDocument.textFrames; // If no objects are selected, do all text frames in the doc...

// set up an array of text objects
var txtObjs = new Array;
for (var i = 0; i<(mySelection.length); i++){
	if (mySelection[i] == '[GroupItem ]') {
		for (var j = 0; j<(mySelection[i].textFrames.length); j++){
			updateToDo(txtObjs,mySelection[i].textFrames[j]);
		}
	} else {
		updateToDo(txtObjs,mySelection[i]);
	}
}

// Convert the old text objects from path type to area type, using the rectangles they had already
for (var i = 0; i<(txtObjs.length); i++){
	oldText = txtObjs[i];
	newRect = oldText.parent.pathItems.rectangle(oldText.top,oldText.left,oldText.width,oldText.height);
	newText = oldText.parent.textFrames.areaText(newRect);
	oldText.textRange.duplicate(newText);
	// Adjust zOrder/placing
	try {
		do {
			newText.zOrder(ZOrderMethod.SENDBACKWARD);
		} while (newText.zOrderPosition > oldText.zOrderPosition)
	}
	catch(err) {}
	changeCount++;
}

// Remove the changed objects...
for (var i = 0; i < txtObjs.length; i++) txtObjs[i].remove();

dispAlert('Converted ' + changeCount + ' point type objects to area type');
