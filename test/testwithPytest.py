import pytest
import numpy as np
from tsp.solver import City, TravelingSalesman

@pytest.fixture
def setup_tsp():
    cities = [
        City("A", (0, 0), (0, 10), 4),  
        City("B", (1, 1), (2, 12), 2),  
        City("C", (2, 2), (3, 15), 2),  
        City("D", (3, 3), (5, 20), 2),  
    ]
    distance_matrix = np.array([
        [0, 2, 9, float('inf')],
        [1, 0, 6, 4],
        [float('inf'), 7, 0, 8],
        [6, float('inf'), 3, 0]
    ])
    vehicle_capacity = 10
    max_distance = 50
    impractical_routes = [(0, 2), (2, 3)]
    return TravelingSalesman(cities, distance_matrix, vehicle_capacity, max_distance, impractical_routes)

def test_is_route_valid(setup_tsp):
    tsp = setup_tsp
    assert tsp.is_route_valid([0, 1, 3, 2]) == True
    assert tsp.is_route_valid([0, 1, 2, 3]) == False
    assert tsp.is_route_valid([0, 2, 3, 1]) == False

def test_calculate_distance(setup_tsp):
    tsp = setup_tsp
    route = [0, 1, 3, 2]
    assert tsp.calculate_distance(route) == 20  # Expected based on the matrix

def test_find_best_route(setup_tsp):
    tsp = setup_tsp
    best_route, min_distance = tsp.find_best_route()
    assert best_route is not None
    assert min_distance == 20
