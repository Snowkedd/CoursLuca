# TODO 2
print("-TODO 2-")
x = input("Entrez un nombre à 4 chiffres: ")

m = int(x) // 1000
c = (int(x) % 1000) // 100
d = (int(x) % 100) // 10
u = int(x) % 10

print(m * c * d * u)

# TODO 3
print("-TODO 3-")
y = int(x)
y += 1

m = y // 1000
c = (y % 1000) // 100
d = (y % 100) // 10
u = y % 10

print(m * c * d * u)
