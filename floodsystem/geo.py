# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def stations_by_distance():
    pass

    

import math
def haversine( lat1, long1, lat2, long2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of Earth in kilometers
    R = 6371
    distance = R * c
    return distance


def stations_in_radius(stations, centre, r):
    lat_centre, long_centre = centre
    stations_in_radius = []
    for station in stations:
        lat_station, long_station = station.coord
        distance = haversine(lat_centre, long_centre, lat_station, long_station)
        if distance <= r:
            
            stations_in_radius.append(station)

            
    return stations_in_radius
    