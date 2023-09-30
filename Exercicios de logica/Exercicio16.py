print('Escreva um algoritmo para ler a hora de inicio \n'
      'e a hora de fim de um jogo de xadrez e calcule\n'
      'e calcule a duração do jogo em horas, sabendo-se que \n'
      'o tempo máximo de duração dp jogo é de 24 horas e  que o jogo pode iniciar\n'
      'em um dia e terminar no dia seguinte.')
print('---------------------------------------------------------------------------------')

horainicio = int(input("Digite a hora de início do jogo: "))
horafim = int(input("Digite a hora de fim do jogo: "))


if horainicio > horafim:
    duracao = (24 - horainicio) + horafim
else:
    duracao = horafim - horainicio

print(f"A duração do jogo foi de {duracao} horas.")