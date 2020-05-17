import folium
import pandas

def color_select(eleve):
    if eleve < 1000 :
        return "green"
    elif eleve >= 1000 and eleve < 3000 :
        return "orange"
    else :
        return "red"


map = folium.Map(location=[35.5, -110], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])


for lt,ln, el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el) + " m",icon=folium.Icon(color=color_select(el))))
map.add_child(fg)

map.save("Map1.html")