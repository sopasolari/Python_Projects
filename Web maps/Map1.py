import folium

map = folium.Map(location=[37.976445, 23.725094], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38,24],popup="Hello from Greece!",icon=folium.Icon(color="orange")))
map.add_child(fg)

map.save("Map1.html")