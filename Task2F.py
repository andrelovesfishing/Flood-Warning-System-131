from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime 

def run():
    # Build list of stations
    stations = build_station_list()

    top_five_stations = []
    stations_list = stations_highest_rel_level(stations,5)
    for item in stations_list:
        top_five_stations.append(item[0])

    # Station name to find
    for station in top_five_stations:
        station_name = station

        # Find station
        station_cam = None
        for station in stations:
            if station.name == station_name:
                station_cam = station
                break

        # Check that station could be found. Return if not found.
        if not station_cam:
            print("Station {} could not be found".format(station_name))
            return

        # Fetch and plot data for the past 10 days for each of these stations
        dt = 10
        dates, levels = fetch_measure_levels(
            station_cam.measure_id, dt=datetime.timedelta(days=dt))
        list_of_dates = []
        list_of_levels = []
        for date, level in zip(dates, levels):
            list_of_dates.append(date.replace(tzinfo=None))
            list_of_levels.append(level)

        # Print level history
        plot_water_level_with_fit(station_cam, list_of_dates, list_of_levels,2)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()


