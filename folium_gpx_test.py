from os import listdir
from os.path import isfile, join
import gpxpy
import folium

data_path = '../tracks'
data = [f for f in listdir(data_path) if isfile(join(data_path, f))]
start_lat = 48.1450271619894 
start_lon = 16.29765455716531
# Load map 
my_watercolor_map = folium.Map(tiles='Stamen Watercolor', location=[start_lat, start_lon], zoom_start=12)
my_map = folium.Map(tiles='Stamen Terrain', location=[start_lat, start_lon], zoom_start=12)

points = []

for activity in data:
    gpx_filename = join(data_path, activity)
    gpx_file = open(gpx_filename, 'r')
    print("Opend:", gpx_filename)
    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    #fadd lines
    folium.PolyLine(points, color="red", weight=2.5, opacity=0.6).add_to(my_map)
    folium.PolyLine(points, color="darkred", weight=2.7, opacity=0.4).add_to(my_watercolor_map)
    points =[]


# Save map
my_watercolor_map.save("./watergpx.html")
my_map.save("./folium_gpx.html")
