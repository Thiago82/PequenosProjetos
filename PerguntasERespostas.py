### PERGUNTAS E RESPOSTAS ###

print("Bem vindo ao nosso Quiz!")
#print("Responda as perguntas apenas com letras minúsculas!")

jogando = input("Iniciar jogo?\nResponda sim ou não: ")

if jogando.lower() != "sim":
    quit()

print("Ok, vamos começar as perguntas!")
print("Cada resposta correta vale 2 pontos.")
print("Tente acertar 100% das perguntas!")

ponto = 0

pergunta = input("O que significa a sigla HD? ")
if pergunta.lower() == "hard disk":
    print("Resposta correta!")
    ponto += 2
else:
    print("Você errou.")
    print("Vamos para a próxima pergunta.")


pergunta = input("O que significa a sigla RAM? ")
if pergunta.lower() == "random access memory":
    print("Resposta correta!")
    ponto += 2
else:
    print("Você errou.")
    print("Vamos para a próxima pergunta.")


pergunta = input("Em que ano foi fundada a IBM? ")
if pergunta.lower() == "1911":
    print("Resposta correta!")
    ponto += 2
else:
    print("Você errou.")
    print("Vamos para a próxima pergunta.")


pergunta = input("Qual empresa americana ajudou a criar o MSX? ")
if pergunta.lower() == "microsoft":
    print("Resposta correta!")
    ponto += 2
else:
    print("Você errou.")
    print("Vamos para a próxima pergunta.")

pergunta = input("Qual a tradução  de joystick? ")
if pergunta.lower() == "vara da alegria":
    print("Resposta correta!")
    ponto += 2
else:
    print("Você errou.")


print("Você fez " + str(ponto) + " pontos!")
print("Acertou " + str((ponto / 5) * 50) + " % das perguntas!")