from random import randint
from time import sleep
from getpass import getpass

item = ('Pedra','Papel','Tesoura')
alt = player1 = player2 = None
p1_score = p2_score = 0
while True:
    
    if alt == None:
        print('Pressione 0 para Jogar com o computador')
        print('Pressione 1 para Jogar com um amigo')
        alt = input()
        try:
            alt = int(alt)
            if alt < 0 or alt > 1:
                raise ValueError
        except:
            alt = None
            print('* Digite um número entre 0 e 1')
            continue
        if alt == 1:
            player1 = input('Jogador 1: Escreva seu nome ')
            player2 = input('Jogador 2: Escreva seu nome ')
        else:
            player1 = 'Jogador'
            player2 = 'Computador'
    print('''--------------------
Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    [i] Informações
--------------------''')
    p1_chosen = getpass('Jogador 1: Faça sua jogada ') if alt == 1 else input('Qual a sua jogada? ')
    if p1_chosen == "i":
      print('='*20,
        '\nScore: \n',
        player1 + ' ' + str(p1_score) + ' pontos\n',
        player2 + ' ' + str(p2_score) + ' pontos',
        '\n'+'='*20
      )
      getpass('Aperte Enter para continuar...')
      continue
    p2_chosen = getpass('Jogador 2: Faça sua jogada ') if alt == 1 else randint(0,2)
    
    try:
        p1_chosen = int(p1_chosen)
        p2_chosen = int(p2_chosen)
        if p1_chosen > 2 or p1_chosen < 0 or p2_chosen > 2 or p2_chosen < 0:
            raise ValueError
    except:
        print('* escolha um número entre 0 e 2 *')
        continue
    print('='*20)
    print('\rJO', end='')
    sleep(1)
    print('\rJO-KEN', end='')
    sleep(1)
    print('\rJO-KEN-PÔ ')
    sleep(0.5)
    print('-'*20)
    print(player2 + ' escolheu {}'.format(item[p2_chosen]))
    print(player1 + ' escolheu {}'.format(item[p1_chosen]))
    print('-'*20)
    sleep(0.5)
    if p2_chosen == p1_chosen:
        win=0
        print('EMPATE!')
    elif ((p2_chosen - p1_chosen) == 1 or (p2_chosen == 0 and p1_chosen == 2)):
        win=0
        p2_score += 1
        print(player2 + ' Venceu!')
    else:
        win=1
        p1_score += 1
        print(player1 + ' Venceu!')
    print('='*20)
    sleep(2)
    if alt == 1:
        win = 2
    print(('TENTE OUTRA VEZ!','PROVE QUE NÃO FOI SORTE, JOGUE OUTRA!','JOGUEM NOVAMENTE!')[win])
    sleep(1)
