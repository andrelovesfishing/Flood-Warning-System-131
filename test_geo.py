from floodsystem.geo import haversine1
from haversine import haversine
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river 
from floodsystem.geo import rivers_by_station_number



def test_haversine1():
    """Test manual haversine"""
    given = haversine1((52.2053, 0.1218), (50.0, 25.0))
    answer = haversine((52.2053, 0.1218), (50.0, 25.0))
    assert given == answer

import random
def test_stations_by_distance():
    """Tests type of values returned"""
    from floodsystem.geo import stations_by_distance
    from floodsystem.stationdata import build_station_list
    stations = build_station_list()
    random_station = random.choice(stations)
    assert type(random_station.name) == str and type(random_station.coord) == tuple
    assert type(random_station.coord[0]) == float and type(random_station.coord[1]) == float

from floodsystem.geo import stations_in_radius

def test_stations_in_radius():
    """Ensures stations given are in a list data structure"""
    stations = build_station_list()
    variable = stations_in_radius(stations, (25.0, 10.0) ,5)
    assert type(variable) == list

test_stations_in_radius()
test_stations_by_distance()


def test_stations_by_river():
    """Ensures returned data structure is a dictionary"""
    stations = build_station_list()
    variable = stations_by_river(stations)
    assert type(variable) == dict
        

def test_rivers_by_station_number():
    stations = build_station_list()
    variable = rivers_by_station_number(stations, 13)
    assert type(variable) == list
    if len(variable) > 13:
       for river, count in variable[13:]:
           assert count == variable[12][1]
