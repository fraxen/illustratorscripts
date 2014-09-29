// Fix exports from ArcGIS
/* jshint ignore:start */
#target Illustrator-18.064
#includepath (new File($.fileName)).parent 
#include 'utility.jsx'
/* global activeDocument,ZOrderMethod,ElementPlacement,dispAlert,ungroup */
/* jshint ignore:end */

var lyrBound = activeDocument.layers.add();
var newLayer;

lyrBound.name = "Frame guide";
lyrBound.printable = false;
lyrBound.zOrder(ZOrderMethod.SENDTOBACK);

var lyrMain = activeDocument.layers.getByName('Layers');

for (var intI=0; intI < lyrMain.layers.length; intI++) {
	// $.writeln(lyrMain.layers[intI].name);
	if (lyrMain.layers[intI].groupItems.length) {
		newLayer = activeDocument.layers.add();
		newLayer.name = lyrMain.layers[intI].name;
		newLayer.move(lyrMain, ElementPlacement.PLACEBEFORE);
		lyrMain.layers[intI].groupItems[0].move(newLayer,ElementPlacement.INSIDE);
		ungroup(newLayer.groupItems[0]);
	} else if (lyrMain.layers[intI].layers.length) {
		while (lyrMain.layers[intI].layers.length) {
			newLayer = activeDocument.layers.add();
			newLayer.name = lyrMain.layers[intI].layers[0].name;
			newLayer.move(lyrMain, ElementPlacement.PLACEBEFORE);
			lyrMain.layers[intI].layers[0].groupItems[0].move(newLayer,ElementPlacement.INSIDE);
			lyrMain.layers[intI].layers[0].remove();
			ungroup(newLayer.groupItems[0]);
		}
	}

	// Remove clipping path
	for (var intJ=0; intJ < newLayer.pathItems.length; intJ++) {
		if (newLayer.pathItems[intJ].clipping) {
			if (intI === 0) {
				// If this is the first layer, move the clipping path to the 'frame guide' layer, otherwise delete it
				newLayer.pathItems[intJ].move(lyrBound,ElementPlacement.INSIDE);
				lyrBound.visible = false;
			} else {
				newLayer.pathItems[intJ].remove();
			}
		}
	}
}

lyrMain.remove();

dispAlert('Converted ArcMap export\\n' + activeDocument.fullName);
