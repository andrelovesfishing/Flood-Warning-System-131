def stations_level_over_threshold(stations, tol):
    pass



def stations_highest_rel_level(stations, N):
    """Return a list of the N stations with the highest relative water level."""
    # Filter out stations with no relative water level data
    stations_with_data = [station for station in stations if station.relative_water_level() is not None]
    
    # Sort the stations by relative water level in descending order
    stations_with_data.sort(key=lambda station: station.relative_water_level(), reverse=True)
    
    # Return the top N stations
    return stations_with_data[:N]