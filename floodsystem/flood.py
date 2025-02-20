from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels

def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    stations_over_threshold = []
    for station in stations:
        if station.relative_water_level() is not None and station.typical_range_consistent() is True:
            if station.relative_water_level() > tol:
                stations_over_threshold.append((station.name, station.relative_water_level()))
    
    stations_over_threshold = sorted(stations_over_threshold, key=lambda x: x[1], reverse=True)
    return stations_over_threshold