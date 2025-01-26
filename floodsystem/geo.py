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
    return list_of_stations

def locate_town(stations, station_name):
    for station in stations:
        if station.name == station_name:
            return station.town


import math
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


def stations_in_radius(stations, centre, r):
    lat_centre, long_centre = centre
    stations_in_radius = []
    for station in stations:
        lat_station, long_station = station.coord
        distance = haversine1(lat_centre, long_centre, lat_station, long_station)
        if distance < r:
            
            stations_in_radius.append(station.name)
            stations_in_radius.sort()

            
    return stations_in_radius
    


def rivers_with_station(stations):
    rivers = []
    for station in stations:
        rivers.append(station.river)
    rivers = list(set(rivers))
    rivers.sort()
    return rivers


def stations_by_river(stations):
    stations_by_river = {}
    for station in stations:
        if station.river not in stations_by_river:
            stations_by_river[station.river] = [station.name]
        else:
            stations_by_river[station.river].append(station.name)
            stations_by_river[station.river].sort()
    return stations_by_river

def rivers_by_station_number(stations, N):
    rivers_by_station_number = {}
    for station in stations:
        if station.river not in rivers_by_station_number:
            rivers_by_station_number[station.river] = 1
        else:
            rivers_by_station_number[station.river] += 1
        

    sorted_rivers = sorted(rivers_by_station_number.items(), key=lambda x: x[1], reverse=True)

    
    top_rivers = sorted_rivers[:N]
    if len(sorted_rivers) > N:
        nth_count = sorted_rivers[N-1][1]
        for river, count in sorted_rivers[N:]:
            if count == nth_count:
                top_rivers.append((river, count))
            else:
                break

    return top_rivers
