import pandas as pd
import numpy as np
import math

df = pd.read_excel("in.xlsx")

print(len(df))
for i in range(1, len(df)):

    key = df.iloc[i, 2]
    if isinstance(key, int):
        keyv = key
    else:
        keyv = key[:5]

    dzi = df.iloc[i, 3]
    if isinstance(dzi, int):
        dzip = dzi
    else:
        dzip = dzi[:5]

    dzip = np.int64(dzip)
    keyv = np.int64(keyv)

    if key == 0:
        continue
    else:
        print(keyv)
        print(dzip)
        print(type(keyv))
        print(type(dzip))

        key = ''
        dzi = ''
        df1 = pd.read_excel("Gazzet.xlsx")
        print(df1.iloc[2, 0])
        #con = str(df1.iloc[1,0])
        print(df1[df1['zcta5'] == keyv].index[0])
        orlat = df1.iloc[df1[df1['zcta5'] == keyv].index[0], 1]
        orlan = df1.iloc[df1[df1['zcta5'] == keyv].index[0], 2]
        print(df1[df1['zcta5'] == dzip].index[0])
        deslat = df1.iloc[df1[df1['zcta5'] == dzip].index[0], 1]
        deslon = df1.iloc[df1[df1['zcta5'] == dzip].index[0], 2]
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
        df.loc[i, "Origin Zip - 5 digit"] = keyv
    df.loc[i, "Destination Zip - 5 digit"] = dzip
    df.loc[i, "Origin Lat"] = orlat
    df.loc[i, "Origin Lon"] = orlan
    df.loc[i, "Destination Lat"] = deslat
    df.loc[i, "Destination Lon"] = deslon
    df.loc[i, "Total straight line distance (km)"] = distance
    df.loc[i, "Total detour distance (km)"] = detor
    df.to_excel("in.xlsx")
    df.to_excel("in.xlsx")

    #ke = df.iloc[1,13]
    # print(ke)
