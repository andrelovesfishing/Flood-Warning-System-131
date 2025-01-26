from floodsystem.geo import stations_in_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""
    stations = build_station_list()
    in_radius = stations_in_radius(stations, (52.2053, 0.1218), 10)
    print(in_radius)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()