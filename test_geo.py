from floodsystem.geo import haversine1
from haversine import haversine
from floodsystem.stationdata import build_station_list

def test_haversine1():
    given = haversine1((52.2053, 0.1218), (50.0, 25.0))
    answer = haversine((52.2053, 0.1218), (50.0, 25.0))
    assert given == answer

import random
def test_stations_by_distance():
    from floodsystem.geo import stations_by_distance
    from floodsystem.stationdata import build_station_list
    stations = build_station_list()
    random_station = random.choice(stations)
    assert type(random_station.name) == str and type(random_station.coord) == tuple
    assert type(random_station.coord[0]) == float and type(random_station.coord[1]) == float

from floodsystem.geo import stations_in_radius

def test_stations_in_radius(r):
    
    stations = build_station_list()
    variable = stations_in_radius(stations, (25.0, 10.0) ,5)
    assert type(variable[0]) == str

test_stations_by_distance()
     
   
    