import gpxpy
import matplotlib.pyplot as plt

gpx_file = open('../tracks/track_2019-09-12_07-15.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
