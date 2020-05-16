import folium
map = folium.Map(location=[50,50], zoom_start=15, tiles="Stamen Terrain")
map.save("Map1.html")