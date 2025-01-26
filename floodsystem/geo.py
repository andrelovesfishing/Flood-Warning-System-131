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