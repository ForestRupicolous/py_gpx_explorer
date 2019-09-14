from os import listdir
from os.path import isfile, join
import gpxpy
import folium

data_path = '../tracks'
data = [f for f in listdir(data_path) if isfile(join(data_path, f))]
start_lat = 48.1450271619894 
start_lon = 16.29765455716531
# Load map 
my_map = folium.Map(location=[start_lat, start_lon], zoom_start=12)

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
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(my_map)
    points =[]

#ave_lat = sum(p[0] for p in points)/len(points)
#ave_lon = sum(p[1] for p in points)/len(points)
#print(ave_lat,ave_lon)
#centred on average coordinates
#my_map.location = [ave_lat, ave_lon]

#add a markers
#for each in points:  
#    folium.Marker(each).add_to(my_map)


# Save map
my_map.save("./gpx.html")
