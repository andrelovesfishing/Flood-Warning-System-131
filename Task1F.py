from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1D"""
    #Create a list of stations
    stations = build_station_list()

    #Iterates through list and spots anomalies
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    print(inconsistent_stations)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
