# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
numero = int(input("Fatorial de: ") )

fat = 1

for i in range (1, numero+1):
    fat*= i
print(f"o resultado de {numero}!: {fat}")