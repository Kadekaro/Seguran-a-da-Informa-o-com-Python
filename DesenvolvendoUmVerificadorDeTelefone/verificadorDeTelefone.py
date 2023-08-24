import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o telefone no formato do Brasil --> +xx (xx) xxxx-xxxx: ")
phone_numbers = phonenumbers.parse(phone.strip())

print(geocoder.description_for_number(phone_numbers, 'pt'))
