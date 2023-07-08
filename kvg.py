import pandas as pd
import numpy as np
import math

df = pd.read_excel("in.xlsx")

print(len(df))

key = df.iloc[2,2]
keyv = key[:5]
dzi = df.iloc[2,3]
dzip = dzi[:5]
dzip = np.int64(dzip)
keyv = np.int64(keyv)


print(keyv)
print(dzip)
print(type(keyv))
print(type(dzip))


df1 = pd.read_excel("Gazzet.xlsx")
print(df1.iloc[2,0])
#con = str(df1.iloc[1,0])
print(df1[df1['zcta5']==keyv].index[0])
orlat = df1.iloc[df1[df1['zcta5']==keyv].index[0],1]
orlan = df1.iloc[df1[df1['zcta5']==keyv].index[0],2]
print(df1[df1['zcta5']==dzip].index[0])
deslat = df1.iloc[df1[df1['zcta5']==dzip].index[0],1]
deslon = df1.iloc[df1[df1['zcta5']==dzip].index[0],2]
print(orlat)
print(orlan)

print(deslat)
print(deslon)

print(type(orlan))
print(type(deslat))
print(type(deslon))
lat1_rad = math.radians(orlat)
lon1_rad = math.radians(orlan)
lat2_rad = math.radians(deslat)
lon2_rad = math.radians(deslon)
print(lat1_rad)
distance = math.acos(math.sin(lat1_rad) * math.sin(lat2_rad) +
                         math.cos(lat1_rad) * math.cos(lat2_rad) *
                         math.cos(lon2_rad - lon1_rad)) * 6371
detor = distance*1.417
#print(key = df.iloc[1,13])
df.insert(7, "Origin Zip - 5 digit", keyv, True)
df.insert(8, "Destination Zip - 5 digit", dzip, True)
df.insert(9, "Origin Lat", orlat, True)
df.insert(10, "Origin Lon", orlan, True)
df.insert(11, "Destination Lat", deslat, True)
df.insert(12, "Destination Lon", deslon, True)
df.insert(13, "Total straight line distance (km)", distance, True)
df.insert(14, "Total detour distance (km)", detor, True)
df.to_excel("in.xlsx")

#ke = df.iloc[1,13]
#print(ke)
