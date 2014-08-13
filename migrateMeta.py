import os
# {{{ ALL XML
allXml = [
    r'C:\project\1001 siwi west asia\graphics\00_overview\00_overview.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\01_euphtigrisgw\01_euphtigrisgw.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\01_euphtigrisgw\01_groundwaterlegend.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\01_euphtigrisov\01_euphtigrisow.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\02_jordangw\02_jordangw.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\02_jordanov\02_jordanov.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\03_arabianpgw\03_arabiangw.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\03_arabianpov\03_arabianov.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\04_waterbalance\04_waterbalance.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\05_gwall\05_gwall.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\00_overview.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\01_euphtigrisgw.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\01_euphtigrisow.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\01_groundwaterlegend.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\02_jordangw.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\02_jordanov.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\03_arabiangw.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\03_arabianov.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\04_waterbalance.xml',  # noqa
    r'C:\project\1001 siwi west asia\graphics\_output\05_gwall.xml',  # noqa
    r'C:\project\1002 food security\graphics\401_globallanddegradation\ws\npp9e_Dissolve.shp.xml',  # noqa
    r'C:\project\1002 food security\graphics\401_globallanddegradation\ws\npp9e_Dissolve1.shp.xml',  # noqa
    r'C:\project\1002 food security\graphics\401_globallanddegradation\ws\npp9e_Dissolve2.shp.xml',  # noqa
    r'C:\project\1002 food security\graphics\408_badbugs\ws\panel2_2.jpg.aux.xml',  # noqa
    r'C:\project\1002 food security\graphics\408_badbugs\ws\panel3_2.jpg.aux.xml',  # noqa
    r'C:\project\1002 food security\graphics\408_badbugs\ws\panel4_2.jpg.aux.xml',  # noqa
    r'C:\project\1002 food security\graphics\410b_himalayamap\ws\as_bas.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ahdr_bound\ws\ahdr2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ahdr_bound\ws\ahdr3.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ahdr_bound\ws\ahdr3_geo.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\bioclimate\ws\cp_bioclimate_la.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\floristicprovinces\incoming\florprov_la.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\floristicprovinces\ws\florprov2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\floristicprovinces\ws\florprov3_pnt.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\floristicprovinces\florprov_la.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice03_10.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice03_11.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice03_12.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice03_13.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice03_14.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice09_10.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice09_11.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice09_12.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice09_13.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\ice\ice09_14.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\income\ws\income1.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\income\ws\income2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\income\ws\income3.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\income\ws\income4kml2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\income\ws\income4kml3.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\avgjuly3\metadata.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\box2\metadata.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\info\arc0035.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\avgjuly11.tif.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\avgjuly12.bmp.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\avgjuly13_geo.tif.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\avgjuly4.png.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\avgjuly8x.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\bg2.bmp.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\julytemp\ws\land2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\lang8\metadata.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\lang9\metadata.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\language3\metadata.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\language5\metadata.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\lang11.png.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\lang13.bmp.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\lang14geo.bmp.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\lang15geo.tif.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\langlabel1.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\langlabel2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\language11.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\language2.png.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\language5.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\language\ws\temp_lang8.png.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\permafrost\ws\permaice2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\permafrost\ws\permaice3.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\popden\ws\grump_pd5\metadata.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\popden\grump_pd7.gif.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\popden\grump_pd7.gif.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\popden\grump_pd8_geo.png.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\popden\grump_pd9_geo.tif.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\incoming\wah.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\baffin1.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\herds1.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\herds2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\herds2_pnt1.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\hvidda1.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\iceland1.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\iceland2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\shampt1.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\rangifier\ws\wah2.shp.xml',  # noqa
    r'C:\project\1003 uarctic atlas\data\uarctic_map\new_UARCTIC_MAP_with_logo_329_0335Q2.jpg.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\docs\index_files\filelist.xml',  # noqa
    r'C:\project\1003 uarctic atlas\docs\index_files\master03.xml',  # noqa
    r'C:\project\1003 uarctic atlas\docs\index_files\pres.xml',  # noqa
    r'C:\project\1003 uarctic atlas\mapserver\capabilities_1_1_1.xml',  # noqa
    r'C:\project\1003 uarctic atlas\web\graphics\comingsoon.png.aux.xml',  # noqa
    r'C:\project\1003 uarctic atlas\web\map.uarctic.org\webroot\current\v3\config\mach-ii.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\basemap\boxg1\metadata.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\basemap\cntry06.sdc.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\basemap\cntry06_ln.sdc.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\basemap\country.sdc.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\basemap\latlong.sdc.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Denmark\LINE2.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Ireland\Corrib\Corrib\IRL_Corrib_Outline.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Ireland\Corrib\Corrib\IRL_Proposed_Pipieline_Route_Corrib.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Ireland\OSPAR1\Current_Authorisations.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Ireland\OSPAR1\gas_network.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Ireland\OSPAR1\Wells1970_2008.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Ireland\OSPAR_fields\offshore_fields.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Netherland\allFieldsExt\All_fields_external_juli_2007.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Netherland\Platforms_external_december_2007\Platforms_external_december_2007.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\newdiscoveries\disc_expoutp3.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\apa_open_dd\apa_open_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\Area_with_stratigraphic_licencing_dd\area_with_stratigraphic_licencing_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\Development_wellbores_dd\development_wellbores_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\Discoveries_dd\discoveries_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\Exploration_wellbores_dd\exploration_wellbores_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\facility_subsurface_dd\facility_subsurface_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\facility_surface_dd\facility_surface_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\fields_dd\ArcGis\fields_dd layer.lyr.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\fields_dd\fields_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\pipelines_dd\pipelines_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Norway\Production_licences_dd\production_licences_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\OSPAR-DATA\OSPAR_Contracting_Parties\OSPAR_Contracting_Parties.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\OSPAR-DATA\OSPAR_regions_polygons\OSPAR_regions_polygons.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\OSPAR-DATA\OSPAR_shoreline\OSPAR_shoreline.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Other_data\Shell - North Sea Data - August 2005\Shell - North Sea Data - August 2005\Data_ARC\NLD_arcdata\nld_pipelines.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Other_data\Shell - North Sea Data - August 2005\Shell - North Sea Data - August 2005\Data_ARC\NLD_arcdata\nld_protection.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Other_data\Shell - North Sea Data - August 2005\Shell - North Sea Data - August 2005\Output\Northern Europe Land ED50_31N Line.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Other_data\Shell - North Sea Data - August 2005\Shell - North Sea Data - August 2005\Output\Northern Europe Land ED50_32N Line.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Other_data\Shell - North Sea Data - August 2005\Shell - North Sea Data - August 2005\Output\Northern Europe Land ED50_32N.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Other_data\Shell - North Sea Data - August 2005\Shell - North Sea Data - August 2005\Output\NorthernEuropeLandED50_31NLi.DWG.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Other_data\Shell - North Sea Data - August 2005\Shell - North Sea Data - August 2005\Output\NorthernEuropeLandED50_32NLi.DWG.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Russia\amapoga_fields2.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Russia\fields3.jpg.aux.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\Russia\shtokman.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\25Round_Blocks_Applied\25Round_Blocks_Applied_For.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\25Round_Blocks_On_Offer\25Round_Blocks_On_Offer.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\Field_Determinations_Off\Field_Determinations_Off.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\Hydrocarbon_Fields_Off\Hydrocarbon_Fields_Offshore.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\Licensed_Blocks_Off\Licensed_Blocks_Off.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\pipeline\pipeline_eab.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\Relinquished_after_25rd\Relinquished_after25rd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\subsurface\subsurface.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\data\UK\surface\surface.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\All_fields_external_juli_2007.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\amapoga_fields2.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\discoveries_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\disc_expoutp3.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\facility_subsurface_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\facility_surface_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\fields_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\gas_network.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\Hydrocarbon_Fields_Offshore.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\LINE2.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\OSPAR_regions_polygons.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\OSPAR_shoreline.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\pipelines_dd.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\pipeline_eab.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\Platforms_external_december_2007.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\subsurface.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\surface.shp.xml',  # noqa
    r'C:\project\1005 OSPAR maps\maps\ospar_hydrocarbon_20090402\Shapefiles\Wells1970_2008.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Cities.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Flow_Monit.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Forest.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Pipelines.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Railway.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Roads.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Towns.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Villages.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N\Water_Abstraction.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N2\Adm1.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N2\Adm2.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\Data_N2\HydroChem_Monit.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\landcover\metadata.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Adm1_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Adm1_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Adm2_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Adm2_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\boundaries_line.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\box.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\box_hollow.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\box_hollow_coast.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Cities_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Cities_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Dniester_Catchments.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Flow_Monit_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Flow_Monit_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Forest_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Forest_MoldovaCopy.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Forest_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\HydroChem_Monit_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\HydroChem_Monit_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\HydroPower_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\international_boundaries.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Lakes_Dniester.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\landcover.dbf.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Landslides_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Line_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Pipelines_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Protec_Areas_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\RBD_Dniester.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Rivers_Dniester.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Roads_Molodova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Roads_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Sanitary_Monit_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\soil.lyr.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Soil.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Towns_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Towns_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Villages_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Villages_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Watersheds_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Water_Abstraction_Moldova.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Water_Abstraction_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\finaldb\GIS_Data\Water_Discharge_Ukraine.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\climate\metadata.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\dem\metadata.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\landcover\metadata.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\popdens\metadata.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\admin_area.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\admin_bound.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\boundingbox.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\demshade.tif.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\demtoposhade.png.aux.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\demtoposhade.png.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\dniesterbasin.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\imagery_geocover.tif.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\imagery_truemarble.tif.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\landcover.dbf.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\railroad.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\road.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\settlement_area.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\settlement_points.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\soil.lyr.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\Soil.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\water_area.shp.xml',  # noqa
    r'C:\project\1007 Dniester\data\topdown\database\water_line.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\admin_area.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\admin_bound.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\boundingbox.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\demshade.tif.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\demtoposhade.png.aux.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\demtoposhade.png.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\dniesterbasin.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\imagery_geocover.tif.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\imagery_truemarble.tif.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\landcover.dbf.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\railroad.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\road.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\settlement_area.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\settlement_points.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\soil.lyr.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\Soil.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\water_area.shp.xml',  # noqa
    r'C:\project\1007 Dniester\web\www\metadata\water_line.shp.xml',  # noqa
    r'C:\project\1009 AoA\graphics\aoa_map\ws\5_final map2.png.aux.xml',  # noqa
    r'C:\project\1009 AoA\graphics\aoa_map\ws\5_final map3.png.aux.xml',  # noqa
    r'C:\project\1009 AoA\graphics\aoa_map\ws\antconv2.shp.xml',  # noqa
    r'C:\project\1010 uarctic tnmap\data\allforallmap\campus4.dbf.xml',  # noqa
    r'C:\project\1010 uarctic tnmap\data\maincamp2.dbf.xml',  # noqa
    r'C:\project\1010 uarctic tnmap\data\topo1.tif.xml',  # noqa
    r'C:\project\1010 uarctic tnmap\membersmap_nov2009\ws\income\grp4kml.shp.xml',  # noqa
    r'C:\project\1010 uarctic tnmap\membersmap_nov2009\ws\members2.shp.xml',  # noqa
    r'C:\project\1010 uarctic tnmap\membersmap_nov2009\ws\members3.shp.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\00_overview\ws\dem3\metadata.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\00_overview\ws\cntry2.shp.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\00_overview\ws\riverline2.shp.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\00_overview\ws\riverline3.shp.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\00_overview\ws\riverpoly2.shp.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\00_overview\00_overview.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\01_waterbalance\ws\water2\metadata.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\01_waterbalance\ws\water3\metadata.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\01_waterbalance\ws\water5\metadata.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\01_waterbalance\ws\water6\metadata.xml',  # noqa
    r'C:\project\1011 siwi central asia\graphics\01_waterbalance\ws\water7.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\arcticchar\ws\Char\IntDV.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\arcticchar\arcticchar.xml',  # noqa
    r'C:\project\1012 ABA\graphics\asti_locations\ws\Arctic boundaries_digitised\HighArctic_digitised.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\asti_locations\ws\Arctic boundaries_digitised\LowArctic_digitised.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\asti_locations\ws\Arctic boundaries_digitised\SubArctic_digitised.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\asti_locations\asti_locations.xml',  # noqa
    r'C:\project\1012 ABA\graphics\asti_trends\asti_trends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\connections\worldconnections.xml',  # noqa
    r'C:\project\1012 ABA\graphics\eidermap\ws\eider2x.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\eidermap\eidercommon.xml',  # noqa
    r'C:\project\1012 ABA\graphics\extent\ws\SubArctic_digitised.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\extent\extent.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishchanges\fishproduction.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\ws\year01_3.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\ws\year01_4.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\ws\year10_3.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\ws\year10_4.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\ws\year20_3.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\ws\year20_4.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\ws\year30_3.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\ws\year30_4.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\fishdistribution\fishdistribution.xml',  # noqa
    r'C:\project\1012 ABA\graphics\geneticdiversity\geneticdiversity.xml',  # noqa
    r'C:\project\1012 ABA\graphics\greening\ws\box45\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\greening\ws\greening2\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\greening\ws\greening3x\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\greening\ws\greening4.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\greening\greening.xml',  # noqa
    r'C:\project\1012 ABA\graphics\greening_chart\greening_chart.xml',  # noqa
    r'C:\project\1012 ABA\graphics\harvest_alaska\harvest_alaska.xml',  # noqa
    r'C:\project\1012 ABA\graphics\harvest_inuit\ws\place2.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\harvest_inuit\ws\place3.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\harvest_inuit\ws\place3x.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\harvest_inuit\harvest_inuit.xml',  # noqa
    r'C:\project\1012 ABA\graphics\harvest_nwt\harvest_nwt.xml',  # noqa
    r'C:\project\1012 ABA\graphics\harvest_nwt\harvest_nwt_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\icecovertrends\icecovertrends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\icecovertrends\icecovertrends_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\indcatorsoverview\indicatorsoverview_ecosystems_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\indcatorsoverview\indicatorsoverview_species_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\current5\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\land3\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\scenario4\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\scenario5\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\current2.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\current3.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\land1.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\landx2.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\scenario2.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\ws\scenario3.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\invasivehydrilla\invasivehydrilla.xml',  # noqa
    r'C:\project\1012 ABA\graphics\lakes_oldcrowflats\lakes_oldcrowflats.xml',  # noqa
    r'C:\project\1012 ABA\graphics\linguistics_map\ws\language12\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\linguistics_map\linguistics_map.xml',  # noqa
    r'C:\project\1012 ABA\graphics\linguistics_map\linguistics_maplegend.xml',  # noqa
    r'C:\project\1012 ABA\graphics\linguistics_populationsize\linguistics_populationsize.xml',  # noqa
    r'C:\project\1012 ABA\graphics\linguistics_speakerschart\linguistics_speakerschart.xml',  # noqa
    r'C:\project\1012 ABA\graphics\linguistics_vitality\linguistics_vitality.xml',  # noqa
    r'C:\project\1012 ABA\graphics\murremap\murremap.xml',  # noqa
    r'C:\project\1012 ABA\graphics\murretrends\murretrends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\murre_chart\murrechart.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peatloss\peatloss.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_chart\peat_chart_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\peat4\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\peat5\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\peat6\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\peat7\metadata.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\clip1.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\extent1.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\peat8.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\russia1.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\ws\russia2.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\peat_map\peat_map.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\ws\brevia_figure_hires2.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\ws\floodplains2.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\ws\floodplains3.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\ws\fullfigure2x.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\ws\fullfigure3.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\ws\nonsurveyed2.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\ws\nonsurveyed3.png.aux.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\permafrost_a.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\permafrost_b_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\permafrost\permafrost_cd.xml',  # noqa
    r'C:\project\1012 ABA\graphics\phenology_zackenberg\phenology.xml',  # noqa
    r'C:\project\1012 ABA\graphics\polarbears\ws\IUCN_Polar_Bear_Subpopulation_Boundaries.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\polarbears\ws\polarbearpops1.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\polarbears\ws\polarbear_subpop2.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\polarbears\polarbear.xml',  # noqa
    r'C:\project\1012 ABA\graphics\protectedareas_map\ws\2010-04-20\Protected_Areas_April.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\protectedareas_map\ws\Hugo_protected_areas\hugo.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\protectedareas_map\ws\Sweden\sweden.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\protectedareas_map\ws\Arctic_PAs_January28.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\protectedareas_map\ws\NA_areas.shp.xml',  # noqa
    r'C:\project\1012 ABA\graphics\protectedareas_map\protectedareas_map.xml',  # noqa
    r'C:\project\1012 ABA\graphics\protectedareas_trends\protectedareas_trends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\rangifer_chart\rangifer_chart.xml',  # noqa
    r'C:\project\1012 ABA\graphics\rangifer_map\rangifer_map.xml',  # noqa
    r'C:\project\1012 ABA\graphics\redknot\redknotmigration.xml',  # noqa
    r'C:\project\1012 ABA\graphics\reindeerherding_norway\reindeerherding_norway.xml',  # noqa
    r'C:\project\1012 ABA\graphics\reindeerherding_siberia\reindeerherding_siberia.xml',  # noqa
    r'C:\project\1012 ABA\graphics\seaice_web\seaice_web.xml',  # noqa
    r'C:\project\1012 ABA\graphics\shipping\invasive_shipping.xml',  # noqa
    r'C:\project\1012 ABA\graphics\shorebirds_status\shorebirds_status.xml',  # noqa
    r'C:\project\1012 ABA\graphics\snowcovertrends\snowcovertrends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\speciesindex\speciesindex_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\stressors\stressors.xml',  # noqa
    r'C:\project\1012 ABA\graphics\topo\topo.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\arcticchar.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\asti_locations.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\asti_trends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\eidercommon.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\extent.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\fishdistribution.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\fishproduction.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\geneticdiversity.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\greening.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\greening_chart.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\harvest_alaska.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\harvest_inuit.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\harvest_nwt.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\harvest_nwt_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\icecovertrends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\icecovertrends_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\indicatorsoverview_ecosystems_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\indicatorsoverview_species_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\invasivehydrilla.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\invasive_shipping.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\lakes_oldcrowflats.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\linguistics_map.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\linguistics_maplegend.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\linguistics_populationsize.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\linguistics_speakerschart.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\linguistics_vitality.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\murrechart.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\murremap.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\murretrends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\peatloss.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\peat_chart_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\peat_map.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\permafrost_a.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\permafrost_b_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\permafrost_cd.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\phenology.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\polarbear.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\protectedareas_map.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\protectedareas_trends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\rangifer_chart.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\rangifer_map.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\redknotmigration.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\reindeerherding_norway.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\reindeerherding_siberia.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\seaice_web.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\shorebirds_status.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\snowcovertrends.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\speciesindex_ot.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\stressors.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\topo.xml',  # noqa
    r'C:\project\1012 ABA\graphics\_output\worldconnections.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\acidification\acid1994_6\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\acidification\acid2100_6\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\bleachingscenarios\hadfrq2030_3\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\bleachingscenarios\hadfrq2050_3\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\bleachingscenarios\pcmfrq2030_3\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\bleachingscenarios\pcmfrq2050_3\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\bleachingscenarios\reef4\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\depletionsites\deplete4.shp.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\globiocoast\scenario00y3\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\globiocoast\scenario50y3\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\npp\avg9806\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\temperaturecoralscenarios\hadavg2030_63\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\temperaturecoralscenarios\hadavg2050_63\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\temperaturecoralscenarios\pcm2030_63\metadata.xml',  # noqa
    r'C:\project\1013 GLOBIO mix\deadwater-gis\temperaturecoralscenarios\pcm2050_63\metadata.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\gotaalv\gotaalv.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\goteborg\ws\hittase_gbg2.png.aux.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\goteborg\goteborg.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\malmo\malmo.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\skane\ws\erosionsf”ruts„ttningar\Fyllning.shp.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\skane\ws\erosionsf”ruts„ttningar\Grovsand finsand.shp.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\skane\ws\erosionsf”ruts„ttningar\Silt.shp.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\skane\skane.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\_output\gotaalv.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\_output\goteborg.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\_output\malmo.xml',  # noqa
    r'C:\project\1015 Effekt\graphics\_output\skane.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\ag\ws\ag1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\ag\ws\ag2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\ag\ws\cropland2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\ag\ws\cropland21\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\ag\ws\cropland3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\ag\ws\pasture2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\ag\ws\pasture21\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\ag\ws\pasture3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\info\arc0020.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\plant4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\plant5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\plant6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\plant7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\plant8\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\wab_data\PLANTDIV010IMGC1.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\wab_data\ponet_rob.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\wab_data\VERT_DIV010IMGC1.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\wab_data\wab_data.mxd.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\plant8.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\ws\plant9.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_plant\biodiversity_plant.tif.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\info\arc0002.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\terrvert3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\terrvert4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\terrvert5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\terrvert6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\terrvert7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\terrvert8\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\setnu_ras.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\terrvert8.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biodiversity_terrvert\ws\terrvert9.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biome\ws\biome2.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\biome\biome2.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\bound\ws\bound1.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\bound\ws\country1.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\bound\ws\country2.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\bound\ws\new1.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\area1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\carbon1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\carbon2w\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\carbon3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\carbon4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\carbon5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\carbon6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\ch4_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\ch4_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\ch4_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\ch4_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\ch4_7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\co2_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\co2_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\co2_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\co2_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\emiss2005_1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\emiss2005_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\emiss2005_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\emiss2005_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\emiss2005_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\emiss2005_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\emiss2005_7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\ggtest1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hcfc-141b_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hcfc-141b_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hcfc-141b_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hcfc-141b_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hcfc-142b_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hcfc-142b_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hcfc-142b_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hcfc-142b_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-125_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-125_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-125_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-125_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-134a_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-134a_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-134a_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-134a_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-143a_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-143a_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-143a_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-143a_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-152a_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-152a_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-152a_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-152a_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-227ea_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-227ea_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-227ea_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-227ea_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-236fa_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-236fa_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-236fa_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-236fa_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-23_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-23_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-23_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-23_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-245fa_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-245fa_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-245fa_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-245fa_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-32_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-32_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-32_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-32_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-365mfc_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-365mfc_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-365mfc_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc-365mfc_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc4310mee_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc4310mee_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc4310mee_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\hfc4310mee_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\land2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\land3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\n2o_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\n2o_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\n2o_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\n2o_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\nwo_7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc-c4f8_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc-c4f8_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc-c4f8_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc-c4f8_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc2f6_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc2f6_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc2f6_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc2f6_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc3f8_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc3f8_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc3f8_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc3f8_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc4f10_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc4f10_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc4f10_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc4f10_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc5f12_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc5f12_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc5f12_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc5f12_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc6f14_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc6f14_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc6f14_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc6f14_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc7f16_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc7f16_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc7f16_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfcc7f16_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfccf4_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfccf4_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfccf4_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\pfccf4_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\sf6_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\sf6_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\sf6_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\sf6_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\sf6_7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\area1.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\co2_3.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\carbondioxide\ws\emiss2005_4.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2050_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2050_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2050_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2050_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2050_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2090_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2090_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2090_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2090_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2090_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precipbase1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precipbase2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precipbase3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precipbase4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precipbase5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precipd2050\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precipd2090\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2050_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2050_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2050_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2050_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2050_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2050_7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2090_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2090_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2090_4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2090_5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2090_6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\temp2090_7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2050_5.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate\ws\precip2050_6.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\precipitationchange2050.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\precipitationchange2090.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\precipitation_january.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\precipitation_july.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\precipitation_year.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\temperaturechange2050.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\temperaturechange2090.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\temperature_january.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\temperature_july.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\climate_old\ws\temperature_mean.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\coast\ws\caspian1.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\coast\ws\continent1.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\coast\ws\continent2.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\coast\ws\continent3xx.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\coast\ws\continent_low1.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\forest\ws\forest2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\globio\ws\dem\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\globio\ws\mercator\ws\dem\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\globio\ws\mercator\ws\scenario0y\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\globio\ws\mercator\ws\scenario50y\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\globio\ws\mercator\ws\scenario0y2.img.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\globio\ws\mercator\ws\scenario50y.img.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\globio\ws\scenario0y\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\globio\ws\scenario50y\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\hazards\ws\ag2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\hazards\ws\multihzrd1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\hazards\ws\multihzrd2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\hazards\ws\multihzrd3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\hazards\ws\test1.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\landcover\ws\GLC2000_LANDCOVER.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\landcover\ws\GLC2000_LANDCOVER2.tif.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\area1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\landnodata1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppland2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppland3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppland4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppland5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppland6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppland7\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppland8\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\npplandx1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppsea1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppsea2x\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppsea3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppsea4\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppsea5\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppsea6\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\npp_grid\npp_grid\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\landnodata2.png.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\nppland8.img.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\npp\ws\production.mxd.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popdens\ws\grump1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popdens\ws\grump3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popdens\ws\grump5x\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popdens\ws\info\arc0035.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popdens\ws\greenland.shp.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popdens\ws\sea2.png.aux.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\info\arc0011.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\info\arc0014.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd1700_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd1700_21\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd1700_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd1900_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd1900_21\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd1900_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd2000_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd2000_21\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\pophist\ws\popd2000_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\abschange2015\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\glds05ag\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\glds15ag\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\popd2005_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\popd2005_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\popd2015_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\popd2015_3\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\rel2015_1\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\popscenario\ws\rel2015_2\metadata.xml',  # noqa
    r'C:\project\1017 FN-Sambandet\graphics\topo\topo.tif.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world2x\metadata.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world4\metadata.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\country2.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\lakes2.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\seaice1.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\seaice2.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world.200409.3x21600x10800.jpg.aux.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world.200409.3x21600x10800.jpg.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world2.tif.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world5xx.png.aux.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world6.png.aux.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world6.png.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\ws\world7x.png.aux.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\00_cover4.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\00_cover\00_cover_ot.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\01_globalscheme\01_globalscheme.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\02_temperature\02_temperature.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country10.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country11.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country12x.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country2.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country3.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country4.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country5.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country6.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country7.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country8.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\country9.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\lake2.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\ws\nz1.shp.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\03_emissionscartogram\03_emissionscartogram.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\04_sectoremissions\04_sectoremissions.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\05_emissionsvswealth\05_emissionsvswealth.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\06_regionalimpacts\06_regionalimpacts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\07_europeimpacts\ws\country08_ln1.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\07_europeimpacts\07_europeimpacts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\08_centralasiaimpacts\ws\asia2.png.aux.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\08_centralasiaimpacts\ws\asia3.png.aux.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\08_centralasiaimpacts\ws\europe3.png.aux.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\08_centralasiaimpacts\ws\europe4.png.aux.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\08_centralasiaimpacts\08_centralasiaimpacts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\10_northamericaimpacts\10_northamericaimpacts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\11_mitigationcosts\11_mitigationcosts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\13_adaptationoptions\13_adaptationoptions.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\14_gdppopghg\14_gdppopghg.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\00_cover4.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\00_cover_ot.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\01_globalscheme.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\02_temperature.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\03_emissionscartogram.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\04_sectoremissions.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\05_emissionsvswealth.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\06_regionalimpacts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\07_europeimpacts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\08_centralasiaimpacts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\10_northamericaimpacts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\11_mitigationcosts.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\13_adaptationoptions.xml',  # noqa
    r'C:\project\1018 UNECE climate\graphics\_output\14_gdppopghg.xml',  # noqa
    r'C:\project\1019 CAFF Secretariat\graphics\asti_chart\astiterrestrial.xml',  # noqa
    r'C:\project\1019 CAFF Secretariat\graphics\asti_locations\ws\Arctic boundaries_digitised\HighArctic_digitised.shp.xml',  # noqa
    r'C:\project\1019 CAFF Secretariat\graphics\asti_locations\ws\Arctic boundaries_digitised\LowArctic_digitised.shp.xml',  # noqa
    r'C:\project\1019 CAFF Secretariat\graphics\asti_locations\ws\Arctic boundaries_digitised\SubArctic_digitised.shp.xml',  # noqa
    r'C:\project\1019 CAFF Secretariat\graphics\asti_locations\asti_locations.xml',  # noqa
    r'C:\project\1019 CAFF Secretariat\graphics\_output\astiterrestrial.xml',  # noqa
    r'C:\project\1019 CAFF Secretariat\graphics\_output\asti_locations.xml',  # noqa
    r'C:\project\1020 Zoi mix\graphics\mediterranean_emissions\bubbles_mediterranean.xml',  # noqa
    r'C:\project\1020 Zoi mix\graphics\_output\bubbles_mediterranean.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\about_membersmap\about_membersmap.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\about_timeline\about_timeline.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\mdg_impactchain\mdg_impactchain.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\purpose\purpose.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\regional_flows\regional_flows_ot.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\regional_trends\regional_trends.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\trends_amongcountries\trends_amongcountriesexport.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\trends_amongcountries\trends_amongcountriesimport.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\trends_reportingparties\trends_reportingparties.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\trends_wastemain\trends_wastemain.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\about_membersmap.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\about_timeline.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\mdg_impactchain.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\purpose.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\regional_flows_ot.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\regional_trends.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\trends_amongcountriesexport.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\trends_amongcountriesimport.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\trends_reportingparties.xml',  # noqa
    r'C:\project\1021 Bali posters\graphics\_output\trends_wastemain.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\defined\arctic_defined.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\finnmark\finnmark_roaddev_ot.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\languages\languagemap.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\protectedareas\ws\wdpa2009_1.shp.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\protectedareas\protectedareas_map.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\protectedareas\protectedareas_map_wh.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\reindeer_and_caribou\rangifer_map.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\topo\topo.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\_output\arctic_defined.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\_output\finnmark_roaddev_ot.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\_output\languagemap.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\_output\protectedareas_map.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\_output\protectedareas_map_wh.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\_output\rangifer_map.xml',  # noqa
    r'C:\project\1022 Arctic Conventions\graphics\_output\topo.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\allcampus\allcampus.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\allmembers\membersmap_all.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\background\fullview20.png.aux.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\ipy\membersmap_ipy.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test01.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test02.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test03.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test04.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test05.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test06.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test07.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test08.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test09.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test10.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test11.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test12.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\n2n\north2north2008_2009_test13.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\tn\themenetworks.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\allcampus.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\membersmap_all.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\membersmap_ipy.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test01.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test02.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test03.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test04.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test05.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test06.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test07.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test08.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test09.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test10.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test11.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\north2north2008_2009_test12.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\graphics\_output\themenetworks.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\boxit1\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem1\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem2\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\demland_ng6\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\demsea_ng6\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem_ng1\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem_ng2\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem_ng3\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem_ng4\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem_ng5\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\lc1\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\lc2\metadata.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem2.aux.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\dem_ng2.tif.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\lake3.png.aux.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\land2.png.aux.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\lc2.aux.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\ws\lc3.png.aux.xml',  # noqa
    r'C:\project\1023 UArctic Map Revision\uarctic.png.aux.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\ws\shedcountry5.shp.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\ws\sheds4.shp.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\countries.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\countries_hdi.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\majorwatersheds.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\majorwatersheds_countcountries.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\majorwatersheds_countries.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\majorwatersheds_hdiweighted.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\majorwatersheds_ismajority.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\basins\majorwatersheds_transboundary.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\_output\countries.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\_output\countries_hdi.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\_output\majorwatersheds.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\_output\majorwatersheds_countcountries.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\_output\majorwatersheds_countries.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\_output\majorwatersheds_hdiweighted.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\_output\majorwatersheds_ismajority.xml',  # noqa
    r'C:\project\1024 TWAP indicators\graphics\_output\majorwatersheds_transboundary.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\sthlm\ws\border1.shp.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\sthlm\ws\coast1.shp.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\sthlm\ws\kommunsthlm1.shp.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\sthlm\ws\valdistrikt.shp.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\sthlm\ws\water1.shp.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\sthlm\ws\water2.shp.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\sthlm\sthlmslan.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\sthlm\sthlmslan_sv.xml',  # noqa
    r'C:\project\1025 SEI small tasks\graphics\_output\sthlmslan.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\agriculture\agriculture.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\bluewater_crop\ws\blue_lpjml.shp.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\bluewater_crop\bluewater_cropland.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\ciesin_drought\ciesin_drought.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\climographs\agriculture.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\climographs\precipitation_afghanistan.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\climographs\precipitation_burkinafaso.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\climographs\precipitation_ethiopia.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\climographs\precipitation_morocco.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\climographs\precipitation_sudan.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\climographs\precipitation_yemen.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\climographs\precipitation_zimbabwe.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\dryyears\ws\dryyears1\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\dryyears\ws\info\arc0000.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\dryyears\dry400.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\dryyears\dry600.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\evapotranspiration\ws\a2_mean_annual_evapotranspiration_1950_2000.asc.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\evapotranspiration\ws\a2_mean_annual_evapotranspiration_1950_2000.shp.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\evapotranspiration\evapotranspiration.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\fractional_water\ws\greenblue_lpjml.shp.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\fractional_water\greenblue.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\greenwater_crop\ws\green_lpjml.shp.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\greenwater_crop\greencrop.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\groundwater\groundwater.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\groups\countrygroups.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\hdi\countries_hdi.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\popdens\popdens.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\precipitation_average\ws\cruts21_5\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\precipitation_average\ws\cruts_4\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\precipitation_average\ws\info\arc0006.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\precipitation_average\ws\cruts21_6.png.aux.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\precipitation_average\precipitation_current.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\ws\precip2050_5\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\ws\precip2090_5\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\ws\precurrent3\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\ws\precurrent4\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\ws\precurrent5\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\ws\pre1991_2000.dbf.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\precipitationvuln_2050.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\precipitationvuln_2090.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preciptation_now\precipitationvuln_current.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preview_droughtcv\ws\dr_cv\cvx100\metadata.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preview_droughtcv\ws\cvx100.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\preview_droughtcv\droughtcv.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\runoff\ws\a3_mean_annual_runoff_1950_2000.asc.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\runoff\ws\a3_mean_annual_runoff_1950_2000.shp.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\runoff\runoff.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\agriculture.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\bluewater_cropland.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\ciesin_drought.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\countries_hdi.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\countrygroups.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\droughtcv.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\dry400.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\dry600.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\evapotranspiration.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\greenblue.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\greencrop.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\groundwater.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\popdens.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitationvuln_2050.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitationvuln_2090.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitationvuln_current.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitation_afghanistan.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitation_burkinafaso.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitation_current.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitation_ethiopia.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitation_morocco.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitation_sudan.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitation_yemen.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\precipitation_zimbabwe.xml',  # noqa
    r'C:\project\1027 SIWI early warning\graphics\_output\runoff.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_jg2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_jg3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_jm2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_jm3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_pg2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_pg3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_pm2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_pm3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_sg2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_sg3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_sm2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_sm3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\dem2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\dem3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\demmask1\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\info\arc0057.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\nemawater1\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\nemawater5\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\nemawater5x\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\nemawater6\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\nemawater7\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\pa2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\pa3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\precip2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\reco_jtrph1\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\reco_palm1\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\reco_sugar1\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\soilprod2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\soilprod3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_jtrph2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_jtrph3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_jtrph4\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_maize2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_maize3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_maize4\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_palm2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_palm3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_palm4\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_sugar2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_sugar3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_sugar4\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\temp_max2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\temp_max3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\temp_min2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\temp_min3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\wetland2\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\wetland3\metadata.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_jg4.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_jm4.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_pg5.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_pm4.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_sg4.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\conflict_sm4.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\demask2.png.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\demlake2.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\demmask2.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\districtbound1.shp.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\nemawater3.shp.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\nemawater4.shp.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\nemawater7x.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\pa4.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\precip3.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\reco_jtrph2.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\reco_palm2.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\reco_sugar2.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\shade1.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\soilprod4.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_jtrph5.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_maize5.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_palm5.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\suit_sugar5.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\temp_max4.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\temp_min3.png.aux.xml',  # noqa
    r'C:\project\1028 Uganda Atlas\data\ws\wetland5.png.aux.xml',  # noqa
    r'C:\project\1030 The Globe\data\tcarta\kara_dbm\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\data\tcarta\shapefiles\kara_demo_contours.shp.xml',  # noqa
    r'C:\project\1030 The Globe\data\tcarta\shapefiles\kara_demo_sounding_points.shp.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\backdrop\ws\dem2\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\backdrop\ws\dem3\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\chlorophyll\ws\chloro2\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\chlorophyll\ws\chloro2.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\chlorophyll\ws\chloro3.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\crustalmagnetic\ws\crustmag2\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\crustalmagnetic\ws\crustmag2.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\crustalthickness\ws\crusthick2.asc.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\geoid\ws\ellipsoid2.asc.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\magneticfield\ws\info\arc0007.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\magneticfield\ws\magnetic3\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\magneticfield\ws\setnull_magn1\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\magneticfield\ws\magnetic3.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\magneticfield\ws\magnetic4.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\magneticfield\ws\SetNull_magn1.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\oceanfloorage\ws\age3\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\oceanfloorage\ws\land1\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\oxygen_dissolved\ws\oxygendiss1.asc.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\oxygen_utilization\ws\oxygenutil1.asc.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\seasurfacetemperature\ws\sst2\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\seasurfacetemperature\ws\sst2.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\seasurfacetemperature\ws\sst3.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\seasurfacetemperature\ws\sst3x.aux.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\sedimentthickness\ws\land1\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\sedimentthickness\ws\sedthick3x\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\worldbathymetry\ws\gshssf_3\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\worldbathymetry\ws\gshssf_3x\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\worldbathymetry\ws\ne3_5\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\graphics\worldbathymetry\ws\ne3_6\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\incoming\emag2\EMAG2_V2.tif.aux.xml',  # noqa
    r'C:\project\1030 The Globe\incoming\NOAA Pathfinder\annual_combined.hdf.aux.xml',  # noqa
    r'C:\project\1030 The Globe\incoming\tcarta\kara_dbm\metadata.xml',  # noqa
    r'C:\project\1030 The Globe\incoming\tcarta\shapefiles\kara_demo_contours.shp.xml',  # noqa
    r'C:\project\1030 The Globe\incoming\tcarta\shapefiles\kara_demo_sounding_points.shp.xml',  # noqa
    r'C:\project\1031 Taby\graphics\uni_city_taby_k3\uni_city_taby_k3.xml',  # noqa
    r'C:\project\1031 Taby\graphics\uni_nordics_sweden_k4\uni_nordics_sweden_k4.xml',  # noqa
    r'C:\project\1031 Taby\graphics\uni_region_malardalen_taby_k4\uni_region_malardalen_taby_k4.xml',  # noqa
    r'C:\project\1031 Taby\graphics\uni_region_malardalen_taby_k4\uni_region_malardalen_taby_k4_ot.xml',  # noqa
    r'C:\project\1031 Taby\graphics\uni_region_taby_catchment_k2\uni_region_taby_catchment_k2.xml',  # noqa
    r'C:\project\1031 Taby\graphics\_output\uni_city_taby_k3.xml',  # noqa
    r'C:\project\1031 Taby\graphics\_output\uni_nordics_sweden_k4.xml',  # noqa
    r'C:\project\1031 Taby\graphics\_output\uni_region_malardalen_taby_k4.xml',  # noqa
    r'C:\project\1031 Taby\graphics\_output\uni_region_malardalen_taby_k4_ot.xml',  # noqa
    r'C:\project\1031 Taby\graphics\_output\uni_region_taby_catchment_k2.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\biomes\ws\biome2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\biomes\ws\biome3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\biomes\ws\biome4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\biomes\ws\wwf_terr_ecos.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ci_hotspots\ws\hotspot2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ci_hotspots\ws\hotspot3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ci_hotspots\ws\hs_landmask1\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ci_hotspots\ws\hotspots_revisited_2004_polygons.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ci_hotspots\ws\test1.dbf.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\crisisecoregions\ws\crisis2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\crisisecoregions\ws\crisis3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\crisisecoregions\ws\crisis4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\crisisecoregions\ws\crisis2.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ecoregion_prot\ws\ecoprot2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ecoregion_prot\ws\ecoprot3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ecoregion_prot\ws\ecoprot4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ecoregion_prot\ws\ecoline1.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ecoregion_prot\ws\ecoprot1.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\ecoregion_prot\ws\ecoprot2.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\endemism\ws\endemism2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\endemism\ws\endemism3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\endemism\ws\endemism4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa1700_3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa1700_4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa1700_5\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa1700_6\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa2000_3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa2000_4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa2000_5\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa2000_6\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa2050_3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa2050_4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa2050_5\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_biodiversity\ws\msa2050_6\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu1700_3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu1700_4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu1700_5\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu1700_6\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2000_3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2000_4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2000_5\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2000_6\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2050_3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2050_4\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2050_5\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2050_6\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu1700_5.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu1700_6.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\globio3_landuse\ws\lu2000_5.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\lme\ws\lme2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\lme\ws\lme3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\lme\ws\lmes_64.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\info\arc0002.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\info\arc0005.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\info\arc0020.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\info\arc0023.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\neland1\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\neland2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\prot6\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpnt3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpntm3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpol2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpolm2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\neland1.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\neland2.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\prot4.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\prot5.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\prot6.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpnt2.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpnt3.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpntm3.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpol2.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protarea\ws\protpolm2.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\land3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lme2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lme3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lmemax5\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\land1.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\land3.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lme2.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lme3.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lme4.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lme5.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lmemax1.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lmemax2.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lmemax3.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lmemax4.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lmemax5.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\protection_lme\ws\lmes_64.shp.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\threatanimals\ws\ecothreatam1\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\threatanimals\ws\ecothreatam2\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\threatanimals\ws\ecothreatam3\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\threatanimals\ws\info\arc0002.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\threatanimals\ws\ecota1.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\threatanimals\ws\ecothreatam1.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\threatanimals\ws\ecothreatam2.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\graphics\threatanimals\ws\ecothreatam3.aux.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\incoming\globio3\geo4_msa_2000\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\incoming\globio3\geo4_msa_se50\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\incoming\globio3\gmlct_2000\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\incoming\globio3\gmlct_2050\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\incoming\globio3\hyde_lu_1700\metadata.xml',  # noqa
    r'C:\project\1035 Globalis biodiversity\incoming\globio3\hyde_msa_1700\metadata.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\fia_brochure\fia_brochure.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\fia_system\fia_system1a.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\logo\logo24.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\logo\logo24_bw.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\logo\logo24_small.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\logo\logo24_small_bw.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\logo\logo24_small_bw_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\logo\logo24_small_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictograms10.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictograms10a.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictograms10a_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictograms10_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictogram_blossom_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictogram_forwardlooking_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictogram_indicators_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictogram_megatrends_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictogram_scenarios_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\ws\pictogram_tools_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_blossom.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_blossom_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_blossom_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_forwardlooking.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_forwardlooking_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_forwardlooking_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_indicators.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_indicators_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_indicators_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_megatrends.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_megatrends_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_megatrends_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_scenarios.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_scenarios_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_scenarios_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_tools.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_tools_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\pictograms\pictogram_tools_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\platform\fia_platform1.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\powerpoint_template\ws\fia_presentation4.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\powerpoint_template\ws\fia_presentationFINAL 29Aug2010_ha.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\powerpoint_template\fia_presentationFINAL 29Aug2010_ha.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\powerpoint_template\flis_presentation5.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\system_neighbours\ws\system_neighbours1_ot.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\system_neighbours\system_neighbours1.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\system_neighbours\system_neighbours1a.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\fia_brochure.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\fia_platform1.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\fia_presentationFINAL 29Aug2010_ha.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\fia_system1a.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\flis_presentation5.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\logo24.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\logo24_bw.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\logo24_small.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\logo24_small_bw.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\logo24_small_bw_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\logo24_small_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_blossom.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_blossom_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_blossom_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_forwardlooking.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_forwardlooking_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_forwardlooking_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_indicators.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_indicators_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_indicators_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_megatrends.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_megatrends_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_megatrends_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_scenarios.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_scenarios_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_scenarios_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_tools.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_tools_alt.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\pictogram_tools_notext.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\system_neighbours1.xml',  # noqa
    r'C:\project\1036 FLISE\graphics\_output\system_neighbours1a.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\02_permafrostinterglacial\fig02_permafrostinterglacial_a.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\02_permafrostinterglacial\fig02_permafrostinterglacial_b.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\02_permafrostinterglacial\fig02_permafrostinterglacial_c.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\04_permafrost\ws\permaice2.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\04_permafrost\fig04_permafrost.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\05_subsea\ws\llipa.bil.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\05_subsea\ws\nhipa.bil.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\05_subsea\ws\nlipa.bil.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\05_subsea\ws\subsea2.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\05_subsea\ws\subsea3.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\05_subsea\ws\subsea4.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\05_subsea\fig05_subseaice.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\06_ipygroundtemp\ws\ipytemp1.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\06_ipygroundtemp\ws\Romanovsky fig2.tif.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\06_ipygroundtemp\fig06_ipygroundtemp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\08_calm\fig08_calmsites.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_a_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_a_5\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_b_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_b_5\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_c_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_c_5\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\NH\NH\GRD\ts20812100\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\NH\NH\GRD\ts2m19912010\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\NH\NH\GRD\ts2m20312050\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\NH\NH\GRD\ts20812100.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\NH\NH\GRD\ts2m19912010.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\NH\NH\GRD\ts2m20312050.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_a_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_a_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_a_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_b_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_b_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_b_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_c_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_c_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\ws\gipltime_c_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\fig10_groundtempscenarios.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\10_groundtempscenarios\fig10_groundtempscenarios_images.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2000_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2000_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2050_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2050_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2100_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2100_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\box1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\box2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\ASCII\alt2000.txt.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\ASCII\alt2100.txt.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\20m2000\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\20m2050\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\20m_2100\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\2m2000\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\2m2050\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\2m2100\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\5m2000\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\5m2050\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\5m2100\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\alt2000\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\alt2050\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\alt2100\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\20m2000.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\20m2050.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\20m_2100.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\2m2000.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\2m2050.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\2m2100.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\5m2000.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\5m2050.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\5m2100.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\alt2000.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\alt2050.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\incoming\GRID\alt2100.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\land2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2000_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2000_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2050_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2050_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m_2100_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m_2100_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2000_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2000_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2050_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2050_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2100_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2100_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2000_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2000_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2050_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2050_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2100_2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2100_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2000_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2000_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2000_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2000_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2000_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2000_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2050_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2050_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2050_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2050_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2050_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2050_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2100_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2100_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2100_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2100_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2100_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\alt2100_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\box1.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\box2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\land2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\modelOutline.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\modeloutline2.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2000_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2000_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2000_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2000_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2000_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2000_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2050_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2050_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2050_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2050_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2050_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m2050_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m_2100_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m_2100_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m_2100_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m_2100_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m_2100_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t20m_2100_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2000_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2000_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2000_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2000_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2000_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2000_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2050_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2050_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2050_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2050_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2050_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2050_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2100_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2100_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2100_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2100_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2100_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t2m2100_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2000_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2000_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2000_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2000_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2000_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2000_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2050_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2050_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2050_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2050_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2050_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2050_7.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2100_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2100_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2100_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2100_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2100_6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\t5m2100_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\ws\temp1.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\fig11_alaskaclimatescenarios.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\11_alaskaclimatescenarios\fig11_alaskaclimatescenarios_images.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2000_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2000_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2000_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2050_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2050_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2050_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2100_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2100_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\ws\alaska2100_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\fig12_alaskaaltscenarios.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\12_alaskaaltscenarios\fig12_alaskaaltscenarios_images.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\13_nordicpermafrost\fig13_nordicpermafrost.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\alt3049_1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\alt8099_1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\magt3049_1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\magt8099_1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\template1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\template2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\alt3049_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\alt8099_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\magt3049_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\magt8099_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\ws\template3.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\fig14_giplyamal.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\14_gipl_yamal\fig14_giplyamap_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\16_thermokarstlakes\fig16_thermokarstlakes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\17_stordalen_waterlogging\fig17_stordalen_waterlogging.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\17_stordalen_waterlogging\fig17_stordalen_waterlogging_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\27_coastal\ws\ACD_beta_version_october_2007.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\27_coastal\ws\ACD_polygons_Hugues_20sept2010.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\27_coastal\fig27_coastal.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\30_stordalenco2\fig30_stordalen_co2.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\30_stordalenco2\fig30_stordalen_co2_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\alaska2000_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\alaska2050_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\alaska2100_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2003_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2003_3.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2003_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2003_5.png.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2003_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2004_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2004_3.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2004_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2004_5.png.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_fco2_2004_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2003_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2003_3.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2003_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2003_5.png.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2003_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2004_2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2004_3.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2004_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2004_5.png.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\ws\flux_s_2004_6.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\fig31_eastsiberianfluxes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\31_eastsiberianfluxes\fig31_eastsiberianfluxes_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\32_dissolvedmethane_eastsiberia\ws\airseafluxes2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\32_dissolvedmethane_eastsiberia\ws\airseafluxes3.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\32_dissolvedmethane_eastsiberia\fig32_dissolvedmethane_eastsiberia.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\32_dissolvedmethane_eastsiberia\fig32_dissolvedmethane_eastsiberia_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_a1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_b1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_c1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_d1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt3outline.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_a1.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_a2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_b2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_c2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\ws\alt_d2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\fig38_eurasia_altprobs.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\38_probalisticalt\fig38_eurasia_altprobs_images.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\climate03_northernanomalies\ws\anomalies2.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\climate03_northernanomalies\ws\anomalies2b.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\co03_modeledcontaminants\co03_modeledcontaminants.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\co03_modeledcontaminants\co03_modeledcontaminants_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\ws\land2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\ws\tempanomaly4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\ws\worldbox2\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\ws\land2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\ws\TEMPANOMALY2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\ws\tempanomaly4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\ws\tempanomaly6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\ws\worldbox2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\globaltemperature2009_a.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\globaltemperature2009_a_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\globaltemperature2009\globaltemperature2009_b.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\ws\rail6\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\ws\road6\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\ws\rail6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\ws\rail7.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\ws\rail8.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\ws\road6.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\ws\road7.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\ws\road8.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd05_transportation\hd05_transportation.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd08_hydrocarbons\ws\cara_au.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\hd08_hydrocarbons\hd08_hydrocarbons.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp1200_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp250_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp1200_1.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp1200_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp1200_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp1200_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp250_1.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp250_2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp250_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\ws\temp250_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\intro01_anomalies.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro01_anomalies\intro01_anomalies_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\intro02_forcing\intro01_forcing.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l100 canada changes 2050\ws\autumn1.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l100 canada changes 2050\ws\autumn2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l100 canada changes 2050\ws\spring1.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l100 canada changes 2050\ws\spring2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l100 canada changes 2050\ws\spring3.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l100 canada changes 2050\l100_canada2050changes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\ws\breakup2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\ws\extentbox1.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\ws\extentbox2.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\ws\freezup2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\ws\icecover2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\l110_simulatedlakes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\l110_simulatedlakes_breakup_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\l110_simulatedlakes_freezup_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l110_simulatedlakes\l110_simulatedlakes_icecover_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l180_lakeprofiles\l180_lakeprofiles.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l180_lakeprofiles\l180_lakeprofile_a_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l180_lakeprofiles\l180_lakeprofile_b_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l180_lakeprofiles\l180_lakeprofile_c_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l180_lakeprofiles\l180_lakeprofile_d_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l180_lakeprofiles\l180_lakeprofile_e_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\l180_lakeprofiles\l180_lakeprofile_f_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cccma_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cccma_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ccsm3_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ccsm3_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cm20_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cm20_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cm21_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cm21_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cmpst_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cmpst_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cnrm_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cnrm_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020csiro_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020csiro_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020echam5_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020echam5_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020giss_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020giss_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020iap_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020iap_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020inmcm3_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020inmcm3_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ipsl_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ipsl_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020miroc3_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020miroc3_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020mri_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020mri_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020pcm1_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020pcm1_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ukmo_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ukmo_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CCCMA_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CCCMA_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CCCMA_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CCSM3_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CCSM3_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CCSM3_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CM20_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CM20_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CM20_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CM21_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CM21_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CM21_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cmpst_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cmpst_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020cmpst_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CNRM_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CNRM_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CNRM_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CSIRO_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CSIRO_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020CSIRO_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ECHAM5_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ECHAM5_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020ECHAM5_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020GISS_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020GISS_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020GISS_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020IAP_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020IAP_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020IAP_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020INMCM3_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020INMCM3_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020INMCM3_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020IPSL_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020IPSL_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020IPSL_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020MIROC3_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020MIROC3_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020MIROC3_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020MRI_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020MRI_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020MRI_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020PCM1_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020PCM1_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020PCM1_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020UKMO_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020UKMO_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\ws\m020UKMO_5.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\m020_januaryrms.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m020_januaryrms\m020_januaryrms_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\ws\mod040a_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\ws\mod040b_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\ws\mod040a_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\ws\mod040a_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\ws\mod040b_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\ws\mod040b_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\ws\swipa.figure.01.panelA.giss.change.1957-2006.asc.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\ws\swipa.figure.01.panelB.ipcc.annual.asc.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\m040_meantemp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m040 mean temperature\m040_meantemp_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050a_2e\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050a_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050a_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050b_2e\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050b_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050b_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050c_2e\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050c_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050c_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050d_2e\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050d_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050d_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050a_2e.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050a_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050a_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050a_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050b_2e.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050b_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050b_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050b_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050c_2e.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050c_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050c_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050c_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050d_2e.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050d_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050d_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\mod050d_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\ws\swipa.figure.02.panelA.cccma.tas.trend.1951-2000.dat.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\m050_winterpatterns.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m050 winter patterns 1951-2000\m050_winterpatterns_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod050a_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060a_2e\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060a_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060a_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060b_2e\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060b_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060b_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060c_2e\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060c_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060c_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060d_2e\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060d_2w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060d_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod050a_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060a_2e.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060a_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060a_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060a_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060b_2e.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060b_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060b_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060b_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060c_2e.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060c_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060c_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060c_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060d_2e.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060d_2w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060d_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\ws\mod060d_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\m060_projectedchanges.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m060 projected changes\m060_projectedchanges_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070a_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070a_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070b_3w\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070b_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\m020PCM1_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\m020UKMO_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070a_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070a_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070a_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070b_3w.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070b_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\ws\mod070b_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\m070_projectedprecipitation.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\m070 projected precipitation\m070_projectedprecipitation_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\observe03_ghcnstationssnow\observe03_snowstations.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\observe04_soiltempstations\ws\stations2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\observe04_soiltempstations\ws\temp2.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\observe04_soiltempstations\observe04_soiltempstations.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\observe04_soiltempstations\observe04_soiltempstations_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\observe05_lakeice\observe05_lakeice.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si020_seaice\ws\ice2004anom_4.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si020_seaice\ws\iceframe1.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si020_seaice\si020_seaice.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si020_seaice\si020_seaice_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si110_northpolesummerice\si110_northpolesummerice.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si110_northpolesummerice\si110_northpolesummericechart.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si220_solarheattrend\ws\shtrend1\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si220_solarheattrend\ws\shtrend1.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si220_solarheattrend\ws\shtrend2.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si220_solarheattrend\si220_solarheattrend.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si220_solarheattrend\si220_solarheattrend_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si260_allskysurfacetrends\ws\imageoutline1.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si260_allskysurfacetrends\ws\trend_1_autumn3.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si260_allskysurfacetrends\ws\trend_1_summer2.asc.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si260_allskysurfacetrends\ws\trend_2_autumn3.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si260_allskysurfacetrends\si260_allskysurfacetrends.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si260_allskysurfacetrends\si260_allskysurfacetrends_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2007_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2007_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2008_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2008_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2009_3\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2009_4\metadata.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2007_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2007_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2007_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2008_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2008_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2008_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2009_3.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2009_4.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\ice2009_5.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\ws\iceoutline1.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\si280_seaicedistro.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si280_seaicedistro\si280_seaicedistro_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si340_productivity\ws\owdays2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si340_productivity\ws\prod2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si340_productivity\si340_productivity.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si340_productivity\si340_productivity_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si390b_settlements\ws\glpv1_3.shp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si390b_settlements\si390b_settlements.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si390_indigenous\si390_linguistics.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si400_shippingroutes\ws\amsa_canada2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si400_shippingroutes\ws\amsa_russia2.png.aux.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si400_shippingroutes\si400_routes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si400_shippingroutes\si400_shippingroutes_c.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si400_shippingroutes\si400_shipproutes_a.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\si400_shippingroutes\si400_shipproutes_b.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\co03_modeledcontaminants.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\co03_modeledcontaminants_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig02_permafrostinterglacial_a.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig02_permafrostinterglacial_b.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig02_permafrostinterglacial_c.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig04_permafrost.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig05_subseaice.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig06_ipygroundtemp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig08_calmsites.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig10_groundtempscenarios.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig10_groundtempscenarios_images.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig11_alaskaclimatescenarios.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig11_alaskaclimatescenarios_images.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig12_alaskaaltscenarios.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig12_alaskaaltscenarios_images.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig13_nordicpermafrost.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig14_giplyamal.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig14_giplyamap_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig16_thermokarstlakes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig17_stordalen_waterlogging.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig17_stordalen_waterlogging_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig27_coastal.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig30_stordalen_co2.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig30_stordalen_co2_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig31_eastsiberianfluxes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig31_eastsiberianfluxes_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig32_dissolvedmethane_eastsiberia.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig32_dissolvedmethane_eastsiberia_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig38_eurasia_altprobs.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\fig38_eurasia_altprobs_images.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\globaltemperature2009_a.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\globaltemperature2009_a_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\globaltemperature2009_b.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\hd05_transportation.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\hd08_hydrocarbons.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\intro01_anomalies.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\intro01_anomalies_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\intro01_forcing.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l100_canada2050changes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l110_simulatedlakes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l110_simulatedlakes_breakup_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l110_simulatedlakes_freezup_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l110_simulatedlakes_icecover_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l180_lakeprofiles.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l180_lakeprofile_a_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l180_lakeprofile_b_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l180_lakeprofile_c_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l180_lakeprofile_d_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l180_lakeprofile_e_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\l180_lakeprofile_f_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m020_januaryrms.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m020_januaryrms_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m040_meantemp.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m040_meantemp_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m050_winterpatterns.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m050_winterpatterns_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m060_projectedchanges.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m060_projectedchanges_background.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m070_projectedprecipitation.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\m070_projectedprecipitation_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\observe03_snowstations.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\observe04_soiltempstations.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\observe04_soiltempstations_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\observe05_lakeice.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si020_seaice.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si020_seaice_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si110_northpolesummerice.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si110_northpolesummericechart.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si220_solarheattrend.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si220_solarheattrend_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si260_allskysurfacetrends.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si260_allskysurfacetrends_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si280_seaicedistro.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si280_seaicedistro_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si340_productivity.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si340_productivity_bg.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si390b_settlements.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si390_linguistics.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si400_routes.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si400_shippingroutes_c.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si400_shipproutes_a.xml',  # noqa
    r'C:\project\1037 AMAP SWIPA\graphics\_output\si400_shipproutes_b.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\Bawazagba\bawazagba.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\carbonfluxlanduse\carbonfluxlanduse.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\carbonfluxlanduse_total\carbonfluxlanduse_total.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\deforest2a\metadata.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\deforest4\metadata.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\deforest5\metadata.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\deforest2a.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\deforest4.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\deforest5.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\deforest6.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\htrop_change_20km.tif.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\ws\htrop_change_20km.tif.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforest\deforestation.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforestationcauses\deforestationcauses.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforestationrate\deforestationrate.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\deforestation_region\deforestation_region.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\ecosystemservices\forestecosystemservices.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestloss\forestloss.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\biome1\metadata.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\biome2\metadata.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\country3\metadata.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\bcountry4.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\biome1.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\biome2.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\country2.shp.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\country3.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\reforest2.tif.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\reforest3.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\reforest3c1.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\reforest3c2.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\reforest4.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\reforest5.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\ws\reforest6.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\biome-rainforest_for.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap\rainforest-changes_n†.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\forestmap2\forestmap2_embed.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\plantthreat\plantthreat.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\reddfunding\reddfunding.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\treespecies\treespecies.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\mask4.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\mask5.bmp.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\mask5.bmp.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\mask5.tif.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\mask5.tif.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\mask6.tif.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\mask7.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\maskCore.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\maskFade.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\rf1700_6.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\vk_regnskog\ws\rf2000_6.aux.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\bawazagba.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\biome-rainforest_for.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\carbonfluxlanduse.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\carbonfluxlanduse_total.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\deforestation.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\deforestationcauses.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\deforestationrate.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\deforestation_region.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\forestecosystemservices.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\forestloss.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\forestmap2_embed.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\plantthreat.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\rainforest-changes_n†.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\reddfunding.xml',  # noqa
    r'C:\project\1038 Globalis Rainforest\graphics\_output\treespecies.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\graphics\basemap\neman_pregola.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\graphics\_output\neman_pregola.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtm\srtm_40_02.asc.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtm\srtm_41_01.asc.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtm\srtm_41_02.asc.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtm\srtm_42_01.asc.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\dem1.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\dembox2.shp.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtmdem2.asc.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtmdem3.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtmdem4.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtmdem5.tif.aux.xml',  # noqa
    r'C:\project\1039 SIWI Kaliningrad\ws\srtmdem5.tif.xml',  # noqa
    r'C:\project\1040 Water book\brochure\www2012\graphics\flows\flows.xml',  # noqa
    r'C:\project\1040 Water book\docs\refs\1040 water book.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_01 population water shortage\1_01_populationwatertrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_02 great acceleration\1_02_a_greatacceleration.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_02 great acceleration\1_02_b_greatacceleration.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_03 water hockey sticks\ws\ariditiy\ai_yr\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_03 water hockey sticks\ws\crop\info\arc0002.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_03 water hockey sticks\ws\crop\crop.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_03 water hockey sticks\ws\crop\stats.dbf.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_03 water hockey sticks\ws\dams\GRanD_dams_v1_1.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_03 water hockey sticks\ws\dams\GRanD_reservoirs_v1_1.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_03 water hockey sticks\1_03_a_waterhockeysticks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_03 water hockey sticks\1_03_b_waterhockeysticks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_04 climate tipping points\1_04_climatetippingpoints.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_05 water tipping points overview\1_05_watertippingpointsoverview.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_06 temperaturehistory\1_06_temperaturehumanhistory.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_07 water scarcity quadrant\1_07_waterscarcityquadrant.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_07 water scarcity quadrant\1_07_waterscarcityquadrant_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_08 planetary boundary processes\1_08_planetaryboundaryprocesses.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\cloud_combined_2048.jpg.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\cloud_combined_2048.jpg.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\world.200409.3x5400x2700.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\world.200409.3x5400x2700.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\world2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\world2.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\world3.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\world3.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\ws\world4.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_09 planetary boundary status\1_09_planetaryboundarystatus.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_10 carbon sink\1_10_carbonsink.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_11 complex interactions\1_11_complexinteractions.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_12 resilience paradigm\1_12_resilience_paradigm.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_13 feedback flows\1_13_feedbackflows.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_14 conceptual framework\1_14_fullconceptualframework.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_15 water agenda_ot\1_15_wateragenda_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_b1_1 DEU\1_b1_1a DEU.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_b4_1_ot partitioning\1_b4_1_a_partitioning_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_b4_1_ot partitioning\1_b4_1_b_partitioning_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\1_b5_1_ot landscape resilience\1_b5_1_buildinglandscaperesilience_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_01 population trends\2_01_populationtrends_long.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_02 urban rural population\2_02_populationtrends_urbanrural.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_03 diet\ws\dietbubble.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_03 diet\2_03_dietarytrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_04 china water demand\2_04_chinawaterdemand.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_05 agricultural exports\2_05_agriculturalexports.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\ws\soy4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\ws\soy5\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\ws\soy6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\ws\soy2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\ws\soy4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\ws\soy5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\ws\soybean_harea2.ASC.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\ws\soybean_harea3.ASC.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_06 soy production\2_06_soyproduction.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_07 land acquisitions\2_07_landacquisitions.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_08 Major MEAs\2_08_majormeas.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1500_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1600_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1700_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1750_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1800_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1850_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1900_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1950_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag2000_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag2005_6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1850_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1900_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1930_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1950_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1960_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1970_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1980_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1990_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag2000_4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1850_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1900_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1930_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1950_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1960_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1970_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1980_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1990_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop2000_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1850_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1900_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1930_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1950_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1960_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1970_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1980_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1990_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras2000_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\mland2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1850_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1900_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1930_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1950_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1960_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1970_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1980_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag1990_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\ag2000_4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1850_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1850_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1900_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1900_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1930_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1930_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1950_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1950_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1960_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1960_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1970_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1970_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1980_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1980_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1990_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop1990_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop2000_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\crop2000_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1850_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1850_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1900_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1900_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1930_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1930_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1950_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1950_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1960_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1960_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1970_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1970_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1980_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1980_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1990_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras1990_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras2000_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\gras2000_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\aghist\mland2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1500_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1600_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1700_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1750_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1800_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1850_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1900_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1950_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop2000_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop2005_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1500_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1600_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1700_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1750_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1800_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1850_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1900_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1950_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras2000_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras2005_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\mland2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1500_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1500_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1500_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1600_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1600_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1600_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1700_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1700_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1700_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1750_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1750_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1750_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1800_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1800_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1800_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1850_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1850_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1850_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1900_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1900_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1900_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1950_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1950_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag1950_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag2000_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag2000_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag2000_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag2005_6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag2005_7.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\ag2005_7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1500AD.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1500_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1500_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1500_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1600_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1600_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1600_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1700_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1700_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1700_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1750_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1750_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1750_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1800_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1800_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1800_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1850_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1850_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1850_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1900_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1900_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1900_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1950_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1950_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop1950_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop2000_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop2000_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop2000_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop2005_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop2005_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\crop2005_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1500_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1500_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1500_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1600_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1600_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1600_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1700_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1700_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1700_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1750_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1750_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1750_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1800_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1800_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1800_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1850_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1850_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1850_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1900_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1900_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1900_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1950_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1950_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras1950_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras2000_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras2000_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras2000_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras2005_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras2005_3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\gras2005_5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\ws\mland2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\2_09_agriculturehistory.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_09 Agriculture history\2_09_agriculturehistory_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_10 carbon sinks\2_10a_forestareatrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_10 carbon sinks\2_10b_carbonstocks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_10 carbon sinks\2_10_carbonsinks_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_11 irrigation trends\2_11_irrigationtrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_12 HANPP\ws\test\thanpppall_pc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_12 HANPP\ws\hanppp2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_12 HANPP\ws\hanppp3.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\2_12 HANPP\2_12_hanppp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_01 regime shifts\3_01_regimeshifts.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_02 shiftscales\3_02_shiftscales.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\ws\6cb375aa273449b2b4353b9e265d5557\commondata\data0\adjust_hws\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\ws\6cb375aa273449b2b4353b9e265d5557\commondata\data0\Adjust_HWS.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\ws\6cb375aa273449b2b4353b9e265d5557\esriinfo\iteminfo.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\ws\6cb375aa273449b2b4353b9e265d5557\metadata\metadata1.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\ws\6cb375aa273449b2b4353b9e265d5557\metadata\metadata1_original.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\ws\hws3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\ws\hws4.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\3_03a_watertippingpoints_land.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\3_03b_watertippingpoints_water.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\3_03c_watertippingpoints_global.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\3_03c_watertippingpoints_global_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_03 water tipping points\3_03d_waterstress.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_04 cascading thresholds\3_04_cascadingthresholds.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_05 conceptual smallholder farming\3_05_conceptual_smallholder_farming.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_06 feedback loops\3_06_feedbackloops.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_b1_1 Goulburn Broken panarchy\3_b1_1_goulburnbroken_panarchy.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_b2_1 uganda attraction basin\3_b2_1a_ugandaattractionbasin.xml',  # noqa
    r'C:\project\1040 Water book\graphics\3_b3_1 andes attraction basin\3_b3_1a_andesattractionbasin.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_01_hydrocycle\4_01_hydrocycle2.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\gpptransp3\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\test1\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\vegctransp3\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\gpptransp3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\gpptransp4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\gpptransp5.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\ifthe_ras.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\ifthe_ras1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\test1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\test2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\transp3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\vegctransp3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\vegctransp4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\vegctransp5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\vegctransp6.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\ws\vegc_per_transp.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\4_02a_bloodstream_gpptransp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_02 bloodstream\4_02b_bloodstream_vegctransp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_03_greenbluefluxes\4_03_a_greenbluefluxes.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_03_greenbluefluxes\4_03_b_greenbluefluxes.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_04 Water cycling\4_04_watercycling.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_05 Greening Sahel\ws\a4.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_05 Greening Sahel\ws\box1.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_05 Greening Sahel\ws\Fig 2.img.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_05 Greening Sahel\ws\npp2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_05 Greening Sahel\ws\npp5.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_05 Greening Sahel\4_05_greeningafrica.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_06 evaporation difference\ws\mapdeltaet4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_06 evaporation difference\ws\int_ras.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_06 evaporation difference\ws\mapdeltaet3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_06 evaporation difference\ws\map_delta_et.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_06 evaporation difference\ws\map_delta_et2.ASC.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_06 evaporation difference\4_06_evaporationdifference.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_07 river discharge 2080\ws\discharge3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_07 river discharge 2080\ws\discharge4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_07 river discharge 2080\ws\median_change_discharge2.ASC.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_07 river discharge 2080\4_07_riverdischarge2080.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_08 sea level rise estuaries\ws\estvul2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_08 sea level rise estuaries\ws\hotspots1.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_08 sea level rise estuaries\4_08_sealevelrisevulnerableestuaries.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_09 extreme events\ws\4_09_extremeeventstrend.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_09 extreme events\4_09_extremeeventstrend.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_09 extreme events\4_09_extremeeventstrend_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_10 crops distance volume\4_10_crops_distance_volume.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_10 crops distance volume\4_10_crops_distance_volume_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_11 water imports\4_11_vwwaterimports.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_12 water trade\4_12_waterbluegreentrade.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_13 waterscarce population\4_13_populationscale.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_14 CPWF basins\4_14_basins.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_14 CPWF basins\4_15_basins.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_15 basin water\4_15a_basinwater.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_15 basin water\4_15b_basinwater.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_15 basin water\4_15c_basinwater.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_16a basin precipitation\4_16a_basinprecipitation.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_16b nile basin precpshed\ws\pshed7\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_16b nile basin precpshed\ws\pshed1.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_16b nile basin precpshed\ws\pshed7.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_16b nile basin precpshed\ws\pshed8.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_16b nile basin precpshed\ws\pshedfp.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_16b nile basin precpshed\4_16b_nileprecipitationshed.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_17 basin gdp\4_17a_basin_gdp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_17 basin gdp\4_17b_basin_ag_gdp_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_18 basin pop scenario\4_18a_basindrivers.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_18 basin pop scenario\4_18b_basinscenario.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_19 Stylized trends in basin poverty\4_19_stylizedbasintrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\old\a2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\old\b2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\old\c2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\old\fp1.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\a3.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\a3.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\a3.png_footprint.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\a4.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\b3.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\b3.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\b4.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\c3.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\c3.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\ws\c4.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\4_b2_indiaconversion_a.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\4_b2_indiaconversion_a_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\4_b2_indiaconversion_b.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\4_b2_indiaconversion_b_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\4_b2_indiaconversion_c.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b2 india conversion\4_b2_indiaconversion_c_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b3_1 rainstormcycle w mediterranean\4_b3_1_rainstormcycle_w_mediterranean.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\angle2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\compsn2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\compwe2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\epsc4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\epsc6\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\eps_c_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\eps_r_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\idgrid2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\info\arc0021.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambdarho4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambdarho_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rhoc4\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rho_c_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rho_r_2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\angle2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\angle_deg.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\arrow3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\arrow5.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\arrow6x.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\compSN2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\compWE2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\epsc3.ASC.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\epsc3.ASC.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\epsc4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\epsc5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\epsc6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\epsc7.png.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\eps_c.asc.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\eps_c_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\eps_r.asc.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\eps_r_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\Fa_SN_total_m2a.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\Fa_WE_total_m2a.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\footprint1.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\idgrid2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambdarho4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambdarho5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambdarho6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambdarho_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambda_rho.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambdrarho5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\lambdrarho5_footprint.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\outgrid.asc.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rhoc4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rhoc5.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rhoc6.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rho_c.asc.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rho_c_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rho_r.asc.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\ws\rho_r_2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\4_b4_1_moisturerecycling_a.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\4_b4_1_moisturerecycling_b.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b4_1 moisture recycling\4_b4_1_moisturerecycling_c.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b5_1 australiatrends\ws\stations1.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b5_1 australiatrends\ws\stations2.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b5_1 australiatrends\4_b5_1_australiatrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b5_2 perth streamflow\4_b5_2_perth_streamflow.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\box1\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\land1\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus_mm2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus_ratio2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\box1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\footprint1.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\land1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\land3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus3.ASC.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus_mm2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus_mm4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus_ratio2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus_ratio3.ASC.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\ws\nus_ratio4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\4_b6_1_groundwater_a.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\4_b6_1_groundwater_b.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b6_1 groundwater\4_b6_1_groundwater_c.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\irrigated2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\uslc2\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\chinalc1.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\chinalc4.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\irrigated1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\irrigated2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\uslc1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\uslc2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\uslc2x.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\uslc3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\ws\uslc4.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_b8 landuse north china + high plains\4_b8_landuseplains.xml',  # noqa
    r'C:\project\1040 Water book\graphics\4_ot sufficiencyratio\4_14_sufficencyratio_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_01 hunger + targets\5_01_hunger_targets.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_02_undernourishedmaps\5_02a_undernourished.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_02_undernourishedmaps\5_02b_populationincrease.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_03_diettrends\5_03_dietarytrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_04 undernourished vs diet\5_04_undernourishedvsdiet.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_05 diet projections\5_05_dietprojections.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_06 food wasteage\5_06_foodlosses.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_07 reducing food demand\5_07_waterdemand.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_08 water scenarios\5_08_waterscenarios.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_09 water 2050\5_09a_water2050.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_09 water 2050\5_09a_water2050_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_09 water 2050\5_09b_water2050.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_09 water 2050\5_09b_water2050_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_09 water 2050\5_09c_water2050.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_09 water 2050\5_09c_water2050_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\5_10 summer climate\5_10_summerclimate.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_01 poverty + climate\ws\Raster files\world_koppen\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_01 poverty + climate\ws\climzone3.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_01 poverty + climate\ws\hunger3.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_01 poverty + climate\ws\hunger5.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_01 poverty + climate\ws\ifthe_ras.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_01 poverty + climate\ws\ifthe_ras1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_01 poverty + climate\6_01a_savanna.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_01 poverty + climate\6_01b_poverty.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_02 savannah partitioning\6_02_savannahpartitioning.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_03 africa dry spells\6_03_africadryspells.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_04a yield gap ratios\ws\fig2_023.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_04a yield gap ratios\ws\yield2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_04a yield gap ratios\ws\yield4.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_04a yield gap ratios\ws\yield5.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_04a yield gap ratios\6_04a_yieldgap.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_04b yield gaps\6_04b_yieldgaps.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_05 water system classification\6_05_watersystemclassification.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_07 water productivity\6_07_waterproductivity.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_08 SWIs feedbacks Makanya\6_08_swis_feedbacks_makanya.xml',  # noqa
    r'C:\project\1040 Water book\graphics\6_ot yield experiments\6_07_yieldexperiments_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_01 SES and water\7_01a_SES_and_water.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_01 SES and water\7_01b_SES_and_water.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_02 SES water and feedbacks\7_02a_ses_water_feedbacks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_02 SES water and feedbacks\7_02b_ses_water_feedbacks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_03 processes scales\7_03_processes_scales.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_04_scales_impacts\7_04_scales_impacts.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_05 residence times\7_05_residencetime.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_06 analysis errors\7_06_analysiserrors.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_07 degraded_resilient_SES\7_07a_degraded_ses.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_07 degraded_resilient_SES\7_07b_resilient_ses.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_08 dam density vs volume\7_08_dam_density_vs_volume.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_09 hydro ESS\7_09_hydro_ess.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_10 states and dimensions\7_10_states_dimensions.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_11 cases rainfall regimes\ws\lwscar3.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_11 cases rainfall regimes\7_11_cases_risk.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_12 kothapally catchment\ws\files\files\sourcedem1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_12 kothapally catchment\ws\Kothapally files\02Musi sub-basin\major_reservoirs_in_musi.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_12 kothapally catchment\ws\Kothapally files\03kothapally\kothapally_village.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_12 kothapally catchment\ws\Kothapally files\03kothapally\meterological_stn.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_12 kothapally catchment\ws\Kothapally files\03kothapally\storagestructurs.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_12 kothapally catchment\ws\dem2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_12 kothapally catchment\7_12_kothapally.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_13 kothapally partitioning\7_13_kothapally_partitioning.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_14 ougadougou rainfall\7_14_ouadougourainfall.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\Nariale-LC-A\Nariale-LC-A.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\Nariale-LC-B\Nariale-LC-B.shp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\nariale1950_1\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\nariale2010_1\metadata.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\dem2.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\dem3.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\nariale1950_1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\nariale1950_2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\nariale2010_1.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\ws\nariale2010_2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\7_15a_nariarle_landuse.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_15 nariarle land use\7_15b_nariarle_landuse.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_16 Cerrado\ws\glc2000_2.png.aux.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_16 Cerrado\7_16_cerrado.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_17 brazil land use\7_17_brazillanduse.xml',  # noqa
    r'C:\project\1040 Water book\graphics\7_18 Rajasthan inflow\7_18_rajasthan_inflow.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_01 global interaction\8_01_globalinteraction.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_02 dimensions of ESS\8_02_dimensions_ess.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_03 floor management feedbacks\8_03_floodmgmt_feedbacks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_04 transformation phases\8_04_transformationphases.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_05 triple loop\8_05_tripleloop.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_b2_1 paradigm shift\8_b2_1_paradigmshift.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_b2_1 paradigm shift\8_b2_1_paradigmshift2_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_b2_1 paradigm shift\8_b2_1_paradigmshift3_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_b2_1 paradigm shift\8_b2_1_paradigmshift_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\8_b3_1 everglades mgmt history\8_b3_1_everglades_mgmt_history.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_01 resilience thinking\9_01_resiliencethinking.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_02 water cycle vulnerability\9_02_watercycle_vulnerability.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_03 tipping points revisited\9_03_tippingpoints2.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_03 tipping points revisited\9_03_tippingpoints2_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_04 society and biosphere\9_04_society_and_biosphere.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_05 conceptual framing resilience\9_05_conceptual_framing.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_05 conceptual framing resilience\9_05_conceptual_framing_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_05 conceptual framing resilience\9_05_conceptual_framing_ot2.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_06 water thinking\9_06_water_thinking_development.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_07 framework complex\9_07_frameworkcomplex.xml',  # noqa
    r'C:\project\1040 Water book\graphics\9_07 framework complex\9_07_frameworkcomplex_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_01_populationwatertrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_02_a_greatacceleration.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_02_b_greatacceleration.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_03_a_waterhockeysticks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_03_b_waterhockeysticks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_04_climatetippingpoints.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_05_watertippingpointsoverview.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_06_temperaturehumanhistory.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_07_waterscarcityquadrant.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_07_waterscarcityquadrant_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_08_planetaryboundaryprocesses.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_09_planetaryboundarystatus.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_10_carbonsink.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_11_complexinteractions.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_12_resilience_paradigm.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_13_feedbackflows.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_14_fullconceptualframework.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_15_wateragenda_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_b1_1a DEU.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_b4_1_a_partitioning_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_b4_1_b_partitioning_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\1_b5_1_buildinglandscaperesilience_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_01_populationtrends_long.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_02_populationtrends_urbanrural.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_03_dietarytrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_04_chinawaterdemand.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_05_agriculturalexports.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_06_soyproduction.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_07_landacquisitions.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_08_majormeas.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_09_agriculturehistory.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_09_agriculturehistory_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_10a_forestareatrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_10b_carbonstocks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_10_carbonsinks_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_11_irrigationtrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\2_12_hanppp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_01_regimeshifts.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_02_shiftscales.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_03a_watertippingpoints_land.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_03b_watertippingpoints_water.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_03c_watertippingpoints_global.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_03c_watertippingpoints_global_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_03d_waterstress.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_04_cascadingthresholds.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_05_conceptual_smallholder_farming.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_06_feedbackloops.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_b1_1_goulburnbroken_panarchy.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_b2_1a_ugandaattractionbasin.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\3_b3_1a_andesattractionbasin.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_01_hydrocycle2.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_02a_bloodstream_gpptransp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_02b_bloodstream_vegctransp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_03_a_greenbluefluxes.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_03_b_greenbluefluxes.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_04_watercycling.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_05_greeningafrica.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_06_evaporationdifference.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_07_riverdischarge2080.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_08_sealevelrisevulnerableestuaries.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_09_extremeeventstrend.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_09_extremeeventstrend_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_10_crops_distance_volume.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_10_crops_distance_volume_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_11_vwwaterimports.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_12_waterbluegreentrade.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_13_populationscale.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_14_basins.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_14_sufficencyratio_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_15a_basinwater.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_15b_basinwater.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_15c_basinwater.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_15_basins.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_16a_basinprecipitation.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_16b_nileprecipitationshed.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_17a_basin_gdp.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_17b_basin_ag_gdp_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_18a_basindrivers.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_18b_basinscenario.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_19_stylizedbasintrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b2_indiaconversion_a.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b2_indiaconversion_a_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b2_indiaconversion_b.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b2_indiaconversion_b_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b2_indiaconversion_c.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b2_indiaconversion_c_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b3_1_rainstormcycle_w_mediterranean.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b4_1_moisturerecycling_a.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b4_1_moisturerecycling_b.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b4_1_moisturerecycling_c.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b5_1_australiatrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b5_2_perth_streamflow.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b6_1_groundwater_a.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b6_1_groundwater_b.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b6_1_groundwater_c.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\4_b8_landuseplains.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_01_hunger_targets.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_02a_undernourished.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_02b_populationincrease.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_03_dietarytrends.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_04_undernourishedvsdiet.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_05_dietprojections.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_06_foodlosses.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_07_waterdemand.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_08_waterscenarios.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_09a_water2050.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_09a_water2050_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_09b_water2050.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_09b_water2050_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_09c_water2050.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_09c_water2050_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\5_10_summerclimate.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_01a_savanna.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_01b_poverty.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_02_savannahpartitioning.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_03_africadryspells.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_04a_yieldgap.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_04b_yieldgaps.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_05_watersystemclassification.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_07_waterproductivity.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_07_yieldexperiments_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\6_08_swis_feedbacks_makanya.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_01a_SES_and_water.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_01b_SES_and_water.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_02a_ses_water_feedbacks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_02b_ses_water_feedbacks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_03_processes_scales.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_04_scales_impacts.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_05_residencetime.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_06_analysiserrors.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_07a_degraded_ses.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_07b_resilient_ses.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_08_dam_density_vs_volume.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_09_hydro_ess.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_10_states_dimensions.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_11_cases_risk.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_12_kothapally.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_13_kothapally_partitioning.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_14_ouadougourainfall.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_15a_nariarle_landuse.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_15b_nariarle_landuse.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_16_cerrado.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_17_brazillanduse.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\7_18_rajasthan_inflow.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_01_globalinteraction.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_02_dimensions_ess.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_03_floodmgmt_feedbacks.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_04_transformationphases.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_05_tripleloop.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_b2_1_paradigmshift.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_b2_1_paradigmshift2_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_b2_1_paradigmshift3_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_b2_1_paradigmshift_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\8_b3_1_everglades_mgmt_history.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_01_resiliencethinking.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_02_watercycle_vulnerability.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_03_tippingpoints2.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_03_tippingpoints2_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_04_society_and_biosphere.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_05_conceptual_framing.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_05_conceptual_framing_ot.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_05_conceptual_framing_ot2.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_06_water_thinking_development.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_07_frameworkcomplex.xml',  # noqa
    r'C:\project\1040 Water book\graphics\_output\9_07_frameworkcomplex_ot.xml',  # noqa
    r'C:\project\1040 Water book\rollup\rollup_www2013.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\dem2\metadata.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\dem3\metadata.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\glacier1\metadata.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\info\arc0011.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\land1\metadata.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\dem2.aux.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\dem3.aux.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\dem4.aux.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\dem5.aux.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\glacier1.aux.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\glacier2.tif.aux.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\land1.aux.xml',  # noqa
    r'C:\project\1041 UArctic Map NG\graphics\uarcticmap\ws\land2.tif.aux.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\Africa.idb\c_1\r_1.img.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\createconsta2\metadata.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\land1\metadata.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\landcover2\metadata.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\basin2.shp.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\dem2.aux.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\dem3.aux.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\land1.aux.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\land2.png.aux.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\landcover2.aux.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\landcover3.png.aux.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\ws\landcover3.shp.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\00_overview\overview.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\01_southsudan\southsudan.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\_output\overview.xml',  # noqa
    r'C:\project\1043 SIWI Nile\graphics\_output\southsudan.xml',  # noqa
    r'C:\project\1044 UArctic map\graphics\hi_map\hi_students.xml',  # noqa
    r'C:\project\1044 UArctic map\graphics\_output\hi_students.xml',  # noqa
    r'C:\project\1044 UArctic map\incoming\institutions2_files\filelist.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\members_april2012\members_20120430_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\members_april2012\members_april2012_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\members_jan2012\members_jan2012_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\members_may2012\members_20120522_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\members_may2012\members_20120523.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\organization\organization_20120430.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\organization\organization_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\sizemap\sizemap.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\tn\ws\tnmembers5.shp.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\tn\thematicnetworkfeb2012_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\tn2\tn_all_20120430_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\tn2\tn_all_260312_alt_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\tn3\ws\networka2a_laea1.shp.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\tn3\ws\tnmembers5.dbf.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\tn3\tn_all_20120605.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_discussion\kml\land1\metadata.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_discussion\kml\land1.aux.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_discussion\kml\land2.png.aux.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_discussion\kml\SR_HR.tif.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\members_20120430_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\members_20120522_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\members_20120523.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\members_april2012_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\members_jan2012_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\organization_20120430.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\organization_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\sizemap.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\thematicnetworkfeb2012_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\tn_all_20120430_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\tn_all_20120605.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\graphics\_output\tn_all_260312_alt_ot.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\ws\network1.shp.xml',  # noqa
    r'C:\project\1044 UArctic map\maps 2012\ws\networka2a_laea1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\landsea\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\rail\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\road\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\sett_poly_n\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\sett_poly_p\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\util\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\util_now\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\util_plan\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\data\popdens.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\work\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\work\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\work\impactplain2.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\work\landcover1.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\work\scenario30y2.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\work\setnu_ras.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\ws\landcover3.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\ws\landsea1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\ws\power_plan1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\ws\power_plan2.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\ws\road2.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\foranalysis\ws\sett_poly_plan.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\land2.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\nussir2.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\powerline_future.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\powerline_future.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\water1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\finnmark\water2.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\clip\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\landsea\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\mine\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\mineral\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\rail\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\rail_now\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\rail_plan\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\road\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\road_now\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\road_plan\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\util\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\util_now\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\util_plan\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\data\popdens.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\work\landcover\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\analysis\work\landcover.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\tempws_scenario\landcover\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\landsea.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\rail_now.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\rail_plan.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\road_now.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\road_plan.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\sett_pnt.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\sett_poly.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\util_now.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\final\util_plan.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\landcover2\metadata.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\landcover3.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\landcover4.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\landcover5.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\pipe_new1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\pipe_plan1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\rail2.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\rail3.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\rail_new1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\rail_plan1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\rail_plan2.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\road_new1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\foranalysis\road_plan1.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\0605 pipe Kharasavey-Sabeta_1.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\0605 pipe Kharasavey-Sabeta_2.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\6.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\7.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\fromriccardo4.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\fromriccardo5.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\fromriccardo6.shp.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\Kharasavey2.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\Kharasavey3.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\Kruzenshternskoe2.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\most possile future dev-t (Gazprom) in Yamal.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\most possile future dev-t (Gazprom) in Yamal2.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\obb-bovanenkovo-map.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\obb-bovanenkovo-map2.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\pipe, winter road1.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\pipe, winter road2.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\pipe, winter road3.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\pipes outside the peninsula.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\pipes outside the peninsula2.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\sabeta2.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\sabeta3.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\spring2.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\Yamal District.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\Yamal District2.jpg.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\yamburg_planned1.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\data\yamal\yamburg_planned2.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\finnmark_2030\ws\scenario30y.png.aux.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\finnmark_2030\finnmark_2030.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\finnmark_2030\finnmark_2030_alt.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\finnmark_layout\finnmark_layout.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\finnmark_now\finnmark_2010.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\finnmark_now\finnmark_2010_alt.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\legend\legend.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\yamal_2030\yamal_2030.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\yamal_2030\yamal_2030_alt.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\yamal_layout\yamal_layout.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\yamal_now\yamal_2010.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\yamal_now\yamal_2010_alt.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\finnmark_2010.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\finnmark_2010_alt.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\finnmark_2030.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\finnmark_2030_alt.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\finnmark_layout.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\legend.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\yamal_2010.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\yamal_2010_alt.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\yamal_2030.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\yamal_2030_alt.xml',  # noqa
    r'C:\project\1045 GLOBIO Yamal Finnmark\graphics\_output\yamal_layout.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1970_01\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1970_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1970_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1975_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1975_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1980_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1980_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1985_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1985_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1990_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1990_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1995_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1995_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2000_01\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2000_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2000_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2005_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2005_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2010_01\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2010_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2010_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2015_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2015_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2020_01\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2020_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2020_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2025_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2025_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2030_01\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2030_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2030_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2035_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2035_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2040_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2040_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2045_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2045_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2050_01\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2050_03\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2050_06\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\temp\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1970_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1970_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1970_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1970_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1975_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1975_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1975_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1975_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1980_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1980_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1980_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1980_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1985_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1985_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1985_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1985_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1990_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1990_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1990_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1990_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1995_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1995_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1995_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa1995_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2000_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2000_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2000_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2000_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2005_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2005_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2005_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2005_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2010_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2010_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2010_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2010_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2015_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2015_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2015_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2015_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2020_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2020_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2020_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2020_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2025_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2025_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2025_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2025_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2030_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2030_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2030_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2030_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2035_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2035_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2035_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2035_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2040_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2040_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2040_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2040_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2045_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2045_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2045_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2045_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2050_01.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2050_02.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2050_04.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\msa2050_05.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\biodiversity\ws\temp.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1970_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1970_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1970_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1970_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1975_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1975_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1975_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1975_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1980_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1980_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1980_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1980_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1985_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1985_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1985_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1985_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1990_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1990_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1990_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1990_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1995_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1995_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1995_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city1995_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2000_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2000_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2000_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2000_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2005_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2005_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2005_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2005_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2009_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2009_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2009_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2009_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2009_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2010_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2010_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2010_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2010_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2015_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2015_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2015_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2015_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2020_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2020_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2020_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2020_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2025_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2025_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2025_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2025_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2030_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2030_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2030_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2030_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2035_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2035_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2035_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2035_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2040_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2040_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2040_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2040_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2045_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2045_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2045_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2045_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2050_10m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2050_10m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2050_5m_2.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\city2050_5m_3.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\wup2009_4.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\wup2009_5.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\city\ws\wup2009_5m_6.shp.xml',  # noqa
    r'C:\project\1046 Heureka Animation\data\gdp_grids_1990_2025_15mi_ascii\gdp25_15mi.txt.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\data\gdp_grids_1990_2025_15mi_ascii\gdp90_15mi.ascii.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\data\pop_grids_1990_2025_15mi_ascii\p2025i15.ascii.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1970_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1970_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1970_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1975_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1975_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1980_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1980_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1985_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1985_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990x_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990_4\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1995_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1995_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2000_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2000_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2005_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2005_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2010_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2010_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2015_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2015_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2020_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2020_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2025_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2025_4\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2025_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2030_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2030_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2035_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2035_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2040_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2040_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2045_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2045_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2050_08\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2050_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1970_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1970_1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1970_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1970_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1970_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1975_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1975_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1975_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1975_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1980_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1980_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1980_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1980_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1985_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1985_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1985_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1985_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990x_1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990_09.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1990_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1995_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1995_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1995_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp1995_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2000_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2000_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2000_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2000_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2005_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2005_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2005_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2005_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2010_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2010_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2010_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2010_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2015_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2015_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2015_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2015_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2020_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2020_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2020_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2020_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2025_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2025_09.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2025_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2025_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2025_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2030_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2030_09.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2030_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2030_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2030_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2035_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2035_09.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2035_11.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2035_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2035_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2035_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2040_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2040_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2040_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2040_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2045_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2045_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2045_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2045_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2050_08.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2050_09.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2050_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2050_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2050_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp2050_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdp90_15mi.asc.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc1970_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc1975_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc1980_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc1985_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc1990_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc1995_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2000_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2005_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2010_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2015_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2020_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2025_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2030_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2035_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2040_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2045_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\gdpc2050_7.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\gdp\ws\testx1.bil.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\land\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1970\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1970_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1970_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1975\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1975_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1975_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1980\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1980_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1980_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1985\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1985_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1985_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1990\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1990_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1990_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1995\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1995_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1995_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2000\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2000_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2000_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2005\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2005_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2005_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2010\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2010_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2010_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2015\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2015_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2015_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2020\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2020_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2020_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2025\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2025_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2025_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2030\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2030_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2035\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2035_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2040\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2040_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2050\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2050_1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\int_ras1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\land.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens%s_1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1970.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1970_2_1.ASC.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1970_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1970_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1970_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1975_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1975_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1975_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1980_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1980_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1980_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1985_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1985_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1985_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1990_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1990_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1990_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1995_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1995_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens1995_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2000.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2000_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2000_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2000_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2005_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2005_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2005_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2010_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2010_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2010_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2015_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2015_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2015_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2020_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2020_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2020_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2025_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2025_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2025_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2030.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2030_1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2030_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2030_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2030_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2035.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2035_1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2035_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2035_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2035_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2040.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2040_1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2040_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2040_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2040_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045_1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045_2.asc.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2045_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2050.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2050_1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2050_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2050_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2050_5.png.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\popdens2050_5.png.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\setnu_ras1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\final\test1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\lake1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\land1\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1970_2\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1970_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1980_2\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1980_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1990\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1995\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2000\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2005\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2010\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2015\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2025_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2025_2\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2025_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2025_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2050_2\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2050_3\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2050_7\metadata.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\divid_ras.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\divid_ras1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\int_ras.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\lake1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\land1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\land2.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\land2x.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1970_2.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1970_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1970_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1975.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1980_2.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1980_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1985.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens1990.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2000.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2005.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2020.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2025_1.asc.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2025_2.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2025_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2030.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2035.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2040.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2045.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdens2050.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2025_2.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2025_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2025_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2025_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2025_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2050_2.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2050_3.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2050_4.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2050_5.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\popdenx2050_6.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\test1.aux.xml',  # noqa
    r'C:\project\1046 Heureka Animation\population\ws\testf1.png.aux.xml',  # noqa
    r'C:\project\1047 Globalis UNESCO\data\sites4.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\county\county.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\county\county_sv.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\sthlm\ws\border1.shp.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\sthlm\ws\coast1.shp.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\sthlm\ws\kommunsthlm1.shp.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\sthlm\ws\valdistrikt.shp.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\sthlm\ws\water1.shp.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\sthlm\ws\water2.shp.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\sthlm\sthlmslan.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\sthlm\sthlmslan_sv.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\_output\county.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\_output\county_sv.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\_output\sthlmslan.xml',  # noqa
    r'C:\project\1048 SEI lanskarta\graphics\_output\sthlmslan_sv.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Alaska\ws\alaska2_ot.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Alaska\ws\alaska_ot.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Alaska\ws\paalaska1.shp.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Alaska\ws\paalaska2xx.shp.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Alaska\ws\paalaska3x.shp.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Alaska\alaska3.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Canada\canada1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Circumpolar\circumpolar1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Finland\finland1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Greenland\greenland1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Iceland\iceland1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Norway\norway1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Russia\russia1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\Sweden\sweden1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\alaska3.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\canada1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\circumpolar1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\finland1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\greenland1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\iceland1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\norway1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\russia1.xml',  # noqa
    r'C:\project\1050 CAFF Protected Areas\graphics\_output\sweden1.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco2ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco3ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco6\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco6ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demibcao4\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demibcao4ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demibcao5ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\ibcao2\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\ibcao3\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\ibcao3ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\info\arc0029.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\land2\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\land3ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\bathy1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\bathy1ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco2ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco3.TIF.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco3.TIF.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco3ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco4.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco4ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco4xps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco5.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco5ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco6.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco6ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco7.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco7ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demgebco7xps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demibcao4.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demibcao4ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\demibcao5ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\ibcao2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\ibcao3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\ibcao3ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\IBCAO_ver2_23_PS_ARC_2km.asc.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\land2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\land2ps.shp.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\land3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\land3ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\land4ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\shade2ps.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\shade3ps.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\shade5.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\detail\shade5ps.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\land2\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask1ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask4ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask5ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\bathy1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\bathy1ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\bathy2ps.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\bathyx1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\dem1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\dem1ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\land2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\land3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\land3ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask1ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask3ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask4ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask5ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask6ps.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\mask6ps.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\masktest.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\shade5.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\shade5ps.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\shade6.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\highdetail\shade6.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\box1\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\box2\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\box2ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\dem3\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\dem3ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\info\arc0028.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land2\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land3ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints2\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3ps\metadata.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\bathy1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\bathy1ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\box1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\box2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\box2ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\boxpoly1.shp.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\boxpoly2.shp.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\boxpoly2ps.shp.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\CleanTOPO2_2D.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\CleanTOPO2_2D.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\dem2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\dem3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\dem3ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\dem4ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\dem5ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\HYP_50M_SR.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\HYP_HR.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\HYP_HR.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land1.shp.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land1ps.shp.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land2ps.shp.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land3ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\land4ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\NE2_HR_LC.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\NE2_HR_LC2.png.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\NE2_HR_LC3.TIF.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\NE2_HR_LC3ps.png.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\NE2_HR_LC3ps.png.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\shade5.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\shade5.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\shade5ps.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\shade6.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\shade6.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints2c1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints2c2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints2c3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3c1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3c2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3c3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3ps.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3psc1.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3psc2.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints3psc3.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints4ps.tif.aux.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\panarctic\tints4ps.tif.xml',  # noqa
    r'C:\project\1051 Arctic ocean basemap\ws\arctic_basemap_3411.mxd.xml',  # noqa
    r'C:\project\1052 Skogsrapport\graphics\skog\forest2_ot.xml',  # noqa
    r'C:\project\1052 Skogsrapport\graphics\skog\forest_en_bw.xml',  # noqa
    r'C:\project\1052 Skogsrapport\graphics\skog\forest_sv_bw.xml',  # noqa
    r'C:\project\1052 Skogsrapport\graphics\skog\forest_sv_col.xml',  # noqa
    r'C:\project\1052 Skogsrapport\graphics\_output\forest2_ot.xml',  # noqa
    r'C:\project\1052 Skogsrapport\graphics\_output\forest_en_bw.xml',  # noqa
    r'C:\project\1052 Skogsrapport\graphics\_output\forest_sv_bw.xml',  # noqa
    r'C:\project\1052 Skogsrapport\graphics\_output\forest_sv_col.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\jrcforest1\metadata.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweden100_2\metadata.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweden_2\metadata.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest6\metadata.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\CM-FMAP_2006_4500035000.tif.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\CM-FMAP_2006_4500045000.tif.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\CM-FMAP_2006_4500055000.tif.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest1.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest35_2.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest35_3.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest35_4.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest45_2.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest45_3.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest45_4.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest55_2.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest55_3.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\forest55_4.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\g100_06.tif.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\jrcforest1.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweden1.shp.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweden100_2.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweden_2.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest1.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest10_7.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest10_8.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest10_8.png.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest2.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest3.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest4.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest5.aux.xml',  # noqa
    r'C:\project\1052 Skogsrapport\ws\sweforest6.aux.xml',  # noqa
    r'C:\project\1056 Arctic Marine Map\graphics\map\arcticmarinezones.xml',  # noqa
    r'C:\project\1056 Arctic Marine Map\graphics\_output\arcticmarinezones.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\clip\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\clip_geo\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\landcover\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\mine\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\rail\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\road\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\util\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\data\landcover.aux.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\landsea1\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\landsea3\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\mine1\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\mine2\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\mine3\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\mineral1\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\mineral2\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_growth\mineral3\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\tempws_scenario\landcover\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\work\landcover\metadata.xml',  # noqa
    r'C:\project\1058 Arctic Globio video\data\ws\work\landcover.aux.xml',  # noqa
    r'C:\project\1061 Malm” social\demo\ws\basemap.png.aux.xml',  # noqa
    r'C:\project\1061 Malm” social\demo\ws\basemap.png.xml',  # noqa
    r'C:\project\1061 Malm” social\demo\ws\basemap.tif.xml',  # noqa
    r'C:\project\1061 Malm” social\demo\ws\basemap2.tif.xml',  # noqa
    r'C:\project\1063 Dongsheng\graphics\dongsheng\dongsheng_ge.xml',  # noqa
    r'C:\project\1063 Dongsheng\graphics\dongsheng\dongsheng_ot.xml',  # noqa
    r'C:\project\1063 Dongsheng\graphics\_output\dongsheng_ge.xml',  # noqa
    r'C:\project\1063 Dongsheng\graphics\_output\dongsheng_ot.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climatea2_2\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climatea2_5\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climatea2_6\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climatea2_7x\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climatea2_2.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climatea2_3.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climatea2_5.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climatea2_6.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\ws\climate_fp1.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\climate\climate.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\ecoregions\ws\g200_marine2.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\ecoregions\ecoregions.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio00y1\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio00y3\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio50y1\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio50y3\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio00y1.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio00y3.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio50e4.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio50y1.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\ws\globio50y3.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\globio.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\globio\globio_scenario.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\indigenous\ws\lang19\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\indigenous\ws\lang17geo.png.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\indigenous\ws\lang17geo.png.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\indigenous\ws\lang19.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\indigenous\ws\lang20.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\indigenous\indigenouslanguages.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\infrastructure\ws\pipel_russia2.tif.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\infrastructure\ws\pipel_russia3_footprint.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\infrastructure\ws\railroad2.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\infrastructure\ws\roads2.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\infrastructure\infrastructure.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\ws\glc2000_3\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\ws\glc2000_4\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\ws\glcc2000_6\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\ws\glc2000_3.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\ws\glc2000_4.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\ws\glc2000_4x.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\ws\glc2000_5.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\ws\glcc2000_6.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\landcover.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\landcover\landcover_background.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\ws\change2099_8\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\ws\perma1999_8\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\ws\change2099_7.ASC.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\ws\change2099_8.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\ws\change2099_9.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\ws\perma1999_7.ASC.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\ws\perma1999_8.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\ws\perma1999_9.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\permafrost_change.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\permafrost\permafrost_temp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\protectedareas\protectedareas.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\reindeer husbandry + herds\ws\husbandry2.png.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\reindeer husbandry + herds\ws\husbandry_fp1.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\reindeer husbandry + herds\ws\MAMMTERR.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\reindeer husbandry + herds\ws\rangifer2.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\reindeer husbandry + herds\rangifer_map.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\box1\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\box3\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\cleantopo4\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\cleantopo5\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\land1\metadata.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\bathy08.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\bathy09.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\bathy10.tif.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\bathy10.tif.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\box3.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\CleanTopo4.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\cleantopo5.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\cleantopo6.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\cleantopo7.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\footprint1.shp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\land1.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\topo08.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\topo09.tif.aux.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\ws\topo09.tif.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\topography.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\topography\topography_background.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\climate.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\ecoregions.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\globio.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\globio_scenario.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\indigenouslanguages.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\infrastructure.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\landcover.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\landcover_background.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\permafrost_change.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\permafrost_temp.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\protectedareas.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\rangifer_map.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\topography.xml',  # noqa
    r'C:\project\1065 Reindeer UNFPII\graphics\_output\topography_background.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\as_bas_15s_beta.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\bgmap3.png.aux.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\bgmap3_footprint.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\dem2.tif.aux.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\dem2x_footprint.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\disctrict1.png.aux.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\disctrict1_footprint.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\mills1.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\mills2.png.aux.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\mills2_footprint.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\newmap2.png.aux.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\srtm_59_13_footprint.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\waterbodies2.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\data\waterlinear2.shp.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\graphics\palmoil\palmoil1.xml',  # noqa
    r'C:\project\1066 Rasmus April 2012\graphics\_output\palmoil1.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\graphics\ws\info\arc0002.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\graphics\ws\extent1.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\graphics\ws\extent2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\graphics\bg.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\0\0\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\1\0\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\1\0\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\1\1\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\1\1\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\0\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\0\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\0\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\1\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\1\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\1\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\2\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\2\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\2\2\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\0\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\0\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\0\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\0\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\0\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\1\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\1\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\1\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\1\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\1\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\2\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\2\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\2\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\2\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\2\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\3\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\3\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\3\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\3\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\3\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\4\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\4\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\4\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\4\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\3\4\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\0\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\1\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\2\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\3\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\4\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\5\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\6\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\7\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\8\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\4\9\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\0\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\1\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\10\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\11\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\12\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\13\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\14\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\15\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\16\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\2\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\3\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\4\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\5\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\6\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\7\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\8\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\0.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\1.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\10.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\11.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\12.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\13.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\14.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\15.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\16.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\2.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\3.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\4.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\5.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\6.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\7.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\8.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\5\9\9.png.aux.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\gml\line.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\gml\multipoint.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\gml\multipolygon.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\gml\owls.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\gml\point.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\gml\polygon.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\tasmania\sld-tasmania.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\tasmania\TasmaniaCities.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\tasmania\TasmaniaRoads.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\tasmania\TasmaniaStateBoundaries.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\tasmania\TasmaniaWaterBodies.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\xml\features.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\xml\georss-flickr.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\xml\track1.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\xml\wmsdescribelayer.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\georss.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\examples\yelp-georss.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\tests\Layer\atom-1.0.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\tests\Layer\mice.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\tests\Layer\owls.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\tests\speed\wmscaps.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\tests\atom-1.0.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\tests\mice.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\OpenLayers-2.11\tests\owls.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\proj4js\build\build.xml',  # noqa
    r'C:\project\1067 UArctic Interactive\web\current\tilemapresource.xml',  # noqa
    r'C:\project\1069 AMAP Web\documentdb\amap_workdocs\OGA-Graphical Production\GIS repository\Birds\Larus_fuscus_graellsii_wgs84.shp.xml',  # noqa
    r'C:\project\1069 AMAP Web\documentdb\amap_workdocs\OGA-Graphical Production\GIS repository\Birds\Larus_fuscus_heuglini_wgs84.shp.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_01 carbonates and ph in seawater\2_01_carbonates_and_ph_in_seawater.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_02 ph and alkalinity\2_02_ph_and_alkalinity.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_03 co2 solubility and cooling\2_03_CO2_solubility_and_cooling.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_05 arctic ocean profile\2_05_arctic_ocean_profile.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_06 CaCO3 surface arctic ocean\ws\fromodv2.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_06 CaCO3 surface arctic ocean\ws\fromodv3.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_06 CaCO3 surface arctic ocean\ws\fromodv_fp1.shp.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_06 CaCO3 surface arctic ocean\2_06_surface_carbonite.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_06 CaCO3 surface arctic ocean\2_06_surface_carbonite_samplingpoints.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_08 dilution aragonite\2_08_dilution_aragonite.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_10 sound absorptivity\2_10_sound_absorptivity_ot.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_12 recent ph\2_12_recent_ph.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_13 nordic aragonite\ws\nordic_ar_3.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_13 nordic aragonite\ws\nordic_ar_fp1.shp.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_13 nordic aragonite\2_13_nordic_aragonite.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_14 bering\ws\currents2.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_14 bering\2_14a_bering_currents.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_14 bering\2_14b_bering_currents.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\ws\land2\metadata.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\ws\bathy2.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\ws\bathy3.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\ws\bathy4.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\ws\bathy5.tif.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\ws\bathy_fp1.shp.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\ws\land2.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\ws\land3.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_15 aragonite siberian seas\2_15_siberianseas.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\ws\land2\metadata.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\ws\bathy2.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\ws\bathy3.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\ws\bathy4.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\ws\bathy5.tif.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\ws\bathy5.tif.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\ws\bathy_fp1.shp.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\ws\land2.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\2_16a_shelfmap.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\2_16b_beaufort_ph.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_16 beaufort shelf\2_16c_beaufort_omegaar.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_17 Canadian Archipelago aragonite\2_17_canadian_archipelago_sections.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_17 Canadian Archipelago aragonite\2_17_canadian_archipelago_sections_ot.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_18 alaska gakkel\2_18_beringia2005.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_19 global aragonite SRESA2\2_19_global_aragonite_scenario.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_20 ph reduction due to methane\2_20_ph_reduction_due_to_methane.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_21 Laptev sea scenarios\2_21_laptev_scenarios.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_21 new 1 simulated sept ph\2_21_ph_models.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_21 new 1 simulated sept ph\2_21_scenarios_ph_aragonite.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_21 new 2 multimodel aragonite\2_21_scenariocharts.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_24 Greenland sea ph\ws\ph5\metadata.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_24 Greenland sea ph\ws\ph4.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_24 Greenland sea ph\ws\ph5.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_24 Greenland sea ph\ws\ph6.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_24 Greenland sea ph\ws\ph6x.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_24 Greenland sea ph\ws\ph_fp1.shp.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_24 Greenland sea ph\2_24_nordic_ph.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_end4.asc.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_end5.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_end6.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_end7.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_end7b.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_fp1.shp.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_start5.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_start6.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_start7.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\ws\o_ar_start7b.png.aux.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\2_25 nordic omega scenario\2_25_nordic_ar_o_scenario.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_old\12 Nordic seas carbonbudget\2_12_nordic_seas_carbon.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_01_carbonates_and_ph_in_seawater.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_02_ph_and_alkalinity.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_03_CO2_solubility_and_cooling.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_05_arctic_ocean_profile.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_06_surface_carbonite.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_06_surface_carbonite_samplingpoints.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_08_dilution_aragonite.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_10_sound_absorptivity_ot.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_12_recent_ph.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_13_nordic_aragonite.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_14a_bering_currents.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_14b_bering_currents.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_15_siberianseas.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_16a_shelfmap.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_16b_beaufort_ph.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_16c_beaufort_omegaar.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_17_canadian_archipelago_sections.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_17_canadian_archipelago_sections_ot.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_18_beringia2005.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_19_global_aragonite_scenario.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_20_ph_reduction_due_to_methane.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_21_laptev_scenarios.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_21_ph_models.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_21_scenariocharts.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_21_scenarios_ph_aragonite.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_24_nordic_ph.xml',  # noqa
    r'C:\project\1070 AMAP AoA\graphics\_output\2_25_nordic_ar_o_scenario.xml',  # noqa
    r'C:\project\1071 Blueprint Files\ws\1m_dem\deme2.tif.aux.xml',  # noqa
    r'C:\project\1071 Blueprint Files\ws\1m_dem\demw2.tif.aux.xml',  # noqa
    r'C:\project\1071 Blueprint Files\ws\1m_dem\orthoe2.tif.aux.xml',  # noqa
    r'C:\project\1071 Blueprint Files\ws\1m_dem\orthoe2.tif.xml',  # noqa
    r'C:\project\1071 Blueprint Files\ws\1m_dem\orthow2.tif.aux.xml',  # noqa
    r'C:\project\1071 Blueprint Files\ws\1m_dem\orthow2.tif.xml',  # noqa
    r'C:\project\1072 Gibson maps\graphics\argentina\argentina.xml',  # noqa
    r'C:\project\1072 Gibson maps\graphics\lowerusa\lowerusa.xml',  # noqa
    r'C:\project\1072 Gibson maps\graphics\mexico\mexico.xml',  # noqa
    r'C:\project\1072 Gibson maps\graphics\mexico\mexico_ot.xml',  # noqa
    r'C:\project\1072 Gibson maps\graphics\_output\argentina.xml',  # noqa
    r'C:\project\1072 Gibson maps\graphics\_output\lowerusa.xml',  # noqa
    r'C:\project\1072 Gibson maps\graphics\_output\mexico.xml',  # noqa
    r'C:\project\1072 Gibson maps\graphics\_output\mexico_ot.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_AFG.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_AGO.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ALB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ARE.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ARG.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ARM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ATA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ATF.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_AUS.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_AUT.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_AZE.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BDI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BEL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BEN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BFA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BGD.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BGR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BHS.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BIH.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BLR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BLZ.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BOL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BRA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BRN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BTN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_BWA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CAF.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CAN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CHE.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CHL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CHN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CIV.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CMR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_COD.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_COG.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_COL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CRI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CUB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CYP.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_CZE.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_DEU.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_DJI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_DNK.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_DOM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_DZA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ECU.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_EGY.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ERI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ESP.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_EST.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ETH.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_FIN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_FJI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_FLK.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_FRA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GAB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GBR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GEO.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GHA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GIN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GMB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GNB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GNQ.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GRC.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GRL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GTM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_GUY.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_HND.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_HRV.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_HTI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_HUN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_IDN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_IND.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_IRL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_IRN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_IRQ.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ISL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ISR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ITA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_JAM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_JOR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_JPN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_KAZ.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_KEN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_KGZ.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_KHM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_KOR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_KWT.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LAO.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LBN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LBR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LBY.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LKA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LSO.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LTU.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LUX.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_LVA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MAR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MDA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MDG.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MEX.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MKD.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MLI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MMR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MNE.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MNG.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MOZ.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MRT.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MWI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_MYS.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NAM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NCL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NER.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NGA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NIC.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NLD.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NOR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NPL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_NZL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_OMN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PAK.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PAN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PER.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PHL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PNG.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_POL.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PRI.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PRK.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PRT.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PRY.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_PSE.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_QAT.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ROU.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_RUS.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_RWA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SAU.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SDN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SEN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SJM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SLB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SLE.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SLV.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SOM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SRB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SUR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SVK.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SVN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SWE.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SWZ.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_SYR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TCD.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TGO.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_THA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TJK.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TKM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TLS.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TTO.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TUN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TUR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TWN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_TZA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_UGA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_UKR.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_URY.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_USA.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_UZB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_VEN.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_VNM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_VUT.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_YEM.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ZAF.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ZMB.shp.xml',  # noqa
    r'C:\project\1073 Countrysplit\ws\ne110mcountry_ZWE.shp.xml',  # noqa
    r'C:\project\1075 HKH\graphics\cities\cities.xml',  # noqa
    r'C:\project\1075 HKH\graphics\cities\shadedrelief_bg.xml',  # noqa
    r'C:\project\1075 HKH\graphics\hdi\hdi.xml',  # noqa
    r'C:\project\1075 HKH\graphics\hdichart\hdichart.xml',  # noqa
    r'C:\project\1075 HKH\graphics\mpi\mpi.xml',  # noqa
    r'C:\project\1075 HKH\graphics\mpichart\mpichart.xml',  # noqa
    r'C:\project\1075 HKH\graphics\populationdensity\ws\GlobalRuralUrbanMappingProjectVersion1GRUMPv1PopulationDensityGrid.xml',  # noqa
    r'C:\project\1075 HKH\graphics\populationdensity\ws\gluds00ag.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\populationdensity\ws\gluds00g.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\populationdensity\ws\popdens2.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\populationdensity\ws\popdens3.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\populationdensity\ws\popdens4.png.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\populationdensity\populationdensity.xml',  # noqa
    r'C:\project\1075 HKH\graphics\populationdensity\populationdensity_bg.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\imr2\metadata.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\cleantopo2.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\cleantopo3.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\cleantopo4.tif.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\cleantopo4.tif.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\imr.asc.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\imr2.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\imr3.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\imr4.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\imr5.png.aux.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\imrfp1.shp.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\ws\topofp1.shp.xml',  # noqa
    r'C:\project\1075 HKH\graphics\poverty\poverty.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\cities.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\hdi.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\hdichart.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\mpi.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\mpichart.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\populationdensity.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\populationdensity_bg.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\poverty.xml',  # noqa
    r'C:\project\1075 HKH\graphics\_output\shadedrelief_bg.xml',  # noqa
    r'C:\project\1075 HKH\incoming\HKH\HKH_boundary.shp.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem3\metadata.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem4\metadata.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem4_alt\metadata.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem4_high\metadata.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem3.aux.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem4.aux.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem4_alt.aux.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem4_alt2.aux.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem4_high.aux.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem5.tif.aux.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem5_alt.tif.aux.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws\dem5_high.tif.aux.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws_kamoa\kamoa4\metadata.xml',  # noqa
    r'C:\project\1076 Blueprint 2\ws_kamoa\kamoa4.aux.xml',  # noqa
    r'C:\project\1077 Yngern\out\gnesta2_2.jpg.aux.xml',  # noqa
    r'C:\project\1077 Yngern\out\gnesta2_2.png.aux.xml',  # noqa
    r'C:\project\1077 Yngern\out\gnesta5_2.jpg.aux.xml',  # noqa
    r'C:\project\1077 Yngern\out\gnesta5_2.png.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta3\metadata.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta4\metadata.xml',  # noqa
    r'C:\project\1077 Yngern\ws\extract_1c1.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\extract_1c2.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\extract_1c3.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta1.tif.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta1.tif.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta2.tif.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta2.tif.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta3.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta3c1.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta3c2.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta3c3.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta4c1.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta4c2.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta4c3.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta5.tif.aux.xml',  # noqa
    r'C:\project\1077 Yngern\ws\gnesta5.tif.xml',  # noqa
    r'C:\project\1077 Yngern\ws\outside1.shp.xml',  # noqa
    r'C:\project\1077 Yngern\ws\outside2.shp.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\clip\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\clip_geo\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\landcover\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\mine\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\railr\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\roadr\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\util\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\landcover.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\railr.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\roadr.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\data\utillength.dbf.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\prep\power1\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\prep\road4w\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\landsea1\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\mine1\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\mine2\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\mine3\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\mineral1\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\mineral2\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_growth\mineral3\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\tempws_scenario\landcover\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\caff1\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\landcover\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenariom40y\metadata.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\caff1.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\landcover.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenario00y2.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenario00y3.dbf.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenario40y2.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenario40y3.dbf.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenariom40y2.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenariom40y3.dbf.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenarionull2.aux.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\data\ws\work\scenarionull3.dbf.xml',  # noqa
    r'C:\project\1080 GLOBIO Arctic 2012\graphics\arctic\globioarctic.xml',  # noqa
    r'C:\project\1081 UArctic thematic networks Oct 2012\graphics\tn\ws\networka2a_laea1.shp.xml',  # noqa
    r'C:\project\1085 GLOBIO powerlines\ws\util3.dbf.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\arrowmap\north2north_dec2012.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\circle\north2north_circular.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\circle\north2north_circular2.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\circle_institution\north2north_circularinst.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\countryarrows_canada.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\countryarrows_finland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\countryarrows_iceland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\countryarrows_norway.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\countryarrows_russia.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\countryarrows_sweden.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\countryarrows_usa.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\inout_countryarrows_canada.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\inout_countryarrows_finland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\inout_countryarrows_iceland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\inout_countryarrows_norway.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\inout_countryarrows_russia.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\inout_countryarrows_sweden.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\countryarrows\inout_countryarrows_usa.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\ws\countrydot1.shp.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\countryall.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\countryall_canada.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\countryall_finland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\countryall_iceland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\countryall_norway.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\countryall_russia.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\countryall_sweden.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\country_all\countryall_usa.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryall.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryall_canada.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryall_finland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryall_iceland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryall_norway.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryall_russia.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryall_sweden.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryall_usa.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryarrows_canada.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryarrows_finland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryarrows_iceland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryarrows_norway.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryarrows_russia.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryarrows_sweden.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\countryarrows_usa.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\inout_countryarrows_canada.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\inout_countryarrows_finland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\inout_countryarrows_iceland.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\inout_countryarrows_norway.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\inout_countryarrows_russia.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\inout_countryarrows_sweden.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\inout_countryarrows_usa.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\north2north_circular.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\north2north_circular2.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\north2north_circularinst.xml',  # noqa
    r'C:\project\1086 North2North 2012\graphics\_output\north2north_dec2012.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_00 topographic map\0_00_topographicmap.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\lake2\metadata.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\land2\metadata.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\dem1.png.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\lake2.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\lake3.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\lake4.png.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\land2.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\land3.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\land4.png.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe\marble1.png.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\newglobe2\marble1.png.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globe1.png.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\ws\globelaea1.png.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\0_01a cover.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\0_01 cover\0_01b cover.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\1_01 arctic resilience mentions\1_01_arctic_resilience_mentions.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\1_02 ARR process\1_02_arr_process.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\1_03 timeline\1_03_timeline.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\1_04 nested scales\1_04_nested_scales.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\2_01 Ball in basin\2_01a_ballinbasin.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\2_01 Ball in basin\2_01b_ballinbasin.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\2_02 complexity\2_02_complexity.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\2_03 Scales and processes\2_03_scalesandprocesses.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\2_04 ses scales\2_04_ses_scales.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\2_05 Adaptive cycle\2_05_adaptivecycle.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\2_06 DPSIR\2_06_dpsir.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\2_07 Ecosystem society links\2_07_ecosystem_society_links.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\3_01 indigenous peoples\3_01_indigenouslanguages.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_01 arctic cryosphere warming\4_01_arctic_cryosphere_warming.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_02 cascading effects\4_02_cascading_effects.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_06 greenland temp record\4_06_greenlandtemprecord.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_07 typology of threshold behaviours\4_07_typology_thresholds.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_08 social drivers of arctic change\4_08_socialdrivers.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_09 Biophysical drivers\4_09_biophysicaldrivers.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_10 arctic temp trends\4_10_arctictemptrends.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_11 arctic weatherpatterns\4_11a_arcticweatherpatterns.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_11 arctic weatherpatterns\4_11b_arcticweatherpatterns.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_12 energy balance\ws\flux_surface4\metadata.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_12 energy balance\ws\flux_surface4.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_12 energy balance\ws\netflux2.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_12 energy balance\ws\netflux4.asc.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_12 energy balance\ws\netflux4.asc.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_12 energy balance\ws\netflux5.png.aux.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_12 energy balance\4_12_energybalance.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_13 greenland albedo\4_13_greenland_albedo.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_14 Teshekpuk  lake\4_14_capehalkett.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\4_b4 Marine hystersis\4_b4_marine_hysteresis.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_01_coping range\5_01_copingrange.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_02 vulnerability framework\5_02_vulnerabilityframework.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_03 integration vulnerability resilience\5_03_integration_vulnerability_resilience.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_04 components adaptation resilience\5_04_components_adaptation_resilience.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_05 ecosystem wellbeing\5_05_ecosystem_wellbeing.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_06 alaska infrastructure\5_06a_alaska_infrastructure.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_06 alaska infrastructure\5_06b_alaska_infrastructure.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_07 Loop learning\5_07_loop_learning.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\5_08 transformation phases\5_08_transformationphases.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\7_01 refmap bering strait\7_01_refmap_beringstrait.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\7_02 northern sea route traffic\7_02_northernsearoute_traffic.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\7_03 adaptive capacity learning\7_03_adaptive_capacity_learning.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\8_01 refmap sw yukon\8_01_refmap_swyukon.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\9_01 refmap reindeer\9_01_refmap_reindeer.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\9_02 reindeer herding areas\9_02_reindeerherding.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\0_00_topographicmap.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\0_01a cover.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\0_01b cover.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\1_01_arctic_resilience_mentions.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\1_02_arr_process.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\1_03_timeline.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\1_04_nested_scales.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\2_01a_ballinbasin.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\2_01b_ballinbasin.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\2_02_complexity.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\2_03_scalesandprocesses.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\2_04_ses_scales.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\2_05_adaptivecycle.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\2_06_dpsir.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\2_07_ecosystem_society_links.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\3_01_indigenouslanguages.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_01_arctic_cryosphere_warming.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_02_cascading_effects.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_06_greenlandtemprecord.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_07_typology_thresholds.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_08_socialdrivers.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_09_biophysicaldrivers.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_10_arctictemptrends.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_11a_arcticweatherpatterns.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_11b_arcticweatherpatterns.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_12_energybalance.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_13_greenland_albedo.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_14_capehalkett.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\4_b4_marine_hysteresis.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_01_copingrange.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_02_vulnerabilityframework.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_03_integration_vulnerability_resilience.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_04_components_adaptation_resilience.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_05_ecosystem_wellbeing.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_06a_alaska_infrastructure.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_06b_alaska_infrastructure.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_07_loop_learning.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\5_08_transformationphases.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\7_01_refmap_beringstrait.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\7_02_northernsearoute_traffic.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\7_03_adaptive_capacity_learning.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\8_01_refmap_swyukon.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\9_01_refmap_reindeer.xml',  # noqa
    r'C:\project\1089 Arctic Resilience Report\graphics\_output\9_02_reindeerherding.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\clip\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\clip_geo\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\mine\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\mineral\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\rail\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\road\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\data\util\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\prep\power5\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\prep\rail5\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\prep\road5\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\prep\sett_pnt5\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\prep\sett_poly5\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\landsea1\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\mine1\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\mine2\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\mine3\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\mineral1\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\mineral2\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_growth\mineral3\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\tempws_scenario\landcover\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\ws\work\landcover\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\data\stats_00y.dbf.xml',  # noqa
    r'C:\project\1090 Ivory\data\stats_50y.dbf.xml',  # noqa
    r'C:\project\1090 Ivory\docs\globio map\globio_elephant.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\ws\impact00_1\metadata.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\ws\impact00y.png.aux.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\ws\impact00_1.aux.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\ws\impact00_2.png.aux.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\ws\impact50.png.aux.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\ws\impact50_1.aux.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\ws\impact50_2.png.aux.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\ws\range4.shp.xml',  # noqa
    r'C:\project\1090 Ivory\graphics\globio_elephant.xml',  # noqa
    r'C:\project\1091 Vattenkraft\graphics\hydromap\hydromap.xml',  # noqa
    r'C:\project\1091 Vattenkraft\graphics\_output\hydromap.xml',  # noqa
    r'C:\project\1094 Arctic places\graphics\placemap\placesmap.xml',  # noqa
    r'C:\project\1094 Arctic places\graphics\placemap\placesmap2.xml',  # noqa
    r'C:\project\1094 Arctic places\graphics\_output\placesmap.xml',  # noqa
    r'C:\project\1094 Arctic places\graphics\_output\placesmap2.xml',  # noqa
    r'C:\project\1095 OSDS Support\db\CLEANTOPO2_DEM.tif.aux.xml',  # noqa
    r'C:\project\1095 OSDS Support\db\ETOPO5_DEMINT.tif.aux.xml',  # noqa
    r'C:\project\1095 OSDS Support\db\ETOPO5_WATERSHADE.tif.aux.xml',  # noqa
    r'C:\project\1097 n2n May 2013\graphics\circle_country\north2north_circular.xml',  # noqa
    r'C:\project\1097 n2n May 2013\graphics\circle_institution\north2north_circularinst.xml',  # noqa
    r'C:\project\1097 n2n May 2013\graphics\members_may2013\members_may2013.xml',  # noqa
    r'C:\project\1097 n2n May 2013\graphics\n2n\north2north_june2013.xml',  # noqa
    r'C:\project\1097 n2n May 2013\graphics\_output\members_may2013.xml',  # noqa
    r'C:\project\1097 n2n May 2013\graphics\_output\north2north_circular.xml',  # noqa
    r'C:\project\1097 n2n May 2013\graphics\_output\north2north_circularinst.xml',  # noqa
    r'C:\project\1097 n2n May 2013\graphics\_output\north2north_june2013.xml',  # noqa
    r'C:\project\1104 Oskar exkursion\graphics\map\exkursionskarta1.xml',  # noqa
    r'C:\project\1104 Oskar exkursion\graphics\_output\exkursionskarta1.xml',  # noqa
    r'C:\project\1105 Jennie Diagram\graphics\diagram\diagram2.xml',  # noqa
    r'C:\project\1105 Jennie Diagram\graphics\diagram\diagram_ot.xml',  # noqa
    r'C:\project\1105 Jennie Diagram\graphics\_output\diagram2.xml',  # noqa
    r'C:\project\1105 Jennie Diagram\graphics\_output\diagram_ot.xml',  # noqa
    r'C:\project\1107 Palawan\data\Palawan\Palawan.shp.xml',  # noqa
    r'C:\project\1107 Palawan\graphics\map1\ws\dem2.tif.aux.xml',  # noqa
    r'C:\project\1107 Palawan\graphics\map1\ws\muni1.shp.xml',  # noqa
    r'C:\project\1107 Palawan\graphics\map1\ws\srtm_60_10.tif.aux.xml',  # noqa
    r'C:\project\1107 Palawan\graphics\map1\ws\srtm_60_11.tif.aux.xml',  # noqa
    r'C:\project\1107 Palawan\graphics\map1\ws\srtm_61_10.tif.aux.xml',  # noqa
    r'C:\project\1107 Palawan\graphics\map1\map1.xml',  # noqa
    r'C:\project\1107 Palawan\graphics\_output\map1.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\asylumfrom\asylumfrom_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\asylumfrom\asylumfrom_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\asylumfrom\asylumto_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\asylumfrom\asylumto_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\basemap\basemap_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\basemap\basemap_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\basemap\labels_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre4\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre6\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre7\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp4\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp6\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp7\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre2.dbf.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre6.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre7.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\pre7x.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\temp3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp2.dbf.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp6.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp7.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\ws\tmp8.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\precip_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\precip_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\temp_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\climate\temp_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\cyclone3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\drought3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\flood3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\quake3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\slide3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\volcano3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\cyclone3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\cyclone4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\cyclone41.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\cyclone5.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\drought3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\drought4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\drought41.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\drought5.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\flood3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\flood4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\flood41.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\flood5.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\quake3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\quake4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\quake41.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\quake5.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\slide3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\slide4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\slide41.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\slide5.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\volcano3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\volcano4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\volcano41.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\ws\volcano5.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\cyclone_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\cyclone_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\drought_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\drought_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\flood_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\flood_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\quake_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\quake_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\slide_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\slide_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\volcano_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hazard\volcano_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hdi\hdi_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\hdi\hdi_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\lampedusa\lampedusa.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover4\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover5\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover6\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\box2.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover3.tif.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover5.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover6.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover6x.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover7.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\globcover8.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\ws\test.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\landcover_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landcover\landcover_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landgrabs\landgrabs_investor_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landgrabs\landgrabs_investor_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landgrabs\landgrabs_investor_symbols_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landgrabs\landgrabs_investor_symbols_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landgrabs\landgrabs_target_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landgrabs\landgrabs_target_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landgrabs\landgrabs_target_symbols_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\landgrabs\landgrabs_target_symbols_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\mekong\mekong.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\nightlights\nightlights_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\nightlights\nightlights_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\nilen\nilen.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popchange\popchange_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popchange\popchange_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popdens\ws\popdens3\metadata.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popdens\ws\popdens3.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popdens\ws\popdens4.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popdens\ws\popdens5.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popdens\ws\popdens6.png.aux.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popdens\popdens_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\popdens\popdens_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\asylumfrom_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\asylumfrom_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\asylumto_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\asylumto_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\basemap_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\basemap_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\cyclone_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\cyclone_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\drought_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\drought_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\flood_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\flood_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\hdi_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\hdi_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\labels_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\lampedusa.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landcover_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landcover_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landgrabs_investor_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landgrabs_investor_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landgrabs_investor_symbols_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landgrabs_investor_symbols_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landgrabs_target_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landgrabs_target_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landgrabs_target_symbols_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\landgrabs_target_symbols_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\mekong.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\nightlights_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\nightlights_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\nilen.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\popchange_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\popchange_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\popdens_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\popdens_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\precip_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\precip_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\quake_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\quake_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\slide_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\slide_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\temp_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\temp_low.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\volcano_high.xml',  # noqa
    r'C:\project\1113 NE kart\graphics\_output\volcano_low.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\barentsgit\capabilities_1_0_0.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\barentsgit\capabilities_1_1_0.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\barentsgit\capabilities_1_1_1.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\globalis\capabilities_1_0_0.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\globalis\capabilities_1_1_0.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\globalis\capabilities_1_1_1.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\uarcticatlas2\capabilities_1_0_0.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\uarcticatlas2\capabilities_1_1_0.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\uarcticatlas2\capabilities_1_1_1.xml',  # noqa
    r'C:\project\1114 GA maps migration\incoming\axl\wms_capabilities\wms\localhost-5300\uarcticatlas_geo\capabilities_1_1_1.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\carbon1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\carbon3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\carbon4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\datasets\datasets\c_10m\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\datasets\datasets\c_1km\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\datasets\datasets\c_5m\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\datasets\datasets\c_1km.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\carbon1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\carbon2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\carbon3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\ws\carbon4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\carbon\test2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\area1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\ch_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\ch_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\co_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\co_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis2010_10\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis2010_12\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-12_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-12_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-134_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-134_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-143_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-143_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-152_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-152_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-227e_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-227e_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-236f_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-236f_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-245f_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-245f_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-2_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-2_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-365mf_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-365mf_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-3_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-3_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc4310me_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc4310me_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\n2_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\n2_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\nf_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\nf_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc2f_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc2f_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc3f_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc3f_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc4f1_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc4f1_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc5f1_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc5f1_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc6f1_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc6f1_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccc4f_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccc4f_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccf_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccf_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\sf_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\sf_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\area1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\ch4_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\ch4_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\ch_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\ch_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\co24.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\co2_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\co2_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\co_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\co_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis2010_10.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis2010_11.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis2010_12.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis2010_7.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis2010_8.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis2010_9.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\emis_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-125_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-125_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-12_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-12_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-134a_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-134a_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-134_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-134_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-143a_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-143a_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-143_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-143_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-152a_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-152a_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-152_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-152_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-227ea_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-227ea_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-227e_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-227e_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-236fa_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-236fa_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-236f_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-236f_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-23_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-23_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-245fa_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-245fa_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-245f_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-245f_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-2_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-2_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-32_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-32_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-365mfc_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC-365mfc_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-365mf_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-365mf_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-3_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc-3_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC4310mee_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\HFC4310mee_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc4310me_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\hfc4310me_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\n2o_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\n2o_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\n2_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\n2_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\nf3_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\nf3_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\nf_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\nf_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC2F6_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC2F6_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc2f_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc2f_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC3F8_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC3F8_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc3f_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc3f_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC4F10_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC4F10_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc4f1_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc4f1_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC5F12_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC5F12_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc5f1_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc5f1_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC6F14_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcC6F14_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc6f1_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcc6f1_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccC4F8_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccC4F8_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccc4f_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccc4f_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcCF4_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfcCF4_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccf_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\pfccf_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\sf6_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\sf6_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\sf_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\sf_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\emissions\test1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050ano2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050ano3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050ano4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_5\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_9\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050ano2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050ano3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050ano4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_7.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_8.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_9.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_c1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\ph2050_c3.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\test1.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\test2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ws\test3.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2050\ph2050_10.tif.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099ano1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099ano2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099ano3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_5\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_9\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099ano1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099ano2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099ano3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099ano4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_7.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_8.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_9.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_c1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\ph2099\ws\ph2099_c3.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\land2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist5\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist9\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\land2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist7.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist8.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist9.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist_c1.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist_c2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist_c3.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\ws\phhist_c4.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\phstd\phhist10.tif.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050hist1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050hist2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\minus_ras.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano_c1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050ano_c3.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050a_c1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050hist1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2050\ws\p2050hist2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099hist2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano_c1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099ano_c3.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099hist1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precip2099\ws\p2099hist2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\pre19562005_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\pre19562005_6\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\pre19562005_7\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\pre19562005_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\pre19562005_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\pre19562005_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\pre19562005_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\pre19562005_7.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\precipstd_c1.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\precipstd\ws\precipstd_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050hist1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050hist2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano_c1.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050ano_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050hist1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2050\ws\t2050hist2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano4\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099hist1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099hist2\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099anoc1.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano_c1.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099ano_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099hist1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\temp2099\ws\t2099hist2.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tempstd_c1\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tmp19562005_3\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tmp19562005_6\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tmp19562005_7\metadata.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tempstd_c1.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tempstd_c2.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tempstd_c3.shp.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tmp19562005_3.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tmp19562005_4.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tmp19562005_5.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tmp19562005_6.aux.xml',  # noqa
    r'C:\project\1116 FN-Sambandet Climate\graphics\tempstd\ws\tmp19562005_7.aux.xml',  # noqa
    r'C:\project\1117 SEI window\worldmap.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\antarcticabg_10m.png.aux.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\antarcticabg_10m.png.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\antarcticabg_50m.png.aux.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\antarcticabg_50m.png.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\antarctica_clip1.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ice10m_feb.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ice10m_sep.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ice50m_feb.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ice50m_sep.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\labelpoints.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\labels.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_admin_0_antarctic_claims.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_admin_0_antarctic_claim_limit_lines.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_admin_0_boundary_lines_land.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_admin_0_label_points.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_antarctic_ice_shelves_lines.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_antarctic_ice_shelves_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_coastline.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_geographic_lines.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_geography_marine_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_geography_regions_points.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_geography_regions_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_glaciated_areas.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_graticules_1.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_graticules_1_2.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_lakes.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_land.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_land_ocean_label_points.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_ocean.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_populated_places.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_10m_rivers_lake_centerlines_scale_rank.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_admin_0_boundary_lines_land.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_admin_0_countries.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_antarctic_ice_shelves_lines.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_antarctic_ice_shelves_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_coastline.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_geographic_lines.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_geography_marine_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_geography_regions_points.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_geography_regions_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_glaciated_areas.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_graticules_1_2.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_lakes.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_land.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_ocean.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_populated_places.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\ne_50m_rivers_lake_centerlines_scale_rank.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\rck10_polygon.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\antarctica\stationsPoint.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\arcticbg_10m.png.aux.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\arcticbg_10m.png.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\arcticbg_50m.png.aux.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\arcticbg_50m.png.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\arctic_clip1.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ice10m_mar.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ice10m_sep.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ice50m_mar.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ice50m_sep.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\labelpoints.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\labels.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_admin_0_boundary_lines_land.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_admin_0_countries.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_admin_0_label_points.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_coastline.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_geographic_lines.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_geography_marine_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_geography_regions_points.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_geography_regions_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_glaciated_areas.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_graticules_1.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_graticules_1_2.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_lakes.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_land.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_land_ocean_label_points.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_ocean.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_populated_places.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_10m_rivers_lake_centerlines_scale_rank.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_admin_0_boundary_lines_land.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_admin_0_countries.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_coastline.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_geographic_lines.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_geography_marine_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_geography_regions_points.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_geography_regions_polys.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_glaciated_areas.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_graticules_1_2.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_lakes.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_land.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_ocean.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_populated_places.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\data\arctic\ne_50m_rivers_lake_centerlines_scale_rank.shp.xml',  # noqa
    r'C:\project\1119 Polarportal\tilemill\web\OpenLayersv3.0.0-beta.5\examples\data\gml\topp-states-wfs.xml',  # noqa
    r'C:\project\1119 Polarportal\tilemill\web\OpenLayersv3.0.0-beta.5\examples\data\IGNWMTSCapabilities.xml',  # noqa
    r'C:\project\1119 Polarportal\tilemill\web\OpenLayersv3.0.0-beta.5\examples\data\ogcsample.xml',  # noqa
    r'C:\project\1119 Polarportal\tilemill\web\OpenLayersv3.0.0-beta.5\examples\data\WMTSCapabilities.xml',  # noqa
    r'C:\project\1119 Polarportal\tilemill\web\OpenLayersv3.0.0-beta.5\examples\example-list.xml',  # noqa
    r'C:\project\1120 Ola Hall Ghana\graphics\ghana\xghana.xml',  # noqa
    r'C:\project\1120 Ola Hall Ghana\graphics\_output\ghana.xml',  # noqa
    r'C:\project\1120 Ola Hall Ghana\graphics\_output\xghana.xml',  # noqa
    r'C:\project\1121 UArctic 2014 updates\graphics\circle_country\north2north_circular_country_april2014.xml',  # noqa
    r'C:\project\1121 UArctic 2014 updates\graphics\members_april2014\members_april2014.xml',  # noqa
    r'C:\project\1121 UArctic 2014 updates\graphics\_output\members_april2014.xml',  # noqa
    r'C:\project\1121 UArctic 2014 updates\graphics\_output\north2north_circular_country_april2014.xml',  # noqa
    r'C:\project\1122 Vallokaler\incoming\rostlokal.xml',  # noqa
    r'C:\project\1122 Vallokaler\incoming\vallokal.xml',  # noqa
    r'C:\project\1122 Vallokaler\ws\rostlokal_4.xml',  # noqa
    r'C:\project\1122 Vallokaler\ws\vallokal_4.xml',  # noqa
    r'C:\project\1125 Pappaindex\data\incoming\valgeografi_kommun.shp.xml',  # noqa
    r'C:\project\1125 Pappaindex\data\incoming\valgeografi_lan.shp.xml',  # noqa
    r'C:\project\3002 workshop\graphics\flyer\flyer2.xml',  # noqa
    r'C:\project\3002 workshop\graphics\flyer\flyer_climate.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q1\q1.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q1\q1_2.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q2\q2.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q3\q3.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q3\q3_2.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q4\q4.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q4policy\q4policy.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q5\q5.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q5\q5_2.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q6\q6.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q7\q7.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q7b\q7b.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q7c\q7c.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q8\q8.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q8b\q8b.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\q8d_incomegroup\q8d_incomegroup.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\responsesmap\responsesmap.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q1.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q1_2.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q2.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q3.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q3_2.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q4.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q4policy.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q5.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q5_2.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q6.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q7.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q7b.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q7c.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q8.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q8b.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\q8d_incomegroup.xml',  # noqa
    r'C:\project\3002 workshop\survey\graphics\_output\responsesmap.xml',  # noqa
    r'C:\project\3004 Azote\graphics\asia\asien.xml',  # noqa
    r'C:\project\3004 Azote\graphics\asia\asien_mvatten.xml',  # noqa
    r'C:\project\3004 Azote\graphics\asia\asien_vattencity.xml',  # noqa
    r'C:\project\3004 Azote\graphics\cities\ws\distro\1.0\megacities.xml',  # noqa
    r'C:\project\3004 Azote\graphics\cities\ws\distro\1.1\shape\urbanareas1_1.shp.xml',  # noqa
    r'C:\project\3004 Azote\graphics\cities\ws\old\urban.shp.xml',  # noqa
    r'C:\project\3004 Azote\graphics\citiesmaps\ws\megacities.xml',  # noqa
    r'C:\project\3004 Azote\graphics\heartmap\ws\landarea1\metadata.xml',  # noqa
    r'C:\project\3004 Azote\graphics\heartmap\ws\Land1.png.aux.xml',  # noqa
    r'C:\project\3004 Azote\graphics\heartmap\ws\landarea1.aux.xml',  # noqa
    r'C:\project\3004 Azote\graphics\heartmap\ws\landarea2.png.aux.xml',  # noqa
    r'C:\project\3004 Azote\graphics\heartmap\ws\ocean1.png.aux.xml',  # noqa
    r'C:\project\3004 Azote\graphics\heartmap\heartmap.xml',  # noqa
    r'C:\project\3004 Azote\graphics\ice2012\iceaug2012.xml',  # noqa
    r'C:\project\3004 Azote\graphics\vindkraft\vindkraft.xml',  # noqa
    r'C:\project\3004 Azote\graphics\wagnerbasemap\wagnerbasemap.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\doc\graphics\ws\lc2\metadata.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\doc\graphics\ws\lc2.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\doc\graphics\ws\lc3.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\doc\graphics\ws\lc4.png.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\nightlights\ws\land1.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\nightlights\ws\land2.tif.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\nightlights\ws\land2.tif.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\nightlights\ws\land4.png.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\nightlights\nightlights.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\country6\metadata.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\pop2\metadata.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\bound2.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\bound3.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\bound4.png.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\country2.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\country3.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\country4.png.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\country5.png.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\country6.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\country7.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\country9.shp.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\GlobalRuralUrbanMappingProjectVersion1GRUMPv1PopulationDensityGrid.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\gluds00ag.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\gluds00g.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\lakes2.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\lakes3.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\lakes4.png.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\lakes6.png.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\lakes7x.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\pop2.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\pop3.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\pop4.aux.xml',  # noqa
    r'C:\project\3005 Papercraft Atlas\graphics\pop\ws\pop6.png.aux.xml',  # noqa
    r'C:\project\3005 Running\sthlmcycling.shp.xml',  # noqa
    r'C:\project\3005 Running\sthlmwalking.shp.xml',  # noqa
    r'C:\project\3005 Running\Stockholm.shp.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\old\sthlm_fold.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\ws\bingbase2.png.aux.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\ws\bingbase_ne1.png.aux.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\ws\bingbase_nw1.png.aux.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\ws\bingbase_se1.png.aux.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\ws\bingbase_sw1.png.aux.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\ws\land1.shp.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\ws\utsnitt1.aux.xml',  # noqa
    r'C:\project\3006 Stockholm Foldable\graphics\map1\sthlm_fold2.xml',  # noqa
    r'C:\project\3008 Kartdagarna 2013\graphics\ag\agposter1.xml',  # noqa
    r'C:\project\3008 Kartdagarna 2013\graphics\ag\agposter2.xml',  # noqa
    r'C:\project\3008 Kartdagarna 2013\graphics\uarctic_tn\uarctictn_poster1.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\flex\messaging-config.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\flex\proxy-config.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\flex\remoting-config.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\flex\services-config.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\context\admin\plugin\Note\language.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\context\admin\plugin\Simon\language.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\context\admin\resources\language\de.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\context\admin\resources\language\en.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\scheduler\scheduler.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\search\search.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\smartcache\function.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\smartcache\include.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\smartcache\query.xml',  # noqa
    r'C:\project\3010 Gisplanet\wwwroot\current\WEB-INF\railo\video\video.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\10m_cultural\10m-us-parks-area.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\10m_cultural\10m_admin_0_breakaway_disputed_areas.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\10m_cultural\10m_admin_0_breakaway_disputed_areas_scale_ranks.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\10m_cultural\10m_urban_areas_landscan.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\10m_physical\10m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\10m_physical\10m_river_lake_centerlines.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\10m_physical\10m_river_lake_centerlines_scale_ranks.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\110m_cultural\110m-admin-1-states-provinces-lines-shp.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\110m_cultural\110m_admin_0_tiny_countries.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\110m_physical\110m_graticules_all\110m_wgs84_bounding_box.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\110m_physical\110m_coastline.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\110m_physical\110m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\110m_physical\110m_land.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\110m_physical\110m_ocean.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\50m_cultural\50m_admin_0_tiny_countries.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\50m_physical\50m_graticles_all\50m_wgs84_bounding_box.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1\50m_physical\50m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\10m_cultural\10m_admin_0_breakaway_disputed_areas.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\10m_cultural\10m_admin_0_breakaway_disputed_areas_scale_ranks.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\10m_cultural\10m_urban_areas_landscan.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\10m_cultural\10m_us_parks_area.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\10m_physical\10m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\10m_physical\10m_rivers_lake_centerlines.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\10m_physical\10m_rivers_lake_centerlines_scale_ranks.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\110m_cultural\110m_admin_0_tiny_countries.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\110m_cultural\110m_admin_1_states_provinces_lines_shp.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\110m_physical\110m_graticules_all\110m_wgs84_bounding_box.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\110m_physical\110m_coastline.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\110m_physical\110m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\110m_physical\110m_land.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\110m_physical\110m_ocean.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\50m_cultural\50m_admin_0_tiny_countries.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\50m_physical\50m_graticles_all\50m_wgs84_bounding_box.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d1d3\50m_physical\50m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_boundary_breakaway_disputed_areas.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_boundary_lines_land.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_boundary_lines_map_units.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_breakaway_disputed_areas.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_breakaway_disputed_areas_scale_ranks.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_countries.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_map_subunits.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_map_units.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_scale_ranks.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_scale_ranks_with_minor-islands.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_0_sovereignty.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_admin_1_states_provinces_shp.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_roads.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_urban_areas.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_urban_areas_landscan.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_cultural\10m_us_parks_area.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_lakes.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_lakes_historic.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_land.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_minor_islands.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_ocean.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_playas.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_rivers_europe.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_rivers_lake_centerlines.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\10m_physical\10m_rivers_lake_centerlines_scale_ranks.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\110m_cultural\110m_admin_0_boundary_lines_land.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\110m_cultural\110m_admin_0_tiny_countries.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\110m_cultural\110m_admin_1_states_provinces_lines_shp.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\110m_physical\110m_graticules_all\110m_wgs84_bounding_box.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\110m_physical\110m_coastline.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\110m_physical\110m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\110m_physical\110m_land.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\110m_physical\110m_ocean.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_boundary_breakaway_disputed_areas.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_boundary_lines_land.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_boundary_map_units.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_breakaway_disputed_areas.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_countries.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_map_subunits.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_scale_ranks.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_sovereignty.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_0_tiny_countries.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_cultural\50m_admin_1_states_provinces_shp.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_physical\50m_graticules_all\50m_wgs84_bounding_box.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_physical\50m_geography_regions_elevation_points.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_physical\50m_lakes.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_physical\50m_ocean.shp.xml',  # noqa
    r'C:\project\3012 Natural Earth\natural-earth-vector\updates\version_1d2\50m_physical\50m_rivers_lake_centerlines.shp.xml',  # noqa
    r'C:\project\arcgisserver\arcgisoutput\biofuels2_MapServer\wms\GetCapabilities100.xml',  # noqa
    r'C:\project\arcgisserver\arcgisoutput\biofuels2_MapServer\wms\GetCapabilities110.xml',  # noqa
    r'C:\project\arcgisserver\arcgisoutput\biofuels2_MapServer\wms\GetCapabilities111.xml',  # noqa
    r'C:\project\arcgisserver\arcgisoutput\biofuels2_MapServer\wms\GetCapabilities130.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whfwdata3.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whproj.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whres.xml',  # noqa
    r'C:\project\dox\arcgis\server\Install_guides\Server_dotnet\whst_topics.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whidata0.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whidata0.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\ehelp.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whd_topic.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whproj.xml',  # noqa
    r'C:\project\dox\arcims\90\ArcXML_Guide\Support_files\whres.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\eHelp.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whproj.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whres.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\WebHelp\whst_topics.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\ehelp.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whd_topic.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whproj.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\wms_connector\support_files\whres.xml',  # noqa
    r'C:\project\dox\arcims\90\Documentation\sample_aimsacl.xml',  # noqa
    r'C:\project\dox\arcims\90\License_Manager_Guide\ehelp.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\eHelp.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whproj.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whres.xml',  # noqa
    r'C:\project\dox\arcims\90\WebHelp\whst_topics.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\ehelp.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whd_topic.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whproj.xml',  # noqa
    r'C:\project\dox\arcims\90\wms_docs\support_files\whres.xml',  # noqa
    r'C:\project\dox\arcims\90\sample_aimsacl.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whidata0.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\ehelp.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whd_topic.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whproj.xml',  # noqa
    r'C:\project\dox\arcims\91\ArcXML_Guide\Support_files\whres.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\eHelp.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whproj.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whres.xml',  # noqa
    r'C:\project\dox\arcims\91\WebHelp\whst_topics.xml',  # noqa
    r'C:\project\dox\arcims\91\sample_aimsacl.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\eHelp.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whproj.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whres.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\WebHelp\whst_topics.xml',  # noqa
    r'C:\project\dox\arcims\92\Documentation\sample_aimsacl.xml',  # noqa
    r'C:\project\dox\arcims\old\ArcXML_Guide\WebHelp\ehelp.xml',  # noqa
    r'C:\project\dox\arcims\old\WebHelp\eHelp.xml',  # noqa
    r'C:\project\dox\arcims\old\dynamic_joins.xml',  # noqa
    r'C:\project\dox\arcsde\81\license_manager_guide\ehelp.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata3.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata4.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata5.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata6.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata7.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whfwdata8.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\ehelp.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whd_topic.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\90\Admin_Cmd_Ref\Support_files\whres.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whftdata1.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whftdata2.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata10.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata11.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata12.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata13.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata14.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata15.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata16.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata3.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata4.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata5.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata6.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata7.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata8.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whfwdata9.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata1.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata10.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata2.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata3.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata4.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata5.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata6.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata7.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata8.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtdata9.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\eHelp.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whd_topic.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\91\Admin_Cmd_Ref\Support_files\whres.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whfwdata3.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\eHelp.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whres.xml',  # noqa
    r'C:\project\dox\arcsde\91\ARCSDE91MSSQLINSTALLGUIDES\whst_topics.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\eHelp.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whres.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\ARCSDE92DEVKITINSTALLGUIDES\whst_topics.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_sdk\Dev_Help\Support_files\api\capi\logfiles\logClose.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata10.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata3.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata4.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata5.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata6.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata7.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata8.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whfwdata9.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whidata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\ehelp.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whd_topic.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\Admin_Cmd_Ref\Support_files\admincmdref92\whres.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whfwdata3.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whres.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92DB2INSTALLGUIDES\whst_topics.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whfwdata3.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whres.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92INFORMIXINSTALLGUIDES\whst_topics.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whres.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92MSSQLINSTALLGUIDES\whst_topics.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whftdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whfts.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whfwdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whfwdata1.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whfwdata2.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whglo.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whidx.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whtdata0.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whxdata\whtoc.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whproj.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whres.xml',  # noqa
    r'C:\project\dox\arcsde\92\documentation_server\ARCSDE92ORACLEINSTALLGUIDES\whst_topics.xml',  # noqa
    r'C:\project\dox\fusioncharts\HelpDocs\Data\Client.xml',  # noqa
    r'C:\project\dox\fusioncharts\HelpDocs\collapsibleXML.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\Advanced\BgSWF\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\Advanced\Discontinuous\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\Advanced\Discontinuous\Line.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\ClientSide\JavaScript\LineDemo\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\DrillDown\Basic_JS\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\DrillDown\DrillDownData.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\GridComponent\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\LoadFC\Basics\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\LoadFC\EventBased\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\LoadFC\EventBasedMultipleCharts\Data_Line.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\LoadFC\EventBasedMultipleCharts\Data_Pie.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\LoadFC\LoadingCosmetics\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\MultiSeries\SimpleChart\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\MyFirstChart\Data.xml',  # noqa
    r'C:\project\dox\fusioncharts\SampleCode\MyFirstChart\SmallChartData.xml',  # noqa
    r'C:\project\dox\mach_ii\Mach-II_1-5-0_html_CFCDoc\plugin.xml',  # noqa
    r'C:\project\dox\mach_ii\Mach-II_1-5-0_html_CFCDoc\toc.xml',  # noqa
    r'C:\project\dox\mach_ii\old\1_1\machii_info\config\mach-ii.xml',  # noqa
    r'C:\project\dox\mach_ii\old\older\mach-ii_1_0.dtd.xml',  # noqa
    r'C:\project\dox\python\diveintopython-5.4\html\history.xml',  # noqa
    r'C:\project\dox\python\diveintopython-5.4\py\kgp\binary.xml',  # noqa
    r'C:\project\dox\python\diveintopython-5.4\py\kgp\husserl.xml',  # noqa
    r'C:\project\dox\python\diveintopython-5.4\py\kgp\kant.xml',  # noqa
    r'C:\project\dox\python\diveintopython-5.4\py\kgp\russiansample.xml',  # noqa
    r'C:\project\dox\python\diveintopython-5.4\py\kgp\template.xml',  # noqa
    r'C:\project\dox\python\diveintopython-5.4\py\kgp\test.xml',  # noqa
    r'C:\project\dox\python\diveintopython-5.4\py\kgp\thanks.xml',  # noqa
    r'C:\project\dox\xmp\XMP-Metadata-UI-SDK-CC2014\XMP Metadata UI SDK CC 2014\samples\Sample Extension\schema\sampleSchema.xml',  # noqa
    r'C:\project\dox\xmp\XMP-Metadata-UI-SDK-CC2014\XMP Metadata UI SDK CC 2014\samples\Sample Extension\view\sampleView.xml',  # noqa
    r'C:\project\dox\xmp\XMP-Metadata-UI-SDK-CC2014\XMP Metadata UI SDK CC 2014\samples\Sample Extension\manifest.xml',  # noqa
    r'C:\project\fileman\config\mach-ii.xml',  # noqa
    r'C:\project\wikiapp\root\2006-11-02\config\instance.xml',  # noqa
    r'C:\project\wikiapp\root\2006-11-02\config\mach-ii.xml',  # noqa
    r'C:\project\wikiapp\root\current\config\instance.xml',  # noqa
    r'C:\project\wikiapp\root\current\config\mach-ii.xml',  # noqa
    r'C:\project\wikiapp\root\current\mach-ii.xml',  # noqa
    r'C:\project\zGRID projects\203\038\diversity\incoming\plants\terplant\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\diversity\incoming\vertebrate\all_terr\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\clip\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\clip_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\mine\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\rail\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\road\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\util\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\data\landcover.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\work\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arctic\work\landcover.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\clip\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\clip_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\mine\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\railr\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\roadr\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\util\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\landcover.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\railr.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\roadr.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\data\utillength.dbf.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\prep\power1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\prep\road4w\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\landsea1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\mine1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\mine2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\mine3\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\mineral1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\mineral2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_growth\mineral3\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\tempws_scenario\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\caff1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenariom40y\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\caff1.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\landcover.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenario00y2.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenario00y3.dbf.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenario40y2.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenario40y3.dbf.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenariom40y2.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenariom40y3.dbf.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenarionull2.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\arcticosm\work\scenarionull3.dbf.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\asia_pac\data\mineasp_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\asia_pac\data\mineasp_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\asia_pac\data\mralasp_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\asia_pac\data\mralasp_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\barents2\data\hotspots\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\barents2\work\coast1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\barents2\work\coast50km1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\barents2\work\coast50km2.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\barents2\work\landarea1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\c_asia\data\minecas_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\c_asia\data\minecas_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\c_asia\data\mralcas_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\c_asia\data\mralcas_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\c_asia\data1\minecas1_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\c_asia\data1\minecas1_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\c_asia\data1\mralcas1_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\c_asia\data1\mralcas1_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\europe\data\mineeur_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\europe\data\mineeur_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\europe\data\mraleur_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\europe\data\mraleur_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\landsea\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\rail\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\road\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\sett_poly_n\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\sett_poly_p\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\util\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\util_now\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\util_plan\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\data\popdens.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\work\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\work\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\work\impactplain2.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\work\landcover1.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\work\scenario30y2.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\work\setnu_ras.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\ws\landcover3.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\ws\landsea1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\ws\power_plan1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\ws\power_plan2.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\ws\road2.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\finnmark\ws\sett_poly_plan.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\clip\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\clip_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\mine\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\mineral\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\rail\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\road\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\data\util\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\prep\power5\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\prep\rail5\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\prep\road5\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\prep\sett_pnt5\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\prep\sett_poly5\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\coast1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\landsea1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\landsea2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\mine1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\mine2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\mine3\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\mineral1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\mineral2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_growth\mineral3\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\tempws_scenario\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\ivory\work\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\n_america\data\minenam_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\n_america\data\minenam_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\n_america\data\mralnam_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\n_america\data\mralnam_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\s_america\data\minesam_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\s_america\data\minesam_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\s_america\data\mralsam_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\s_america\data\mralsam_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\world\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\world\ws\info\arc0055.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\world\ws\landseageo1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\world\ws\minegeo1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\world\ws\mineralgeo1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\world\ws\popdens_geo1.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\w_asia\data\minewas_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\w_asia\data\minewas_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\w_asia\data\mralwas_geo\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\w_asia\data\mralwas_lam\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\clip\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\landsea\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\mine\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\mineral\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\rail\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\rail_now\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\rail_plan\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\road\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\road_now\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\road_plan\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\sett_pnt\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\sett_poly\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\util\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\util_now\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\util_plan\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\data\popdens.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\work\landcover\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\globio2\yamal\work\landcover.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\bareleval\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barforestal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barprotaal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barprotpal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barrailal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barroadal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barsettlaal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barsettlpal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\bartraffical\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\bartranspal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barwateraal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\barwaterlal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\alproj\klipperal\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\barbuffer\barbuff2a1\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\barbuffer\globio_bar\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\b1000\work\barbuffer\globio_bar.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\barents\moims\www\GLOBIOmetadata_files\filelist.xml',  # noqa
    r'C:\project\zGRID projects\203\038\old\barents\moims\www\filelist.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_11_26\_notes\colors.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_11_26\_notes\dwSiteColumnsMe.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_11_26\_notes\flash.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_11_26\_notes\images.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_11_26\_notes\movies.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_11_26\_notes\scripts.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_11_26\_notes\shockwave.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_11_26\_notes\urls.xml',  # noqa
    r'C:\project\zGRID projects\203\038\website\2001_12_04\old\copied_2001_11_28\_notes\dwSiteColumnsMe.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\nh_dem2.bmp.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\nh_march1.bmp.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\sh_dem2.bmp.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\sh_sept1.bmp.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\srtm_ramp2.world.5400x2700.jpg.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\world.200403.3x5400x2700.jpg.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\world.200403.3x5400x2700.jpg.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\world.200409.3x5400x2700.jpg.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\2_globes\ws\world.200409.3x5400x2700.jpg.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\4_snowbigov\ws\shelf1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\4_springsnowcover\ws\snow6.bmp.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\6a_ov\ws\bg1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\6a_ov\ws\country1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\6b_ov\ws\bg1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\6b_ov\ws\country1.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\6b_ov\ws\glacier2.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\6b_ov\ws\glacier2a.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\6b_wgms_monitoring\ws\glacier2.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\7_ov\ws\antarctica2.jpg.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\7_permafrostscenario\ws\ice2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\7_permafrostscenario\ws\perma1999_2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\7_permafrostscenario\ws\perma2099_2\metadata.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\7_permafrostscenario\ws\change2099_1.aux.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\7_permafrostscenario\ws\ice.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\7_permafrostscenario\ws\mti2d_2080-99_result.shp.xml',  # noqa
    r'C:\project\zGRID projects\203\088 GEO 4 Ice and Snow\graphics\_incoming\mzemp\DataHugo1\Textbox1\glacDCW.shp.xml',  # noqa
]
# }}}

aiFiles = []

for thisXml in allXml:
    aiFile = '.'.join(thisXml.split('.')[0:-1]) + '.ai'
    if os.path.isfile(aiFile):
        aiFiles.append(aiFile)

with open('filestodo.txt', 'w') as filetodo:
    for thisFile in aiFiles:
        filetodo.write(thisFile + '\n')
