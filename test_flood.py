from floodsystem import station
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def test_no_stations_over_threshold():
    # Create mock stations with low water levels
    stations = [
        MonitoringStation("test-s-id-1", "test-m-id-1", "Station A", (52.2053, 0.1218), (0.5, 1.0), "River 1", "Town 1"),
        MonitoringStation("test-s-id-2", "test-m-id-2", "Station B", (52.2050, 0.1215), (0.5, 1.0), "River 2", "Town 2"),
        MonitoringStation("test-s-id-3", "test-m-id-3", "Station C", (52.2060, 0.1220), (0.5, 1.0), "River 3", "Town 3"),
    ]
    
    # Set the latest water levels
    stations[0].latest_level = 0.3
    stations[1].latest_level = 0.6
    stations[2].latest_level = 0.7
    
    threshold = 1.0
    result = stations_level_over_threshold(stations, threshold)
    assert result == [], "Test failed: Expected empty list when no stations are above the threshold"

if __name__ == "__main__":
    test_no_stations_over_threshold()
    print("All tests passed.")


# The test passes because the function correctly returns an empty list when no stations are above the threshold.

def test_stations_highest_rel_level():
    # Create mock stations with known relative water levels
    stations = [
        MonitoringStation("test-s-id-1", "test-m-id-1", "Station A", (52.2053, 0.1218), (0.5, 1.0), "River 1", "Town 1"),
        MonitoringStation("test-s-id-2", "test-m-id-2", "Station B", (52.2050, 0.1215), (0.5, 1.0), "River 2", "Town 2"),
        MonitoringStation("test-s-id-3", "test-m-id-3", "Station C", (52.2060, 0.1220), (0.5, 1.0), "River 3", "Town 3"),
        MonitoringStation("test-s-id-4", "test-m-id-4", "Station D", (52.2070, 0.1230), (0.5, 1.0), "River 4", "Town 4"),
        MonitoringStation("test-s-id-5", "test-m-id-5", "Station E", (52.2080, 0.1240), (0.5, 1.0), "River 5", "Town 5"),
    ]
    
    # Set the latest water levels
    stations[0].latest_level = 0.8  # Relative level: 0.6
    stations[1].latest_level = 0.9  # Relative level: 0.8
    stations[2].latest_level = 1.0  # Relative level: 1.0
    stations[3].latest_level = 0.7  # Relative level: 0.4
    stations[4].latest_level = 0.6  # Relative level: 0.2

    # Ensure typical range is consistent
    for station in stations:
        station.typical_range_consistent = lambda: True

    # Test the function with N=3
    result = stations_highest_rel_level(stations, 3)
    expected = [
        ("Station C", 1.0),
        ("Station B", 0.8),
        ("Station A", 0.6)
    ]
    assert result == expected
