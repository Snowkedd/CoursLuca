# TODO 1) Complète

dents_propres = True
petit_dej_fini = True
est_en_retard = False

la_journée_peut_commencer = dents_propres and petit_dej_fini and not est_en_retard

print(la_journée_peut_commencer)


# TODO 2) Demande X à l'utilisateur. Vérifie si le nombre est divisible par 2 et par 3 ou qu'il est divisible par 2
#  mais pas par 10
#  Test avec 6 (true), 20 (true), 16 (false)
i = int(input("Nombre"))

divisible_par_2 = i%2 == 0
divisible_par_3 = i%3 == 0
pas_divisible_par_10 = i%10 >= 1

print((divisible_par_2 and divisible_par_3) or (divisible_par_2 and pas_divisible_par_10))


