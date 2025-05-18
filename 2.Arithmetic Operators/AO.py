# TODO 1) Calcule les résultats

x = 19

a = x / 5
b = x % 5
c = x // 5

print(a, b, c)

# TODO 2) Demande à l'utilisateur un nombre à 4 chiffres. Affiche le produit de ces 4 chiffres.
i = int(input("Entrer 4 chiffres"))

a = i // 1000

b = (i % 1000) // 100

c = (i % 100) // 10

d = (i % 10)

e = a * b * c * d

print(e)

# TODO 3) Si tu devais ajouter 1 à l'input de l'utilisateur tout en ne modifiant pas X (refaire 2) ?
