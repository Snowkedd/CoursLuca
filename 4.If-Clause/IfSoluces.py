print("-TODO 1-")
x = int(input("Entrez un nombre à 3 chiffres: "))

c = x // 100
d = (x % 100) // 10
u = x % 10

if c == u:
    print(c)
else:
    is_armstrong = x == c**3 + d**3 + u**3
    print(is_armstrong)