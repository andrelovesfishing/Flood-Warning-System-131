from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels


def run():
    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)

    towns_water = {}
    for station in stations:
        current_town = station.town
        water = station.relative_water_level()
        if water is None:
            continue
        if station.town in towns_water:
            if water > towns_water[current_town]:
                towns_water[current_town] = station.relative_water_level()
        else:
            towns_water[current_town] = station.relative_water_level()
    
    towns_risk = {}

    for current_town in towns_water:
        if current_town is None:
            continue
        if towns_water[current_town] > 3:
            towns_risk[current_town] = "Severe"
        elif towns_water[current_town] > 2:
            towns_risk[current_town] = "High"
        elif towns_water[current_town] > 1:
            towns_risk[current_town] = "Medium"
        else:
            towns_risk[current_town] = "Low"
            
    
    queried_risk = input("Which level of risk would you like to view? (Severe/High/Medium/Low)   ")
    valid_responses = ["Severe","High","Medium","Low"]
    if queried_risk in valid_responses:
        pull_towns = [town for town, risk in towns_risk.items() if risk == queried_risk]
        print(pull_towns)
    else:
        print("Error, query invalid")


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
