### ACERTE O NUMERO ###

import random

num_input = input("Tente adivinhar o número de 0 a 10: ")

if num_input.isdigit():
    num_input = int(num_input)

    if num_input <= 0:
        print("Por favor, escolha um número de 0 a 10.")

else:
    print("Por favor, digite apenas números.")

num_random = random.randint(0, num_input)
num_tentativa = 0

while True:
    num_tentativa += 1
    tentativa = input("Tente novamente: ")

    if tentativa.isdigit():
        tentativa = int(tentativa)

    else:
        print("Por favor, digite apenas números.")
        continue

    if tentativa == num_random:
        print("Você acertou!")
        break

    elif tentativa > num_random:
        print("Muito alto!")

    else:
        print("Muito baixo!")

print("Você acertou na", num_tentativa, "º tentativa.")