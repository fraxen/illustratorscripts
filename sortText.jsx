/* {{{ COMMENT
    Sort selected point type objects in alphabetical order

	By Hugo Ahlenius, Nordpil
	http://nordpil.com
}}} */ 

#include '/c/Users/hugoa/config/Application Data/illustrator_scripts/Nordpil'
#include 'utility.jsx'

var oldText,newRect,newText,targetZOrder,i,j;
var changeCount = 0;

var mySelection = activeDocument.selection;

// set up an array of text objects
var txtStrings = new Array;
for (var i = 0; i<(mySelection.length); i++){
    txtStrings.push(mySelection[i].contents);
}

txtStrings.sort()

for (var i = 0; i<(txtStrings.length); i++){
    for(var j = 0; j < (mySelection.length); j++) {
        if ( mySelection[j].contents == txtStrings[i] ) {
            mySelection[j].zOrder(ZOrderMethod.SENDTOBACK);
        }
    }
}


dispAlert('Sorted ' + mySelection.length + ' text items');
