import folium
from IPython.display import display

map_center = [5.6899767, -0.2089417]
mymap = folium.Map(location=map_center, zoom_start=4)

folium.Marker(
[5.6899767, -0.2089417],
    popup='Academic City University College',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(mymap)

display(mymap)