from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list()
x = rivers_by_station_number(stations, 9)
print(x)