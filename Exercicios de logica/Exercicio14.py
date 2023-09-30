print('Escreva um algoritmo para ler uma temperatura em Fahrenheit, calcular e converter para graus Celsius')
print('-------------------------------------------------------------------------------------------------------')

fahrenheit = float (input('Digite a temperatura em Fahrenheit: '))
celsius = ((fahrenheit - 32) / 9) * 5

print(f'A temperatura em graus Celsius é {celsius}')