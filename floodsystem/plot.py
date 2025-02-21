import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """Plot water levels for a station."""

    low = station.typical_range[0]
    high = station.typical_range[1]
    
    if len(dates) != len(levels):
        raise ValueError("Length of dates and levels must be the same")
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(low, color= 'red', linestyle='--', label='low value')
    plt.axhline(high, color='blue', linestyle='--', label='high value')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly_coeff, d0 = polyfit(dates,levels,p)
    true_dates = mdates.date2num(dates)
    print(poly_coeff, "- poly")
    polynomial_expression = np.poly1d(poly_coeff)
    print(polynomial_expression, "- y")
    plt.plot(dates, levels)
    plt.plot(dates,polynomial_expression(true_dates))
    

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.show()