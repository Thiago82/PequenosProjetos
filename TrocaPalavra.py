## TROCA PALAVRA ##


def trocaPalavra():

    str = "Olá, eu gosto de comida, mas não gosto de dieta"
    print(str)
    palavra_antiga = input("Qual palavra quer trocar?: ")
    palavra_nova = input("Qual a nova palavra?: ")
    print(str.replace(palavra_antiga, palavra_nova))

trocaPalavra()