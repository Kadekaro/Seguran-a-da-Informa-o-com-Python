import itertools

string = input("Digite os caracteres ou palavras para que sejam permutadas: ")

# resultado = itertools.permutations('abc', 3)
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))
