from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1E"""
    stations = build_station_list()

    #Returns top 9 rivers, can include more items if there are more than one river with the lowest value
    x = rivers_by_station_number(stations, 9)
    print(x)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
