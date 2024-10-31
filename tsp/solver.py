import numpy as np
from itertools import permutations

class City:
    def __init__(self, name, coordinates, open_time, demand):
        self.name = name
        self.coordinates = coordinates  # (x, y)
        self.open_time = open_time  # (opening_hour, closing_hour)
        self.demand = demand  # Demand for goods
class TravelingSalesman:
    def __init__(self, cities, distance_matrix, vehicle_capacity, max_distance, impractical_routes):
        self.cities = cities
        self.distance_matrix = distance_matrix
        self.vehicle_capacity = vehicle_capacity
        self.max_distance = max_distance
        self.impractical_routes = impractical_routes

    def is_route_valid(self, route):
        total_demand = sum(self.cities[i].demand for i in route)
        if total_demand > self.vehicle_capacity:
            print(f"Route {route} invalide: demande totale {total_demand} > capacité {self.vehicle_capacity}.")
            return False
        
        # Additional checks for impractical routes
        for i in range(len(route) - 1):
            if (route[i], route[i + 1]) in self.impractical_routes:
                print(f"Route {route} invalide: route impraticable de {route[i]} à {route[i + 1]}.")
                return False
        
        return True

    def find_best_route(self):
        # Implement your route finding logic
        all_routes = permutations(range(len(self.cities)))
        valid_routes = []
        
        for route in all_routes:
            if self.is_route_valid(route):
                valid_routes.append(route)
        
        # Proceed with your best route logic
        if valid_routes:
            # Replace this with your actual distance calculation
            best_route = min(valid_routes, key=lambda r: self.calculate_distance(r))
            return best_route, self.calculate_distance(best_route)
        else:
            return None, None

    def calculate_distance(self, route):
        # Implement distance calculation based on the distance matrix
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distance_matrix[route[i], route[i + 1]]
        distance += self.distance_matrix[route[-1], route[0]]  # Return to start
        return distance
