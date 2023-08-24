import hashlib
import time

string = input("Digite o texto que irá gerar a hash: ")


def Menu():
    while True:
        print("=" * 35)
        menu_input = input("""
|=============  MENU  ============|
|             1) MD5              |
|             2) SHA1             |
|             3) SHA 256          |
|             4) SHA512           |
|=================================|

Digite o número do hash a ser gerado: """)

        try:
            menu = int(menu_input)
            if 1 <= menu <= 4:
                resultado = hashlib.md5(string.encode('utf-8')) if menu == 1 else \
                            hashlib.sha1(string.encode('utf-8')) if menu == 2 else \
                            hashlib.sha256(string.encode('utf-8')) if menu == 3 else \
                            hashlib.sha512(string.encode('utf-8'))
                print("O hash da string é:", resultado.hexdigest())
            else:
                print('Digite somente valores de um a quatro, tente novamente!')
                time.sleep(2)
        except ValueError:
            print('Digite somente valores numéricos de um a quatro, tente novamente!')
            time.sleep(2)


Menu()
