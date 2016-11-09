/* jshint ignore:start */
/* global app, CMYKColor, prompt, BlendModes, dispAlert */
/**********************************************************
Hugo Ahlenius
 
bevel/emboss

DESCRIPTION
	Creates a raised effect using the currently selected path
**********************************************************/
#target Illustrator
#includepath (new File($.fileName)).parent 
#include 'utility.jsx'
#include '../zExtendables/extendables.jsx'
/* jshint ignore:end */

var pathBevel,
	pathBevelClip,
	pathEmboss,
	pathEmbossClip,
	colWhite = new CMYKColor(),
	colBlack = new CMYKColor(),
	colPurple = new CMYKColor(),
	nudgeDist = prompt('Nudge distance', app.activeDocument.width / 1500)
	;
	
colBlack.black = 100;
colPurple.magenta = 100;

app.activeDocument.selection[0].layer.name = 'Bevel/Emboss';
app.copy();

pathBevel = app.activeDocument.selection[0];
pathBevelClip = pathBevel.duplicate();
pathEmboss = app.activeDocument.selection[0].duplicate();
pathEmbossClip = pathEmboss.duplicate();

pathBevel.name = 'Bevel';
pathEmboss.name = 'Emboss';
pathBevelClip.name = 'Bevel (clip)';
pathEmbossClip.name = 'Emboss (clip)';

function getCI(thisPageItem) {
	if (thisPageItem.parent.typename === 'CompoundPathItem' && thisPageItem.parent.parent.typename === 'Layer') {
		return thisPageItem.parent;
	}
	if (thisPageItem.parent.typename === 'Document') {
		return false;
	}
	return getCI(thisPageItem.parent);
}

function cleanMagenta(items) {
	Number.range(items.length).reverse().forEach(
		function(i) {
			var thisPath = items[i];
			if (thisPath.typename === 'CompoundPathItem' && thisPath.pathItems[0].fillColor.magenta === 100) {
				thisPath.remove();
			} else if (thisPath.typename !== 'CompoundPathItem' && thisPath.fillColor.magenta === 100) {
				thisPath.remove();
			}
		}
	);
}

Number.range(app.activeDocument.pathItems.length).forEach(
	function(i) {
		var thisPath = app.activeDocument.pathItems[i];
		switch (getCI(thisPath)) {
			case pathBevel:
				thisPath.filled = true;
				thisPath.fillColor = colWhite;
				thisPath.stroked = false;
				break;
			case pathEmboss:
				thisPath.filled = true;
				thisPath.fillColor = colBlack;
				thisPath.stroked = false;
				break;
			case pathBevelClip:
			case pathEmbossClip:
				thisPath.filled = true;
				thisPath.fillColor = colPurple;
				thisPath.stroked = false;
				break;
			default:
				break;
		}
		return;
	}
);

pathBevelClip.translate(nudgeDist, -nudgeDist);
pathEmbossClip.translate(-nudgeDist, nudgeDist);

app.activeDocument.selection = false;
pathBevelClip.selected = true;
pathBevel.selected = true;
app.executeMenuCommand ('group');
app.executeMenuCommand ('Live Pathfinder Trim');
app.executeMenuCommand ('expandStyle');
app.activeDocument.layers.getByName('Bevel/Emboss').selected = true;
cleanMagenta(app.activeDocument.selection[0].pageItems);
app.executeMenuCommand ('compoundPath');
app.activeDocument.selection[0].name = 'Bevel';
app.activeDocument.selection[0].opacity = 40;
app.activeDocument.selection[0].blendingMode = BlendModes.LIGHTEN;

app.activeDocument.selection = false;
pathEmbossClip.selected = true;
pathEmboss.selected = true;
app.executeMenuCommand ('group');
app.executeMenuCommand ('Live Pathfinder Trim');
app.executeMenuCommand ('expandStyle');
app.activeDocument.layers.getByName('Bevel/Emboss').selected = true;
cleanMagenta(app.activeDocument.selection[0].pageItems);
app.executeMenuCommand ('compoundPath');
app.activeDocument.selection[0].name = 'Emboss';
app.activeDocument.selection[0].opacity = 40;
app.activeDocument.selection[0].blendingMode = BlendModes.MULTIPLY;

dispAlert('Finished bevel/emboss!');
