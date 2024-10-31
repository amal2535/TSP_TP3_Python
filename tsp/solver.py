import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt

class City:
    def __init__(self, name, coordinates, open_time, demand):
        self.name = name
        self.coordinates = coordinates  
        self.open_time = open_time  
        self.demand = demand  
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
        
        for i in range(len(route) - 1):
            if (route[i], route[i + 1]) in self.impractical_routes:
                print(f"Route {route} invalide: route impraticable de {route[i]} à {route[i + 1]}.")
                return False
        
        return True

    def find_best_route(self):
        all_routes = permutations(range(len(self.cities)))
        valid_routes = []
        
        for route in all_routes:
            if self.is_route_valid(route):
                valid_routes.append(route)
        
        if valid_routes:
            best_route = min(valid_routes, key=lambda r: self.calculate_distance(r))
            return best_route, self.calculate_distance(best_route)
        else:
            return None, None

    def calculate_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distance_matrix[route[i], route[i + 1]]
        distance += self.distance_matrix[route[-1], route[0]]  
        return distance

def plot_route(cities, best_route):
    # Extract coordinates in order of the best route
    x = [cities[i].coordinates[0] for i in best_route] + [cities[best_route[0]].coordinates[0]]
    y = [cities[i].coordinates[1] for i in best_route] + [cities[best_route[0]].coordinates[1]]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', color='b')
    plt.title("Meilleur chemin du TSP")
    plt.xlabel("Coordonnées X")
    plt.ylabel("Coordonnées Y")

    # Annotate cities
    for i, city in enumerate(best_route):
        plt.annotate(cities[city].name, (cities[city].coordinates[0], cities[city].coordinates[1]),
                     textcoords="offset points", xytext=(0, 10), ha='center')

    plt.grid()
    plt.axis('equal')  # Ensure equal scaling
    plt.show()