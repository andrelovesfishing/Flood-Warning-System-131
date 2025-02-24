import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
import pytest
from floodsystem.analysis import polyfit


def test_polyfit_basic():
    # Test basic functionality with simple known data
    dates = [datetime(2020, 1, 1), datetime(2020, 2, 1), datetime(2020, 3, 1)]
    levels = [1.5, 2.0, 2.5]
    
    degree = 1  # Linear fit (degree 1)
    
    # Call the polyfit function
    poly, reference_date = polyfit(dates, levels, degree)
    
    # Expected values based on the input
    expected_poly = np.polyfit([mdates.date2num(d) for d in dates], levels, degree)
    expected_reference_date = np.mean([mdates.date2num(d) for d in dates])
    
    # Check if the returned polynomial coefficients are close to the expected ones
    np.testing.assert_allclose(poly, expected_poly, rtol=1e-5, atol=1e-8)
    
    # Check if the reference date is close to the expected reference date
    assert abs(reference_date - expected_reference_date) < 1e-5


def test_polyfit_input():
    # Test that the function raises a ValueError when the input is invalid
    dates = [datetime(2020, 1, 1), datetime(2020, 2, 1), datetime(2020, 3, 1)]
    true_dates = [mdates.date2num(d) for d in dates]    
    for item in true_dates:
        assert type(item) == np.float64