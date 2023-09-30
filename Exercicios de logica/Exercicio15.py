print('Escreva um algoritmo para ler dois valores e escreve-los em ordem crescente')
print('------------------------------------------------------------------------------')

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor diferente do primeiro: "))


while valor1 == valor2:
    print("Os valores são iguais. Insira valores diferentes.")
    valor2 = float(input("Digite o segundo valor diferente do primeiro: "))


if valor1 > valor2:
    print(f"Valores em ordem crescente: {valor2}, {valor1}")
else:
    print(f"Valores em ordem crescente: {valor2}, {valor1}")
