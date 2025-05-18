# TODO 1)
print("-TODO 1-")
dents_propres = True
petit_dej_fini = True
est_en_retard = False

la_journée_peut_commencer = dents_propres and petit_dej_fini and not est_en_retard

print(la_journée_peut_commencer)

# TODO 2)
print("-TODO 2-")
x = int(input("Entrez un nombre"))

exo = (x % 2 == 0 and x % 3 == 0) or (x % 2 == 0 and not x % 10 == 0)

print(exo)
