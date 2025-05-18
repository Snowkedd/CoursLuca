# TODO Contexte de l'exo : petit programme de gestion de patients d'hôpital.
#  1) Trouver un moyen d'enregistrer de nouveaux patients. Besoin de => nom, âge, taille, poids.


# TODO 2) Faire une fonction qui donne le min, le max et la moyenne d'une des métriques précédentes
#  (sauf le nom). Afficher aussi le nombre de données et arrondir la moyenne à 2 décimales.


# TODO 3) Faire une fonction qui supprime un client (toutes ses infos)


panier_de_fruits = []

def ajouter_un_fruit(panier_de_fruits, un_fruit):
    panier_de_fruits.append(un_fruit)
    return panier_de_fruits

print(panier_de_fruits)
panier_de_fruits= ajouter_un_fruit(panier_de_fruits, "Orange")
print(panier_de_fruits)