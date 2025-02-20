from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    stations_list = stations_highest_rel_level(stations,5)
    for item in stations_list:
        print(item[0], item[1])

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()