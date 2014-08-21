/* jshint ignore:start */
/* global ExternalObject,$,File,XML */
/* global XMPFile,XMPConst,XMPMeta,XMPUtils */
#target Bridge
#includepath (new File($.fileName)).parent 
#include 'utility.jsx'
/* jshint ignore:end */
var allFiles = [];
allFiles.push("/c/project/1001 siwi west asia/graphics/02_jordangw/02_jordangw.ai");
allFiles.push("/c/project/1001 siwi west asia/graphics/_output/02_jordangw.ai");
allFiles.push("/c/project/1002 food security/graphics/101a_foodpriceindex/1_101a_FoodPriceIndex_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/101b_foodcommodityindices/1_101b_FoodCommodityIndices.ai");
allFiles.push("/c/project/1002 food security/graphics/101c_commodityprices/1_101c_commoditypriceindex.ai");
allFiles.push("/c/project/1002 food security/graphics/102_commodityvsoil/1_102_commodityvsoil.ai");
allFiles.push("/c/project/1002 food security/graphics/201_populationgrowth/2_201_populationgrowth.ai");
allFiles.push("/c/project/1002 food security/graphics/202a_incomedistributionchart/2_202a_incomedistributionchart_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/202b_incomedistribution/2_202b_incomedistribution.ai");
allFiles.push("/c/project/1002 food security/graphics/203_agriculturaltrends/2_203_agriculturaltrends.ai");
allFiles.push("/c/project/1002 food security/graphics/204_africaworldffpi/2_204_africaworldffpi_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/205_agyieldtrends/2_205_agyieldtrends.ai");
allFiles.push("/c/project/1002 food security/graphics/300_croplandpotential/3_300_croplandpotential.ai");
allFiles.push("/c/project/1002 food security/graphics/301_productionincreases/3_301_productionincreases.ai");
allFiles.push("/c/project/1002 food security/graphics/302a_fishlandings/3_302a_fishproduction.ai");
allFiles.push("/c/project/1002 food security/graphics/302b_depthoffishcatches/3_302b_depthoffishcatches.ai");
allFiles.push("/c/project/1002 food security/graphics/401_globallanddegradation/4_401_landdegradation.ai");
allFiles.push("/c/project/1002 food security/graphics/403_biofuelsproduction/4_403a_biofuelsproduction.ai");
allFiles.push("/c/project/1002 food security/graphics/403_biofuelsproduction/4_403b_biofuelsproduction.ai");
allFiles.push("/c/project/1002 food security/graphics/405_climateagriculture/4_405_climateagriculture.ai");
allFiles.push("/c/project/1002 food security/graphics/407_rainfall/4_407_rainfallgdp_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/408_badbugs/4_408_badbugs.ai");
allFiles.push("/c/project/1002 food security/graphics/409_watermdghunger/4_409_watermdghunger.ai");
allFiles.push("/c/project/1002 food security/graphics/410a_himalayascenario/4_410a_himalayscenario.ai");
allFiles.push("/c/project/1002 food security/graphics/410b_himalayamap/4_410b_himalayabasins_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/414_invasivevectors/4_414_invasivevectors_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/416_africaclimate2080/4_416_africaclimate2080.ai");
allFiles.push("/c/project/1002 food security/graphics/419_temperaturescenarios/4_419a_temperaturescenarios_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/419_temperaturescenarios/4_419b_temperaturescenarios_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/421_foodconsumptiontrends/4_421_foodconsumptiontrends_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/424_farmlandbirds/4_424_farmlandbirds.ai");
allFiles.push("/c/project/1002 food security/graphics/425_africandroughts/4_425_africadroughts.ai");
allFiles.push("/c/project/1002 food security/graphics/501_scenarios/5_501_productionscenarios.ai");
allFiles.push("/c/project/1002 food security/graphics/601_worldagriculturetrade/6_601_worldagriculturetrade.ai");
allFiles.push("/c/project/1002 food security/graphics/602_urbanizationindevelopingcountries/6_602_urbanizationindevelopingcountries.ai");
allFiles.push("/c/project/1002 food security/graphics/603_supermarketfood/6_603_supermarketfoodratio.ai");
allFiles.push("/c/project/1002 food security/graphics/604_topgrocery/6_604_topgrocery.ai");
allFiles.push("/c/project/1002 food security/graphics/605_mosantoshare/6_605_monsantoshare.ai");
allFiles.push("/c/project/1002 food security/graphics/606_animalfoodtrends/6_606_animalfoodtrends.ai");
allFiles.push("/c/project/1002 food security/graphics/607_marketaccess/6_607_marketaccess.ai");
allFiles.push("/c/project/1002 food security/graphics/608_conflicts/6_608_conflicts.ai");
allFiles.push("/c/project/1002 food security/graphics/801_foodchainlosses/8_801_foodchainlosses.ai");
allFiles.push("/c/project/1002 food security/graphics/802_foodwaste/8_802_foodwaste.ai");
allFiles.push("/c/project/1002 food security/graphics/803_dietarychanges/8_803_dietarychanges.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/1_101a_FoodPriceIndex_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/1_101b_FoodCommodityIndices.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/1_101c_commoditypriceindex.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/1_102_commodityvsoil.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/2_201_populationgrowth.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/2_202a_incomedistributionchart_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/2_202b_incomedistribution.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/2_203_agriculturaltrends.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/2_204_africaworldffpi_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/2_205_agyieldtrends.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/3_300_croplandpotential.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/3_301_productionincreases.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/3_302a_fishproduction.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/3_302b_depthoffishcatches.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_401_landdegradation.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_403a_biofuelsproduction.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_403b_biofuelsproduction.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_405_climateagriculture.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_407_rainfallgdp_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_408_badbugs.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_409_watermdghunger.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_410a_himalayscenario.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_410b_himalayabasins_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_414_invasivevectors_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_416_africaclimate2080.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_419a_temperaturescenarios_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_419b_temperaturescenarios_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_421_foodconsumptiontrends_ot.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_424_farmlandbirds.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/4_425_africadroughts.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/5_501_productionscenarios.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/6_601_worldagriculturetrade.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/6_602_urbanizationindevelopingcountries.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/6_603_supermarketfoodratio.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/6_604_topgrocery.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/6_605_monsantoshare.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/6_606_animalfoodtrends.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/6_607_marketaccess.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/6_608_conflicts.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/8_801_foodchainlosses.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/8_802_foodwaste.ai");
allFiles.push("/c/project/1002 food security/graphics/_output/8_803_dietarychanges.ai");
allFiles.push("/c/project/1002 food security/graphics/_scrapped/411_oxygendepletion/4_411_oxygendepletion.ai");
allFiles.push("/c/project/1004 grida polar/graphics/icetrendmap/icetrendmap2008.ai");
allFiles.push("/c/project/1004 grida polar/graphics/icetrends/icetrends2008.ai");
allFiles.push("/c/project/1011 siwi central asia/graphics/00_overview/00_overview.ai");
allFiles.push("/c/project/1011 siwi central asia/graphics/01_waterbalance/01_waterbalance.ai");
allFiles.push("/c/project/1011 siwi central asia/graphics/02_groundwater/02_groundwater.ai");
allFiles.push("/c/project/1011 siwi central asia/graphics/_output/00_overview.ai");
allFiles.push("/c/project/1011 siwi central asia/graphics/_output/01_waterbalance.ai");
allFiles.push("/c/project/1011 siwi central asia/graphics/_output/02_groundwater.ai");
allFiles.push("/c/project/zGRID projects/203/088 GEO 4 Ice and Snow/graphics/5_trends/5_arctictrends2008.ai");
 hubby
// Load the XMP Script library
var xmlFile, oldMeta, thisXmlfile, fileMeta = {}, failedFiles = [];
var xmpLib = new ExternalObject( 'lib:AdobeXMPScript' );

for ( var i = 0; i<( allFiles.length ); i++ ) {
	thisXmlfile = allFiles[i].replace('.ai','.xml');
	$.writeln( (i+1) + '/' + allFiles.length + ' - ' + thisXmlfile );
	// read in all meta from the old xml file
	try {
		xmlFile = new File( thisXmlfile );
		xmlFile.open('r');
		oldMeta = new XML (xmlFile.read());
		xmlFile.close();
		fileMeta = {};
		fileMeta.title = oldMeta.xpath('title');
		fileMeta.notes = oldMeta.xpath('notes');
		fileMeta.projection = oldMeta.xpath('projection');
		fileMeta.originator = oldMeta.xpath('originator');
		fileMeta.credit = oldMeta.xpath('credit');
		fileMeta.caption = oldMeta.xpath('caption');
		fileMeta.sources = [];
		if ( oldMeta.xpath('sources/source').length() > 0 ) {
			for ( var j = 1; j < ( oldMeta.xpath('sources/source').length()+1 ); j++ ) {
				fileMeta.sources.push( oldMeta.xpath('sources/source[' + j + ']') );
			}
		}

		// now we enter this into the specified .ai file
		var aiFile = new File (allFiles[i]);
		var xmpf = new XMPFile( aiFile.fsName, XMPConst.UNKNOWN, XMPConst.OPEN_FOR_UPDATE);
		var docXmp = xmpf.getXMP();
		var myXmp = new XMPMeta( docXmp.serialize() );
		var myNamespace = 'http://nordpil.com/';  
		var myPrefix = 'nordpil:';  
		XMPMeta.registerNamespace( myNamespace, myPrefix );
		if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'title' ) ) {
			myXmp.setProperty( XMPConst.NS_DC, 'title', null, XMPConst.PROP_IS_ARRAY );
		}
		myXmp.setProperty( XMPConst.NS_DC, 'title/*[1]', fileMeta.title );
		if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'description' ) ) {
			myXmp.setProperty( XMPConst.NS_DC, 'description', null, XMPConst.PROP_IS_ARRAY );
		}
		if ( fileMeta.caption.length >0) {
			myXmp.setProperty( XMPConst.NS_DC, 'description/*[1]', fileMeta.caption );
		}
		myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'AuthorsPosition', 'Designer' );
		myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'CaptionWriter', 'Hugo Ahlenius, Nordpil' );
		myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'City', 'Stockholm' );
		myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'State', 'Stockholm' );
		myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'Country', 'Sweden' );
		myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'Instructions', fileMeta.notes );
		if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'creator' ) ) {
			myXmp.setProperty( XMPConst.NS_DC, 'creator', null, XMPConst.PROP_IS_ARRAY );
		}
		myXmp.setProperty( XMPConst.NS_DC, 'creator/*[1]', fileMeta.originator );
		myXmp.setProperty( XMPConst.NS_PHOTOSHOP, 'Credit', fileMeta.credit );
		myXmp.setProperty( myNamespace, 'projection', fileMeta.projection );
		if ( fileMeta.sources.length ) {
			if ( !myXmp.doesPropertyExist( XMPConst.NS_DC, 'datasources' ) ) {
				myXmp.setProperty( myNamespace, 'datasources', null, XMPConst.PROP_IS_ARRAY );
			}
			for ( var j = 0; j<( fileMeta.sources.length ); j++ ) {
				myXmp.setProperty( myNamespace, 'datasources/*[' + (j+1) + ']', fileMeta.sources[j] );
			}
		}
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr', 'c/o SRC; Kräftriket 2b' );
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrCity', 'Stockholm' );
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrRegion', 'Stockholm' );
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrPcode', 'SE-10691' );
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiAdrCtry', 'Stockholm' );
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiTelWork', '+46-757575284' );
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiEmailWork', 'hugo.ahlenius@nordpil.com' );
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CreatorContactInfo/Iptc4xmpCore:CiUrlWork', 'http://nordpil.com' );
		myXmp.setProperty( XMPConst.NS_IPTC_CORE, 'CountryCode', 'SE' );
		
		// save back the metadata
		XMPUtils.appendProperties( myXmp, docXmp, XMPConst.APPEND_REPLACE_OLD_VALUES );
		xmpf.putXMP( docXmp );
	} catch(e) {
		$.writeln ('FAILED: ' + allFiles[i]);
		failedFiles.push(allFiles[i]);
	}
	
	try {
		xmpf.closeFile( XMPConst.CLOSE_UPDATE_SAFELY );
	} catch(e) {
	}
}
xmpLib.unload();

$.writeln('Finished!!!\n\n----------\nFailed files:\n' + failedFiles);
