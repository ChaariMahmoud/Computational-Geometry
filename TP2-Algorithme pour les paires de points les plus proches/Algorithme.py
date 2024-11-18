import math
import matplotlib.pyplot as plt

# Fonction pour calculer la distance entre deux points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Algorithme pour les paires de points les plus proches
def closest_pair(points):
    def closest_pair_rec(points_sorted_x, points_sorted_y):
        n = len(points_sorted_x)
        if n <= 3:  # Cas de base : brute force
            min_dist = float('inf')
            min_pair = None
            for i in range(n):
                for j in range(i + 1, n):
                    d = distance(points_sorted_x[i], points_sorted_x[j])
                    if d < min_dist:
                        min_dist = d
                        min_pair = (points_sorted_x[i], points_sorted_x[j])
            return min_dist, min_pair

        # Diviser
        mid = n // 2
        left_x = points_sorted_x[:mid]
        right_x = points_sorted_x[mid:]
        mid_x = points_sorted_x[mid][0]

        left_y = [p for p in points_sorted_y if p[0] <= mid_x]
        right_y = [p for p in points_sorted_y if p[0] > mid_x]

        # Résoudre récursivement
        d1, pair1 = closest_pair_rec(left_x, left_y)
        d2, pair2 = closest_pair_rec(right_x, right_y)

        # Le minimum des deux moitiés
        d = min(d1, d2)
        pair = pair1 if d1 <= d2 else pair2

        # Vérification dans la bande centrale
        strip = [p for p in points_sorted_y if abs(p[0] - mid_x) < d]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d_strip = distance(strip[i], strip[j])
                if d_strip < d:
                    d = d_strip
                    pair = (strip[i], strip[j])

        return d, pair

    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(points_sorted_x, points_sorted_y)

# Algorithme pour l'enveloppe convexe
def convex_hull(points):
    # Trouver le point pivot
    pivot = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=lambda p: (math.atan2(p[1] - pivot[1], p[0] - pivot[0]), p[0], p[1]))

    # Construire l'enveloppe avec une pile
    hull = []
    for p in points:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

# Produit vectoriel pour déterminer l'orientation
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Affichage graphique avec matplotlib
def plot_results(points, closest_pair, hull, non_hull_points):
    plt.figure(figsize=(8, 8))
    plt.scatter(*zip(*points), label="Tous les points", color='blue', s=50)

    # Afficher les deux points les plus proches
    p1, p2 = closest_pair
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-', label="Points les plus proches")
    plt.scatter(*zip(*closest_pair), color='red', s=100, zorder=5)

    # Tracer l'enveloppe convexe
    hull_points = hull + [hull[0]]  # Boucler l'enveloppe
    plt.plot(*zip(*hull_points), label="Enveloppe convexe", color='green')

    # Afficher les points qui ne sont pas sur l'enveloppe
    if non_hull_points:
        plt.scatter(*zip(*non_hull_points), label="Points non sur l'enveloppe", color='orange', s=50)

    plt.legend()
    plt.title("Enveloppe convexe et points les plus proches")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# Fonction principale
if __name__ == "__main__":
    print("Entrez les points (x, y) séparés par des espaces. Tapez 'fin' pour terminer.")
    points = []
    while True:
        inp = input("Point : ")
        if inp.lower() == "fin":
            break
        try:
            x, y = map(float, inp.split())
            points.append((x, y))
        except ValueError:
            print("Veuillez entrer deux coordonnées numériques.")

    if len(points) < 2:
        print("Vous avez besoin d'au moins 2 points.")
    else:
        # Paires de points les plus proches
        dist, pair = closest_pair(points)
        print(f"Les deux points les plus proches sont {pair} avec une distance de {dist:.2f}.")

        # Enveloppe convexe
        hull = convex_hull(points)
        non_hull_points = [p for p in points if p not in hull]
        print(f"L'enveloppe convexe contient les points : {hull}.")
        print(f"Les points qui ne sont pas sur l'enveloppe : {non_hull_points}.")

        # Affichage graphique
        plot_results(points, pair, hull, non_hull_points)
