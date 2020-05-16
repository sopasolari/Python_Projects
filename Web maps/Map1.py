import folium
map = folium.Map(location=[37.976445, 23.725094], zoom_start=6, tiles="Stamen Terrain")
map.add_child(folium.Marker(location=[37.9,23.7],popup="Hello from Greece!",icon=folium.Icon(color="orange")))
map.save("Map1.html")