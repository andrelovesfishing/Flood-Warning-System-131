from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import locate_town

def run():
    """Requirements for Task 1A"""
    # Build list of stations
    stations = build_station_list()

    #Define coordinate p
    #p1 = float(input("Give p latitude"))
    #p2 = float(input("Give p latitude"))
    #p = (p1,p2)

    p = (52.2053, 0.1218)

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))
    
    #Builds list of stations in order of distance
    list_of_station_distance = stations_by_distance(stations, p)
    newlist = []
    
    #Creates a new list that includes town of station
    for item in list_of_station_distance:
        newlist.append((item[0], locate_town(stations, item[0]), item[1]))
    print (newlist)
        

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
