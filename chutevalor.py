import random
import cowsay

n = random.randint(1, 100)
cowsay.cow('Em que número estou pensando??')
yournum = int(input('Chute um valor entre 1 e 100: '))
nivel = ''
tentativas = 1

while yournum != n:
    tentativas += 1
    if yournum > n:
        nivel = 'baixo'
    elif yournum < n:
        nivel = 'alto'    
    yournum = int(input(f'Chute um valor mais {nivel}: '))
print(f'Muito bem, você acertou depois de {tentativas} tentativas! O número sorteado era {n}')    