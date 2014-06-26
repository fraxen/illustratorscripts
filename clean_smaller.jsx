/* {{{ COMMENT
	clean_smaller.js
	delete paths smaller than the top one in the selection
	Note that it does calculate the areas as if the paths were square...

	Originally from:
	http://illustrator.hilfdirselbst.ch/dokuwiki/english/scripts/javascript/clean_smaller?s=clean%20smaller

	Further modified by Hugo Ahlenius

	... {{{ HISTORY......................................
		$Id: clean_smaller.jsx 1371 2013-10-17 10:05:31Z hugo $
	... }}} .............................................
}}} */ 

var delCount = 0;

// Prepare selection/array. If this is a full layer, use pathItems
mySelection = activeDocument.selection;
if (mySelection == '[GroupItem ]') {
	mySelection = mySelection[0].pathItems;
}

if (mySelection.length > 1){
		goal = mySelection[0];
		goalBox = goal.width * goal.height; // area of the goal bounding box
		for (i = 1; i<(mySelection.length); i++){
			// Loop over the entire selection
			obj = mySelection[i];
			obj_Box = obj.width * obj.height;
			if(obj_Box < goalBox){
				// If object/box smaller than the goalBox
				obj.remove()
				delCount++;
			}
	}
	alert( "Paths deleted : " + delCount );
} else {
	alert ( "Nothing selected" );
}
