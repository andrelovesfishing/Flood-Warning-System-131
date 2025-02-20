from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

stations = build_station_list()
x = stations_highest_rel_level(stations, 10)
print("Top 10 stations with highest relative water levels:")
for station in x:
    print(f"Station: {station.name}, Relative Water Level: {station.rel_water_level()}")
