import string
import random

letras_minusculas = string.ascii_lowercase
letras_maiusculas = string.ascii_uppercase
numeros = string.digits
caracteres_especiais = string.punctuation

todos_caracteres = letras_minusculas + letras_maiusculas + numeros + caracteres_especiais
tamanho = 18

continua = "S"
while continua == "S":
    senha = "".join(random.sample(todos_caracteres, tamanho))
    print(f"Sua senha é: {senha}")

    continua = str(input("Deseja gerar outras senha s/n: ")).upper()