import plotly.express as px
import pandas as pd
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels


def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    list_of_stations = []
    latitudes = []
    longitudes = []
    places = []
    level_fraction = []
    for station in stations:
        list_of_stations.append((station.name, station.coord, station.relative_water_level()))
    
    for item in list_of_stations:
        places.append(item[0])
        latitudes.append(item[1][0])
        longitudes.append(item[1][1])
        level_fraction.append(item[2])
    print(list_of_stations)
    # Example coordinates
    data = {
        'lat': latitudes,
        'lon': longitudes,
        'station': places
    }
    #Using a panda dictionary data structure makes the process more efficient
    df = pd.DataFrame(data)

    colour_map = {}

    for i,place in enumerate(places):
        if level_fraction[i] is None:
            colour_map[place] = "grey"
            continue

        if level_fraction[i] > 1:
            colour_map[place] = "red"
        elif level_fraction[i] > 0:
            colour_map[place] = "blue"
        elif level_fraction[i] < 0:
            colour_map[place] = "green"
        else:
            colour_map[place] = "grey"

    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        text="station",
        color = "station",
        color_discrete_map=colour_map,
        zoom=5,
        mapbox_style="carto-positron"
    )

    
    fig.show()
    

if __name__ == "__main__":
    print("*** Task 1 extension: CUED Part IA Flood Warning System ***")
    run()