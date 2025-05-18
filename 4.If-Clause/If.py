# TODO 1) Demande à l'utilisateur un nombre de 3 chiffres. Si c'est un palindrome, affiche le chiffre qui apparait le
#  plus de fois, sinon, vérifie si le nombre est un armstrong number.
i = int(input("Entrer 3 chiffres"))

a = i // 100

b = (i%100) // 10

c = i % 10

if a == c:
    print("C'est un palindrome")
    print(a, "c'est le chiffre qui apparaît le plus de foi")

else:
    armstrong = a**3 + b**3 + c**3 == i
    print(armstrong)
