import math


def surface_volume_sphere(rayon):
    rayon = float(rayon)
    surface = 4*math.pi*rayon**2
    return surface, surface*rayon/3


surface, volume = surface_volume_sphere((input("Donnez le rayon : ")))

print(f"Surface en [m2] : {surface:.2f}, Volume en [m3] : {volume:.2f}")
