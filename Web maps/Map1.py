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

data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],
    radius=10,
    popup=str(el) + " m",
    fill_color=color_select(el),
    fill=True,
    color="gray",
    fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor":"yellow" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] <= 20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")