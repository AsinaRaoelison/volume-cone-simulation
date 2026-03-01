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

# Assign values directly for notebook execution
rayon = 5.0  # Example radius
hauteur = 10.0 # Example height
num_segments = 1000 # Example number of segments

volume_estime = volume_cone_numerical_integration(rayon, hauteur, num_segments)
volume_theorique = (1/3) * math.pi * rayon**2 * hauteur

print("Volume estimé du cône:", volume_estime)
print("Volume théorique du cône:", volume_theorique)
