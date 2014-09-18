function init() {
	var map = L.map('map')
	var osm = new L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

	
	var amtrak_data = L.geoJson(amtrak_geojson, {
		onEachFeature: amtrak_on_each_feature
	});
	
	var nps_data = L.geoJson(nps_geojson, {
		onEachFeature: federal_on_each_feature,
	    	style: nps_style
	});
		
	var fs_data = L.geoJson(fs_geojson, {
		onEachFeature: federal_on_each_feature,
	    	style: fs_style
	});
	
	map.addLayer(osm);
	
	amtrak_data.addTo(map);
	nps_data.addTo(map);
	fs_data.addTo(map);
		
	map.fitBounds(fs_data.getBounds());
}

function amtrak_on_each_feature(feature, layer) {
	layer.bindPopup(feature.properties.STN_NAME);
}

function federal_on_each_feature(feature, layer) {
	layer.bindPopup(feature.properties.NAME1);
}

function nps_style(feature) {
	return {'color': '#006600',
		'weight': 1};

}

function fs_style(feature) {
	return {'color': '#3333FF',
		'weight': 1};
}

window.onLoad = init();
