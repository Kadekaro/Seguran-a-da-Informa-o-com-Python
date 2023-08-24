import random
import string

tamanho = int(input('Digite o tamanho de senha que você deseja: '))
chars = string.ascii_letters + string.digits + f'!ç@#$%¨&*()_=+?:;><'
# os.urandom -> biblioteca e classe que gera números aleatórios a partir do sistema operacional:
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
