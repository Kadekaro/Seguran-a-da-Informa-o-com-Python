import re
import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"
resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']
hostname = dados['hostname']
localizacao = dados['loc']
cep = dados['postal']
fusohorario = dados['timezone']
meleia = dados['readme']

print("Detalhes do IP externo\n")
print(f"IP: {ip}\nPaís: {pais}\nCidade: {cid}\nOrg.: {org}\nRegião: {regiao}\n"
      f"HostName: {hostname}\nLocalização: {localizacao}\nCep: {cep}\nFuso-Horário: {fusohorario}\n"
      f"Me leia: {meleia}")

