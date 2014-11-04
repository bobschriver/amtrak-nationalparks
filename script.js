function init() {
	var map = L.map('map')
	var osm = new L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

	
	var amtrak_data = L.geoJson(amtrak_geojson, {
		pointToLayer: amtrak_point_to_layer,
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

function amtrak_point_to_layer(feature_data, latlng) {
	return L.marker(latlng, {icon: new L.Icon.Default
		({
			iconSize: [28, 42],
			iconAnchor: [2, 7],
			popupAncor: [0, 28],
			shadowSize: [42, 28],
			shadowAnchor: [2, 0],
		})
	});
}

function amtrak_on_each_feature(feature, layer) {
	layer.bindPopup(feature.properties.STN_NAME);
}

function federal_on_each_feature(feature, layer) {
	layer.bindPopup(feature.properties.NAME1 + '<br>' + feature.properties.closest_station + '<br>' + (feature.properties.closest_station_distance * 100).toFixed(2) + ' Miles');
}

function nps_style(feature) {
	return {'color': '#006600',
		'weight': 1};

}

function fs_style(feature) {
	return {'color': '#000099',
		'weight': 1};
}

window.onLoad = init();
