import unittest
import numpy as np
from tsp.solver import City, TravelingSalesman

class TestTravelingSalesman(unittest.TestCase):
    def setUp(self):
        self.cities = [
            City("A", (0, 0), (0, 10), 4),
            City("B", (1, 1), (2, 12), 2),
            City("C", (2, 2), (3, 15), 2),
            City("D", (3, 3), (5, 20), 2),
        ]
        
        self.distance_matrix = np.array([[0, 2, 9, float('inf')],
                                         [1, 0, 6, 4],
                                         [float('inf'), 7, 0, 8],
                                         [6, float('inf'), 3, 0]])
        
        self.vehicle_capacity = 10
        self.max_distance = 50
        self.impractical_routes = [(0, 2), (2, 3)]
        self.tsp = TravelingSalesman(self.cities, self.distance_matrix, self.vehicle_capacity, self.max_distance, self.impractical_routes)

    def test_is_route_valid(self):
        self.assertTrue(self.tsp.is_route_valid([0, 1, 3]))  # Example valid route
        self.assertFalse(self.tsp.is_route_valid([0, 2, 3]))  # Example invalid route due to impractical route

    def test_calculate_distance(self):
        route = [0, 1, 3]
        calculated_distance = self.tsp.calculate_distance(route)
        print(f"Calculated distance for route {route}: {calculated_distance}")
        self.assertEqual(calculated_distance, 12)  # Expected distance based on matrix

    def test_find_best_route(self):
        best_route, min_distance = self.tsp.find_best_route()
        print(f"Best route: {best_route}, Minimum distance: {min_distance}")
        self.assertEqual(min_distance, 22)  # Assuming this is the correct minimal distance

if __name__ == '__main__':
    unittest.main()
