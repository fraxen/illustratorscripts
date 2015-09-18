/* {{{ COMMENT
    Crop to tiles
    
    The first in the selection needs to be a group with tiles, it will loop
    over this group, and the crop the bottom object

    By Hugo Ahlenius, Nordpil
    http://nordpil.com
}}} */ 

#include '/c/Users/hugoa/config/Application Data/illustrator_scripts/Nordpil'
#include 'utility.jsx'

var mySelection = activeDocument.selection;
$.writeln('hej')


dispAlert('Sorted ' + mySelection.length + ' text items');
