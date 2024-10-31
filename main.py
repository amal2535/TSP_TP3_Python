from tsp.solver import City, TravelingSalesman
import numpy as np

class OptimizedTravelingSalesman(TravelingSalesman):
    def __init__(self, cities, distance_matrix, vehicle_capacity, max_distance, impractical_routes):
        super().__init__(cities, distance_matrix, vehicle_capacity, max_distance, impractical_routes)



    def calculate_route_distance(self, route):
        return sum(self.distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

def main():
    # Définir les villes
    cities = [
        City("A", (0, 0), (0, 10), 5),  # Ville A
        City("B", (1, 1), (2, 12), 2),  # Ville B, demande réduite à 2
        City("C", (2, 2), (3, 15), 2),  # Ville C, demande réduite à 2
        City("D", (3, 3), (5, 20), 2),  # Ville D
    ]

    # Matrice des distances modifiée
    distance_matrix = np.array([[0, 2, 9, float('inf')],
                                 [1, 0, 6, 4],
                                 [float('inf'), 7, 0, 8],
                                 [6, float('inf'), 3, 0]])

    vehicle_capacity = 10
    max_distance = 20  # Ajuster la distance maximale si nécessaire
    impractical_routes = [(0, 2), (2, 3)]  # Routes impraticables

    tsp = OptimizedTravelingSalesman(cities, distance_matrix, vehicle_capacity, max_distance, impractical_routes)
    best_route, min_distance = tsp.find_best_route()

    if best_route is not None:
        print("Meilleur chemin:", [cities[i].name for i in best_route], "Distance:", min_distance)
    else:
        print("Aucune route valide trouvée.")

if __name__ == "__main__":
    main()