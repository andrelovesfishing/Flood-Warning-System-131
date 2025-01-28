import plotly.express as px
import pandas as pd
from floodsystem.stationdata import build_station_list


def run():
    # Build list of stations
    stations = build_station_list()
    list_of_stations = []
    latitudes = []
    longitudes = []
    places = []
    for station in stations:
        list_of_stations.append((station.name, station.coord))
    
    for item in list_of_stations:
        places.append(item[0])
        latitudes.append(item[1][0])
        longitudes.append(item[1][1])
    
    # Example coordinates
    data = {
        'lat': latitudes,
        'lon': longitudes,
        'station': places
    }
    #Using a panda dictionary data structure makes the process more efficient
    df = pd.DataFrame(data)

    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        text="station",
        zoom=3,
        mapbox_style="carto-positron"
    )

    
    fig.show()
    

if __name__ == "__main__":
    print("*** Task 1 extension: CUED Part IA Flood Warning System ***")
    run()