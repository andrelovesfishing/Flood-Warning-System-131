# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
    "Build and return a list of stations with their respective distances from co-ordinate p"
    list_of_stations = []
    for station in stations:
        list_of_stations.append((station.name, haversine(station.coord, p)))
    list_of_stations = sorted_by_key(list_of_stations, 1)
    print(list_of_stations)
    pass

import math
"function to calculate the distance between two points on the Earth given their latitude and longitude"
def haversine1(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])
    dlat = lat2 - lat1
    dlon = long2 - long1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of Earth in kilometers
    R = 6371
    distance = R * c
    return distance

"function to find all stations within a given radius of a given coordinate"
def stations_in_radius(stations, centre, r):
    lat_centre, long_centre = centre
    "create an empty list to store the names of stations within the radius"
    stations_in_radius = [] 
    for station in stations:
        lat_station, long_station = station.coord
        distance = haversine1(lat_centre, long_centre, lat_station, long_station)
        if distance < r:
            "append the name of the station to the list if it is within the radius"
            stations_in_radius.append(station.name)
            stations_in_radius.sort()

            
    return stations_in_radius
    

"function to find all rivers with a monitoring station"
def rivers_with_station(stations):
    rivers = []
    for station in stations:
        rivers.append(station.river)
    "remove duplicates"
    rivers = list(set(rivers)) 
    rivers.sort()
    return rivers


def stations_by_river(stations):
    "create empty dictionary to store stations by river"
    stations_by_river = {}
    "iterate through the list of stations and add the station name to the river key in the dictionary"
    for station in stations:
        if station.river not in stations_by_river:
            stations_by_river[station.river] = [station.name]
        else:
            stations_by_river[station.river].append(station.name)
            "sort the stations by river"
            stations_by_river[station.river].sort()
    return stations_by_river

def rivers_by_station_number(stations, N):
    "create an empty dictionary to store the number of stations by river"
    rivers_by_station_number = {}
    "iterate through the list of stations and add the river to the dictionary"
    for station in stations:
        if station.river not in rivers_by_station_number:
            rivers_by_station_number[station.river] = 1
        else:
            rivers_by_station_number[station.river] += 1
        
    "sort the rivers by the number of stations"
    sorted_rivers = sorted(rivers_by_station_number.items(), key=lambda x: x[1], reverse=True)

    "make sure all rivers with the same number of stations as the Nth river are included"
    top_rivers = sorted_rivers[:N]
    if len(sorted_rivers) > N:
        nth_count = sorted_rivers[N-1][1]
        for river, count in sorted_rivers[N:]:
            if count == nth_count:
                top_rivers.append((river, count))
            else:
                break

    return top_rivers
