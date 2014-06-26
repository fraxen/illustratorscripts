// Fix exports from ArcGIS
/* jshint ignore:start */
#target Illustrator-18.064
#includepath (new File($.fileName)).parent 
#include 'utility.jsx'
/* jshint ignore:end */

var lyrBound = activeDocument.layers.add();
var newLayer;

lyrBound.name = "Frame guide";
lyrBound.printable = false;
lyrBound.zOrder(ZOrderMethod.SENDTOBACK);

lyrMain = activeDocument.layers.getByName('Layers');

for (var intI=0; intI < lyrMain.layers.length; intI++) {
	// $.writeln(lyrMain.layers[intI].name);
	newLayer = activeDocument.layers.add();
	newLayer.name = lyrMain.layers[intI].name;
	newLayer.move(lyrMain, ElementPlacement.PLACEBEFORE);
	lyrMain.layers[intI].groupItems[0].move(newLayer,ElementPlacement.INSIDE);
	ungroup(newLayer.groupItems[0]);

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
				if(elements[i].parent.typename!="Layer")elements[i].moveBefore(obj);
				if(elements[i].typename=="GroupItem")ungroup(elements[i]);
			}catch(e){

			}
		}
	}
}

function getChildAll(obj)
{
	var childsArr = [];
	for(var i=0;i<obj.pageItems.length;i++)childsArr.push(obj.pageItems[i]);
	return childsArr;
}
