import ipaddress

ip = "192.168.0.1"

rede_ip = "192.168.0.0/24"
forcado_rede_ip = "192.168.0.100/24"

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(rede_ip)
rede_forcada = ipaddress.ip_network(forcado_rede_ip, strict=False)

print(endereco)
print(rede)
print(rede_forcada)
