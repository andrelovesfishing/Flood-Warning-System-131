from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1A"""
    # Build list of stations
    stations = build_station_list()

    #Define coordinate p
    p1 = float(input("Give p latitude"))
    p2 = float(input("Give p latitude"))
    p = (p1,p2)

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    stations_by_distance(stations, p)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
