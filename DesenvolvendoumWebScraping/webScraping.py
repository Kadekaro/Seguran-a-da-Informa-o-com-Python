from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content

# objeto site recebendo o conteúdo da requisição http do site...
soup = BeautifulSoup(site, 'html.parser')

# objeto soup baixando do site o html
print(soup.prettify())  # mostra as informações do site

print("="*100)
print("Transforma o html em string, e o registro de tela vai exibir o html: \n")
temperatura = soup.find("p", class_="-gray _flex _align-center")
print(temperatura)

print("="*100)
temperatura_minima = temperatura.contents[2].strip()
temperatura_maxima = temperatura.contents[4].strip()

print("Mostra o título e as temperaturas de Máx e Min: \n")
print(soup.title.string[:-13] + "!")  # Mostra o título do site!
print(f"Temperatura mínima: {temperatura_minima}")
print(f"Temperatura máxima: {temperatura_maxima}")

print("="*100)
print(f"Mostrando as notícias: \n")
noticias = soup.find_all("h4", class_="-gray-dark-2 -font-base -bold")
for noticia in noticias:
    texto_noticia = noticia.get_text()
    print(texto_noticia)

print("="*100)
print("Target Ancora: ")
print(soup.a)

print("="*100)
print("Primeira Target 'p' que ele achar: ")
print(soup.p)

print("="*100)
print("Se tiver administrador na página, vc também pode tentar buscar ele etc: ")
print(soup.find("admin"))
print("="*100)
