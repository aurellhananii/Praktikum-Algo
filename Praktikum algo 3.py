# Aurelia Clariza Hanani
# 065002500014

import math
 
print("Silahkan isi Lattitude dan Longitudenya untuk menentukan jarak")

r = 6371 # dalam kilometer
titik1 = input("Masukan nama titik pertama permukaan: ")
titik2 = input("Masukan nama titik kedua permukaan: ")
lat1 = float(input("Lattitude1: "))
lon1 = float(input("Longitude1: "))
lat2 = float(input("Lattitude2: "))
lon2 = float(input("Longitude2: "))
lat1_rad = math.radians(lat1)
lon1_rad = math.radians(lon1)
lat2_rad = math.radians(lat2)
lon2_rad = math.radians(lon2)
dlon = lon2_rad - lon1_rad
dlat = lat2_rad - lat2_rad
a = math.sin(dlat/2)**2 + math.cos(lat1_rad)*math.cos(lat2_rad)*math.sin(dlon/2)**2
c = 2 *math.atan2(math.sqrt(a), math.sqrt(1-a))
jarak = r * c
print("Jarak antara Jakarta dan Yogyakarta adalah: ", jarak,"kilometer")