from tsp.solver import City, TravelingSalesman
import numpy as np

def print_distance_matrix(cities, distance_matrix):
    print("Matrice des distances:")
    print("    " + "   ".join(city.name for city in cities)) 
    for i, row in enumerate(distance_matrix):
        print(f"{cities[i].name} ", end="")
        for distance in row:
            if distance == float('inf'):
                print("inf ", end="")
            else:
                print(f"{distance:3} ", end="")
        print() 

def main():
    cities = [
        City("A", (0, 0), (0, 10), 4),  # City A
        City("B", (1, 1), (2, 12), 2),  # City B
        City("C", (2, 2), (3, 15), 2),  # City C
        City("D", (3, 3), (5, 20), 2),  # City D
    ]
    
    # Distance matrix remains the same
    distance_matrix = np.array([[0, 2, 9, float('inf')],
                                 [1, 0, 6, 4],
                                 [float('inf'), 7, 0, 8],
                                 [6, float('inf'), 3, 0]])


    vehicle_capacity = 10
    max_distance = 20  
    impractical_routes = [(0, 2), (2, 3)]  

    # Print the distance matrix
    print_distance_matrix(cities, distance_matrix)

    tsp = TravelingSalesman(cities, distance_matrix, vehicle_capacity, max_distance, impractical_routes)
    best_route, min_distance = tsp.find_best_route()

    if best_route is not None:
        print("Meilleur chemin:", [cities[i].name for i in best_route], "Distance:", min_distance)
    else:
        print("Aucune route valide trouvée.")

if __name__ == "__main__":
    main()
