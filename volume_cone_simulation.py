import argparse
import math

def volume_cone_numerical_integration(radius, height, num_segments):
    delta_z = height / num_segments
    volume_estime = 0

    for i in range(num_segments):
        z1 = i * delta_z
        z2 = (i + 1) * delta_z

        # Calculate the areas of the two circular cross-sections at different heights
        area1 = math.pi * (radius * (1 - z1 / height))**2
        area2 = math.pi * (radius * (1 - z2 / height))**2

        # Calculate the volume of the frustum between z1 and z2 and add it to the total volume
        volume_estime += (area1 + area2) * delta_z / 2

    return volume_estime

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("rayon", type=float, help="Rayon de la base du cône")
    parser.add_argument("hauteur", type=float, help="Hauteur du cône")
    parser.add_argument("-n", "--numsegments", type=int, default=1000, help="Nombre de segments pour l'intégration")
    args = parser.parse_args()

    rayon = args.rayon
    hauteur = args.hauteur
    num_segments = args.numsegments

    volume_estime = volume_cone_numerical_integration(rayon, hauteur, num_segments)
    volume_theorique = (1/3) * math.pi * rayon**2 * hauteur

    print("Volume estimé du cône:", volume_estime)
    print("Volume théorique du cône:", volume_theorique)
