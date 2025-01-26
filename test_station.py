# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    # Create a consistent station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    station1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create an inconsistent station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, -2.4)
    river = "River X"
    town = "My Town"
    station2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create an station with lacking data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    station3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert station1.typical_range_consistent() == True
    assert station2.typical_range_consistent() == False
    assert station3.typical_range_consistent() == False

def test_less_than():
    # Create a station with an alphabetically lower ranked name
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "adrian"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    station1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station with an alphabetically lower ranked name
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "jamal"
    coord = (-2.0, 4.0)
    trange = (-2.3, -2.4)
    river = "River X"
    town = "My Town"
    station2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert station1 < station2

test_typical_range_consistent()
test_less_than()