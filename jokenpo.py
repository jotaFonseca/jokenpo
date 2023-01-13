from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
continuar = ''
while True:
    print('''Opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('Qual a sua jogada irmão? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    if computador == 0: #computador jogou PEDRA
        if jogador == 0:
            print('-=' * 15)
            print('Nem eu e nem tu parça')
            print(f'Eu fui de {itens[computador]} também')
            print('-=' * 15)
        elif jogador == 1:
            print('-=' * 15)
            print('Merda, tu ganhou...')
            print(f'O estúpido aqui jogou {itens[computador]}')
            print('-=' * 15)
        elif jogador == 2:
            print('-=' * 15)
            print('GANHEI DE TU SEU PUTO HAHAHAH')
            print(f'O PAI FOI DE {itens[computador]} GARAI')
            print('-=' * 15)
        else:
            print('TU É BURRO DOIDÃO? JOGADA INVÁLIDA!')

    elif computador == 1: #computador jogou PAPEL
        if jogador == 0:
            print('-=' * 15)
            print('GANHEI DE TU SEU PUTO HAHAHAH')
            print(f'O PAI FOI DE {itens[computador]} GARAI')
            print('-=' * 15)
        elif jogador == 1:
            print('-=' * 15)
            print('Nem eu e nem tu parça')
            print(f'Eu fui de {itens[computador]} também')
            print('-=' * 15)
        elif jogador == 2:
            print('-=' * 15)
            print('Merda, tu ganhou...')
            print(f'O estúpido aqui jogou {itens[computador]}')
            print('-=' * 15)
        else:
            print('TU É BURRO DOIDÃO? JOGADA INVÁLIDA!')

    elif computador == 2: #computador jogou TESOURA
        if jogador == 0:
            print('-=' * 15)
            print('Merda, tu ganhou...')
            print(f'O estúpido aqui jogou {itens[computador]}')
            print('-=' * 15)
        elif jogador == 1:
            print('-=' * 15)
            print('GANHEI DE TU SEU PUTO HAHAHAH')
            print(f'O PAI FOI DE {itens[computador]} GARAI')
            print('-=' * 15)
        elif jogador == 2:
            print('-=' * 15)
            print('Nem eu e nem tu parça')
            print(f'Eu fui de {itens[computador]} também')
            print('-=' * 15)
        else:
            print('TU É BURRO DOIDÃO? JOGADA INVÁLIDA!')
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if continuar in 'Ss':
        continue
    elif continuar in 'Nn':
        break
print('Jogo finalizado!')
