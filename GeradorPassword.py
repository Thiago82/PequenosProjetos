### GERADOR PASSWORD ###

import random
import string

def geraPassword(pswrd_size, numeros=True, special_caracteres=True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    caracteres = letters
    if numeros:
        caracteres += digits
    if special_caracteres:
        caracteres += punctuation

    pswrd = ""
    criterio_OK = False
    tem_numero = False
    tem_punctuation = False

    while not criterio_OK or len(pswrd) < pswrd_size:
        novo_caractere = random.choice(caracteres)
        pswrd += novo_caractere

        if novo_caractere in digits:
            tem_numero = True
        elif novo_caractere in punctuation:
            tem_punctuation = True

        criterio_OK = True
        if numeros:
            criterio_OK = tem_numero
        if special_caracteres:
            criterio_OK = criterio_OK and tem_punctuation

    return pswrd


pswrd_size = int(input("Tamanho minimo: "))
tem_numero = input("Quer numeros(y/n)? ").lower() == "y"
tem_punctuation = input("Quer caracteres especiais(y/n)? ").lower() == "y"
pswrd = geraPassword(pswrd_size, tem_numero, tem_punctuation)
print("A password é:", pswrd)