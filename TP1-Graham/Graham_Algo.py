import math
import matplotlib.pyplot as plt

def listPoint(n):
    pts = []
    for i in range(n):
        try:
            x = float(input(f"Donner l'abscisse du point p{i} : "))
            y = float(input(f"Donner l'ordonnée du point p{i} : "))
            pts.append([x, y])
        except ValueError:
            print("Veuillez entrer des nombres valides.")
            return listPoint(n)  # Relancer si les entrées ne sont pas valides
    return pts

# Soit Pb le point le plus bas.
def trouverPtPlusBas(pts):
    pb = pts[0]
    for pt in pts:
        if pt[1] < pb[1] or (pt[1] == pb[1] and pt[0] < pb[0]):
            pb = pt
    return pb


# Calculer l'angle entre le point et la ligne horizontale
#Trouver le vecteur directeur d'une droite à partir de deux de ses points :
# vecteur u = vecteur AB 
#xu = xB - xA
#yu = yB - yA
def angleAvecHorizontale(pt1, pt2):
    return math.atan2(pt2[1] - pt1[1], pt2[0] - pt1[0])

# Tri des points par rapport à l'angle et à l'abscisse
def trierPoints(pts, pb):
    # Fonction pour calculer la distance au carré d'un point à pb
    def distanceCarree(pt1, pt2):
        return (pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2

    # Trier les points par angle, puis par distance décroissante en cas d'égalité d'angles
    pts.sort(key=lambda pt: (angleAvecHorizontale(pb, pt), -distanceCarree(pb, pt)))
    return pts

# Fonction pour vérifier la direction (gauche ou droite)
def direction(pt1, pt2, pt3):
    return (pt2[0] - pt1[0]) * (pt3[1] - pt1[1]) - (pt2[1] - pt1[1]) * (pt3[0] - pt1[0])

# Algorithme de balayage de Graham pour construire l'enveloppe convexe
def enveloppeConvexe(pts):
    if len(pts) < 3:
        print("Il faut au moins 3 points pour former une enveloppe convexe.")
        return []

    pb = trouverPtPlusBas(pts)
    pts = trierPoints(pts, pb)
    
    # Pile pour l'enveloppe convexe
    pile = [pts[0], pts[1]]

    for pt in pts[2:]:
        while len(pile) > 1 and direction(pile[-2], pile[-1], pt) < 0:
            pile.pop()  # Retirer le dernier point de la pile
        pile.append(pt)  # Ajouter le point courant à la pile

    return pile


# Fonction pour afficher les points et l'enveloppe convexe
def afficherEnveloppe(points, enveloppe):
    # Extraire les coordonnées x et y de tous les points
    x_points = [p[0] for p in points]
    y_points = [p[1] for p in points]

    # Extraire les coordonnées x et y de l'enveloppe convexe
    x_enveloppe = [p[0] for p in enveloppe] + [enveloppe[0][0]]  # Boucler sur le premier point pour fermer l'enveloppe
    y_enveloppe = [p[1] for p in enveloppe] + [enveloppe[0][1]]  # Boucler sur le premier point

    # Créer le tracé des points
    plt.scatter(x_points, y_points, color='blue', label='Points')

    # Tracer l'enveloppe convexe
    plt.plot(x_enveloppe, y_enveloppe, color='red', label='Enveloppe Convexe')

    # Mettre en évidence les points de l'enveloppe convexe
    plt.scatter(x_enveloppe, y_enveloppe, color='green', label='Points Enveloppe')

    # Annoter les points
    for i, txt in enumerate(points):
        plt.annotate(f'{i+1}', (x_points[i], y_points[i]), textcoords="offset points", xytext=(5,-5), ha='center')

    # Ajouter le titre et les légendes
    plt.title("Enveloppe Convexe par l'Algorithme de Balayage de Graham")
    plt.xlabel("Abscisse (x)")
    plt.ylabel("Ordonnée (y)")
    plt.legend()
    plt.grid()
    plt.show()

# Exemple d'utilisation
n = int(input("Combien de points voulez-vous entrer ? "))
if n >= 3:
    points = listPoint(n)
    enveloppe = enveloppeConvexe(points)

    if enveloppe:
        print("Les points de l'enveloppe convexe sont :")
        for p in enveloppe:
            print(f"Point : {p}")
    
        # Affichage de l'enveloppe convexe
        afficherEnveloppe(points, enveloppe)
else:
    print("Le nombre de points doit être au moins 3 pour calculer l'enveloppe convexe.")