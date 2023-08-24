import hashlib

arquivo1 = "aTeste.txt"
arquivo2 = "bTeste.txt"

hash1 = hashlib.new("ripemd160")

hash1.update(open(arquivo1, "rb").read())

hash2 = hashlib.new("ripemd160")

hash2.update(open(arquivo2, "rb").read())

# if hash1 == hash2:
#     print("São iguais")
# else:
#     print("São diferentes")

if hash1.digest() != hash2.digest():
    print(f"O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}!")
    print(f"O hash do arquivo aTeste.txt é: {hash1.hexdigest()}")
    print(f"O hash do arquivo bTeste.txt É: {hash2.hexdigest()}")
else:
    print(f"O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}!")
    print(f"O hash do arquivo aTeste.txt é: {hash1.hexdigest()}")
    print(f"O hash do arquivo bTeste.txt É: {hash2.hexdigest()}")
