print(' Escreva um codigo que leia o numero total de eleitores, considerando votos em branco, nulos e válidos.\n'
      'Em seguida calcule e escreva o precentual de cada um.')
print('--------------------------------------------------------------------------------------------------------')

totaleleitores = int (input('Digite o total de eleitores: '))
votosembranco = int (input('Digite o total de votos brancos: '))
votosnulos = int (input('Digite o total de votos nulos: '))
votosvalidos = int (input('Digite o total de votos validos: '))

percbrancos = (votosvalidos / totaleleitores) * 100
percnulos  = (votosnulos / totaleleitores) * 100
percvalidos = (votosvalidos / totaleleitores) * 100

print(f'O percentual de votos brancos foi de: {percbrancos:.2f}%')
print(f'O percentual de votos nulos foi de: {percnulos:.2f}%')
print(f'O percentual de votos validos foi de: {percvalidos:.2f}%')