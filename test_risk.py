import pytest

def test_town_risk_levels():
    # Mock data for towns and their water levels
    towns_water = {
        "Town A": 3.5,
        "Town B": 2.5,
        "Town C": 1.5,
        "Town D": 0.5,
    }
    
    # Expected risk levels
    expected_risk_levels = {
        "Town A": "Severe",
        "Town B": "High",
        "Town C": "Medium",
        "Town D": "Low",
    }
    
    # Calculate risk levels
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
    
    # Print the actual calculated risk levels to inspect any discrepancies
    print(f"Calculated towns_risk: {towns_risk}")
    
    # Assert that the calculated risk levels match the expected risk levels
    assert towns_risk == expected_risk_levels, f"Expected {expected_risk_levels}, but got {towns_risk}"

# To run the test using pytest
if __name__ == "__main__":
    pytest.main()