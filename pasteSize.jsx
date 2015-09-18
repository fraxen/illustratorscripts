/* jshint ignore:start */
#target Illustrator-18
#include '/c/Users/hugoa/config/Application Data/illustrator_scripts/zExtendables/extendables.jsx'
#include '/c/home/hugoa/config/Application Data/illustrator_scripts/Nordpil/utility.jsx'
/* global activeDocument,app,Transformation,dispAlert */
/* jshint ignore:end */

var target = {
	'width': 0,
	'height': 0,
	'position': []
};
var ref = {
	'width': 0,
	'height': 0,
	'position': []
};
var theOrigin = activeDocument.rulerOrigin;

// paste the stuff
app.paste();

// find the reference
var refLayer = activeDocument.selection.last().layer;
var items = activeDocument.selection;
for (var i=0; i < items.length; i++) {
	if (items[i].layer === refLayer && items[i].width > ref.width) {
		ref.width = items[i].width;
		ref.height = items[i].height;
		ref.position = items[i].position;
	}
}

// Get the position and width/height of the bottom layer
var targetLayer = activeDocument.layers[activeDocument.layers.length-1];
var items = targetLayer.pageItems;
for (var i=0; i < items.length; i++) {
	if (items[i].width > target.width) {
		target.width = items[i].width;
		target.height = items[i].height;
		target.position = items[i].position;
	}
}

// move and scale the selection
var items = activeDocument.selection;
var moveX, moveY, scale;
activeDocument.rulerOrigin = ref.position;
for (var i=0; i < items.length; i++) {
	scale = target.width/ref.width * 100;
	items[i].resize(scale, scale, true, true, true, true, 0, Transformation.DOCUMENTORIGIN);
	moveX = target.position.first() - ref.position.first();
	moveY = target.position.last() - ref.position.last();
	items[i].translate(moveX, moveY, true, true, true, true);
}
activeDocument.rulerOrigin = theOrigin;

// Delete reference layer/items
var items = activeDocument.selection;
for (var i=0; i < items.length; i++) {
	if (items[i].layer === items.last().layer) {
		items[i].remove();
	}
}

dispAlert('Pasted and transformed!');
