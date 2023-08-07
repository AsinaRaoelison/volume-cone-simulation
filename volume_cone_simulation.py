import random
import argparse
import math

def volume_cone_simulation(radius, height, n_simulations):
    volume_theorique = (1/3) * math.pi * radius**2 * height
    volume_estime = 0

    for _ in range(n_simulations):
        x = random.uniform(0, radius)  # Génération aléatoire des coordonnées x, y, z dans le cube  43d5cdd4e3a0fbcf264fea1da9754c30
        y = random.uniform(0, radius)
        z = random.uniform(0, height)

        # Vérifier si le point est à l'intérieur du cône en comparant avec l'équation du cône
        if z <= (height / radius) * math.sqrt(x**2 + y**2):
            volume_estime += 1

    volume_estime = volume_estime / n_simulations * (radius ** 2) * height

    return volume_estime, volume_theorique

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("rayon", type=float, help="Rayon de la base du cône")
    parser.add_argument("hauteur", type=float, help="Hauteur du cône")
    parser.add_argument("-n", "--nbsimul", type=int, default=10000, help="Nombre de simulations")
    args = parser.parse_args()

    rayon = args.rayon
    hauteur = args.hauteur
    n_simulations = args.nbsimul

    volume_estime, volume_theorique = volume_cone_simulation(rayon, hauteur, n_simulations)

    print("Volume estimé du cône:", volume_estime)
    print("Volume théorique du cône:", volume_theorique)
