function init() {
	L.mapbox.accessToken = 'pk.eyJ1IjoiYm9ic2Nocml2ZXIiLCJhIjoiSUdjdEwwTSJ9.frrQ0LuUZAq1tYhewPldSQ';

	var map = L.mapbox.map('map', 'bobschriver.kc56keio').setView([43.639, -116.184], 6);
	
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
	
	amtrak_data.addTo(map);
	nps_data.addTo(map);
	fs_data.addTo(map);		
}

//TODO: put this in the geojson
function amtrak_point_to_layer(feature, latlng) {
	return L.marker(latlng, {	
		'icon': L.mapbox.marker.icon({
			'marker-color': '#FF8533',
			'marker-size': 'small',
			'marker-symbol': 'rail'
		})
	});
}

//TODO: mapbox makes this irrelevant with the Title and Description geojson properties
function amtrak_on_each_feature(feature, layer) {
	layer.bindPopup(feature.properties.STN_NAME);
}

function federal_on_each_feature(feature, layer) {
	layer.bindPopup(feature.properties.NAME1 + '<br>' + 'Closest Station: ' + feature.properties.closest_station + '<br>' + 'Distance: ' + (feature.properties.closest_station_distance * 100).toFixed(2) + ' Miles');
}

//TODO: I think its possible to put polygon styles in the geojson w/ mapbox?
function nps_style(feature) {
	return {'color': '#060',
		'weight': 1};

}

function fs_style(feature) {
	return {'color': '#33F',
		'weight': 1};
}

window.onLoad = init();
