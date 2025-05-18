print("-TODO 1-")
x = int(input("Entrez un nombre supérieur à 2: "))

n_2 = 0
n_1 = 1
print(n_2, end=" ")
print(n_1, end=" ")

for i in range(2, x):
    sum = n_1 + n_2
    print(sum, end=" ")
    n_2 = n_1
    n_1 = sum
