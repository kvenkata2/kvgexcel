import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the straight line distance between two points on Earth using the Haversine formula.

    Args:
        lat1 (float): The latitude of the first point in degrees.
        lon1 (float): The longitude of the first point in degrees.
        lat2 (float): The latitude of the second point in degrees.
        lon2 (float): The longitude of the second point in degrees.

    Returns:
        float: The straight line distance between the two points in kilometers.
    """

    # Convert the latitudes and longitudes to radians.
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate the difference between the latitudes and longitudes.
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    # Calculate the haversine distance.
    a = math.sin(d_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Return the distance in kilometers.
    return 6371 * c

if __name__ == "__main__":
    lat1 = 34.366336 
    lon1 = -84.917546
    lat2 =33.948632 
    lon2 =-83.995766 

    distance = haversine_distance(lat1, lon1, lat2, lon2)

    print(distance)

