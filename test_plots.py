import matplotlib.pyplot as plt
import datetime as dte
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels
import pytest



def test_plot_water_levels():
    # Create a test station
    station = MonitoringStation("test-s-id-1", "test-m-id-1", "Test Station", (52.2053, 0.1218), (0.5, 1.0), "Test River", "Test Town")
    
    # Example dates and water levels
    dates = [dte.datetime(2023, 1, 1), dte.datetime(2023, 1, 2), dte.datetime(2023, 1, 3)]
    levels = [0.6, 0.8]
    
    with pytest.raises(ValueError):
        plot_water_levels(station, dates, levels)


