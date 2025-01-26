from floodsystem.geo import haversine1
from haversine import haversine

def test_haversine1():
    given = haversine1((52.2053, 0.1218), (50.0, 25.0))
    answer = haversine((52.2053, 0.1218), (50.0, 25.0))
    assert given == answer
