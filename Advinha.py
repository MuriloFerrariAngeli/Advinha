from random import randint

#sortear um número de 1 a 10
sorteado = randint(1, 10)
    
    
#inicializar 3 vidas
vidas = 3

#loop infinito 
while True:
    #palpite do usuário
    palpite = int(input('Digite um número: '))
    
    if palpite > 10:
        print('Número inválido, por favor escreva de 1 à 10')
        
    #palpite igual o sorteado, usuário ganhou
    if palpite == sorteado:
        print('Acertou')
        break

    #palpite menor que o sorteado, mensagem:
    if palpite < sorteado:
        print('Muito baixo')
    #palpite maior que o sorteado, mensagem:
    elif palpite > sorteado:
        print('Muito Alto')

    #não acertou, desconta uma vida
    vidas -= 1

    #acabou as vidas. o usuário perde
    if vidas == 0:
        print('Você perdeu.')
        break