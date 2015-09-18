// Fix exports from ArcGIS
/* jshint ignore:start */
#target Illustrator-18.064
#include '/c/Users/hugoa/config/Application Data/illustrator_scripts/zExtendables/extendables.jsx'
#includepath (new File($.fileName)).parent 
#include 'utility.jsx'
/* global $,activeDocument,ZOrderMethod,ElementPlacement,dispAlert,ungroup,getChildAll */
/* jshint ignore:end */

var lyrBound = activeDocument.layers.add();
var thisLayer, lyrMain;
var firstClip = true;

lyrBound.name = "Frame guide";
lyrBound.printable = true;
lyrBound.zOrder(ZOrderMethod.SENDTOBACK);
lyrBound.printable = false;

try {
	lyrMain = activeDocument.layers.getByName('Layers');
}
catch(err) {
	lyrMain = activeDocument.layers[0];
}

function removeClip(thisLayer) {
	var elements = getChildAll(thisLayer);
	for (var j=0; j < elements.length; j++) {
		if (elements[j].clipping) {
			if (firstClip) {
				// If this is the first layer, move the clipping path to the 'frame guide' layer, otherwise delete it
				try {
					elements[j].move(lyrBound,ElementPlacement.INSIDE);
				}
				catch (err) {
					$.writeln("Failed to move clipping mask to frame layer");
					$.writeln(err);
				}
				lyrBound.visible = false;
				firstClip = false;
			} else {
				elements[j].remove();
			}
		}
	}
}

for (var i=0; i < lyrMain.layers.length; i++) {
	// $.writeln(lyrMain.layers[i].name);
	if (lyrMain.layers[i].groupItems.length) {
		thisLayer = activeDocument.layers.add();
		thisLayer.name = lyrMain.layers[i].name;
		thisLayer.move(lyrMain, ElementPlacement.PLACEBEFORE);
		lyrMain.layers[i].groupItems[0].move(thisLayer,ElementPlacement.INSIDE);
		ungroup(thisLayer.groupItems[0]);
		removeClip(thisLayer);
	} else if (lyrMain.layers[i].layers.length) {
		while (lyrMain.layers[i].layers.length) {
			lyrMain.layers[i].layers[0].name = lyrMain.layers[i].name + '-' + lyrMain.layers[i].layers[0].name;
			while (lyrMain.layers[i].layers[0].layers.length) {
				while (lyrMain.layers[i].layers[0].layers[0].pageItems.length) {
					lyrMain.layers[i].layers[0].layers[0].pageItems[0].move(lyrMain.layers[i].layers[0],ElementPlacement.INSIDE);
				}
				lyrMain.layers[i].layers[0].layers[0].remove();
			}
			while(lyrMain.layers[i].layers[0].groupItems.length) {
				ungroup(lyrMain.layers[i].layers[0].groupItems[0]);
			}
			removeClip(lyrMain.layers[i].layers[0]);
			lyrMain.layers[i].layers[0].move(lyrMain,ElementPlacement.PLACEBEFORE);
		}
	}
}

lyrMain.remove();

dispAlert('Converted ArcMap export\\n' + activeDocument.fullName);
