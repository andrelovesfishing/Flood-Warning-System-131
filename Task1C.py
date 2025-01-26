from floodsystem.geo import stations_in_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()
f = stations_in_radius(stations, (52.2053, 0.1218), 10)
print(f)