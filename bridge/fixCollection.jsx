/* jshint ignore:start */
#target Bridge
#include '/c/users/hugoa/config/Application Data/illustrator_scripts/Nordpil/utility.jsx'
#include '/f/temp/fixCollectionArgs.jsx'
/* global app,dispAlert,Thumbnail,Folder,projectPath,project,$ */
/* jshint ignore:end */

var projectFolder = new Thumbnail(Folder(projectPath));
var gfxToAdd = [];

function getCollection(collName) {
	var allCollections = app.getCollections();
	for (var i in allCollections) {
		if (allCollections[i].name === collName) {
			return allCollections[i];
		}
	}
	return null;
}

if (getCollection(project) !== null) {
	app.deleteCollection(getCollection(project));
}
var coll = app.createCollection(project);
var collAll = getCollection('All');

// Find files to add
projectFolder.open();
projectFolder.refresh();
app.buildFolderCache(projectFolder, true);
coll.refresh();
for (var i in projectFolder.children) {
	// $.writeln(projectFolder.children[i].name);
	if (
		projectFolder.children[i].type === 'folder' &&
		projectFolder.children[i].name !== '_discussion' &&
		projectFolder.children[i].name !== '_output'
	) {
		projectFolder.children[i].open();
		projectFolder.children[i].refresh();
		for (var j in projectFolder.children[i].children) {
			if (
				projectFolder.children[i].children[j].name.split('.').pop() === 'ai' ||
				projectFolder.children[i].children[j].name.split('.').pop() === 'pdf'
			) {
				gfxToAdd.push(projectFolder.children[i].children[j]);
			}
		}
	}
}

// Remove files in the 'All' collection
collAll.refresh();
for (var i=collAll.children.length; i--;) {
	if ( collAll.children[i].spec.fullName.match(projectPath) != null ) {
		app.removeCollectionMember(collAll, collAll.children[i]);
	}
}

// Add found files to collection
for (var i in gfxToAdd) {
	app.addCollectionMember(coll, gfxToAdd[i]);
	app.addCollectionMember(collAll, gfxToAdd[i]);
}
coll.refresh();


dispAlert('Added ' + gfxToAdd.length + ' files to collection ' + coll.name, 'Fix Collection', 'c:\\users\\hugoa\\bin\\icon_bridge.png');
