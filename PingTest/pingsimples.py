import os  # Importa o módulo ou biblioteca os (integra os programas e recursos do S.O)
print('=' * 80)
ip_ou_host = input("Digite o Ip ou host a ser verificado: ")  # Variável que vai receber um ip do usuário
print('=' * 80)
os.system(f'ping -n 6 {ip_ou_host}')  # chamando system da biblioteca os <comando ping>
print('=' * 80)
