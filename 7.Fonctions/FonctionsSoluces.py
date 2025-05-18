# TODO Contexte de l'exo : petit programme de gestion de patients d'hôpital.
#  1) Trouver un moyen d'enregistrer de nouveaux patients. Besoin de => nom, âge, taille, poids.
names = []
ages = []
heights = []
weights = []


def add_new_patient(name, age, height, weight):
    names.append(name)
    ages.append(age)
    heights.append(height)
    weights.append(weight)


# TODO 2) Faire une fonction qui donne le min, le max et la moyenne d'une des métriques précédentes
#  (sauf le nom)

def statistics(metric):
    print("Number of metrics ", len(metric))
    print("Min: ", min(metric))
    print("Max: ", max(metric))
    print("Avg: ", round(sum(metric) / len(metric), 2))


# TODO 3) Faire une fonction qui supprime un client (toutes ses infos)
def remove_patient(name):
    id_patient = names.index(name)
    names.pop(id_patient)
    ages.pop(id_patient)
    heights.pop(id_patient)
    weights.pop(id_patient)


add_new_patient("Maxim", 26, 177, 80)
add_new_patient("Charline", 22, 153, 50)
add_new_patient("Solène", 25, 161, 48)

statistics(ages)
remove_patient("Maxim")
statistics(ages)
