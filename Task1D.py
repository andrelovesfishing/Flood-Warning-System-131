from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    stations_by_river_dict = stations_by_river(stations)

    print(f"Number of rivers with at least one station: {len(stations_by_river_dict)}")
    
    # Print the number of stations for each river
    river_names = sorted(stations_by_river_dict.keys())
    for river in river_names[:10]:
        print(river)

    #Prints stations situated on chosen rivers
    specific_rivers = ["River Aire", "River Cam", "River Thames"]
    for river in specific_rivers:
        if river in stations_by_river_dict:
            print(f"Stations on {river}: {stations_by_river_dict[river]}")
            
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()