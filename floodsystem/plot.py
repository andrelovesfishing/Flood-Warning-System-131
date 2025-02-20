import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def plot_water_levels(station, dates, levels):
    """Plot water levels for a station."""
    if len(dates) != len(levels):
        raise ValueError("Length of dates and levels must be the same")
    
    v = station.typical_range[0]
    h = station.typical_range[1]
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.axhline(v, color= 'red', linestyle='--', label='low value')
    plt.axhline(h, color='blue', linestyle='--', label='high value')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()