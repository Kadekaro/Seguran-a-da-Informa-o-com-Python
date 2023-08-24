import ctypes


pasta = input("Digite o caminho da pasta a ser ocultada: ")

atributos_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributos_ocultar)
# retorno = ctypes.windll.kernel32.SetFileAttributesW("ocultar.txt", atributos_ocultar)

if retorno:
    print("Atributo ocultado!")
else:
    print("O arquivo não foi ocultado!")
