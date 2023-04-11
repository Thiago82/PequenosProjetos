### JANKENPON ###

import random

print("*** JAKENPON ***")
print("Escolha Pedra, Papel, ou Tesoura, e tente vencer o computador!")

player_ponto = 0
cpu_ponto = 0

options = ["pedra", "papel", "tesoura"]


while True:
    usuario_input = input("Digite sua escolha: ").lower()
    if usuario_input not in options:
        continue

    num_random = random.randint(0, 2) # Pedra: 0, Papel: 1, Tesoura: 2
    cpu_choice = options[num_random]
    print("Computador escolheu", cpu_choice + ".")

    if usuario_input == "pedra" and cpu_choice == "tesoura":
        print("Você venceu!")
        player_ponto += 1

    elif usuario_input == "papel" and cpu_choice == "pedra":
        print("Você venceu!")
        player_ponto += 1

    elif usuario_input == "tesoura" and cpu_choice == "papel":
        print("Você venceu!")
        player_ponto += 1

    elif usuario_input == cpu_choice:
        print("Empate!")
        player_ponto += 0

    else:
        print("Você perdeu!")
        cpu_ponto += 1

print("Você fez", player_ponto, "pontos.")
print("O computador fez", cpu_ponto, "pontos." )
print("Até a próxima!")