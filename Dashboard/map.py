from geopy.geocoders import Nominatim
from IPython.core.display_functions import display
import pandas as pd
import folium

geolocator = Nominatim(user_agent='Nominatim(user_agent="my-application")')
location = geolocator.geocode('France')
print(location.address)



locations = locations[["latitude", "longitude", "name"]]

map = folium.Map(location=[locations.latitude.mean(), locations.longitude.mean()], zoom_start=14,control_scale=True)
display(map)