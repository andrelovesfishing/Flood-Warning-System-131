from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
import matplotlib.dates as mdates

def polyfit_1(dates, levels, p):
    """Fit a polynomial of degree p to water level data."""
    # Convert dates to numerical format
    true_dates = mdates.date2num(dates)
    
    # Shift dates to improve numerical stability
    d0 = true_dates[0]
    shifted_dates = true_dates - d0
    
    # Fit polynomial
    poly = np.polyfit(shifted_dates, levels, p)
    
    return poly, d0

def assess_flood_risk(stations):
    risk_levels = []

    # Fetch and analyze data for each station
    for station in stations:
        
        
        # Fetch data for the past 10 days
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        if not dates or not levels:
            print(f"No data for station {station.name}")
            continue
        
        # Calculate relative water level
        relative_level = station.relative_water_level()
        
        if relative_level is None:
            print(f"Skipping station {station.name} due to no relative level")
            continue
        
        # Fit polynomial to water level data
        poly, d0 = polyfit_1(dates, levels, 4)
        
        # Calculate the derivative of the polynomial at the latest date
        poly_derivative = np.polyder(poly)
        latest_date_num = mdates.date2num(dates[-1])
        trend = np.polyval(poly_derivative, latest_date_num - d0)
        
        # Assess risk based on relative level and trend
        if relative_level > 2.0 or (relative_level > 1.5 and trend > 0):
            risk = 'severe'
        elif relative_level > 1.5 or (relative_level > 1.0 and trend > 0):
            risk = 'high'
        elif relative_level > 1.0 or (relative_level > 0.5 and trend > 0):
            risk = 'moderate'
        else:
            risk = 'low'
        
        risk_levels.append((station.town, risk))
    
    return risk_levels

def run():
    # Build list of stations
    stations = build_station_list()

    # Update water levels for all stations
    update_water_levels(stations)

    # Assess flood risk
    risk_levels = assess_flood_risk(stations)

    # Print towns with their assessed risk levels
    if not risk_levels:
        print("No risk levels assessed.")
    for town, risk in risk_levels:
        print(f"Town: {town}, Risk Level: {risk}")

if __name__ == "__main__":
    print("*** Task 2G2: CUED Part IA Flood Warning System ***")
    run()