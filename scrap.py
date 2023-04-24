import requests
from bs4 import BeautifulSoup

#Extraccion de los titulos de las noticias

url= "https://www.eltribuno.com/salta"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
titulos = html.find_all("h1", class_="title-item")
titulos = [ str(titulo)[str(titulo).rfind('">')+1:-10] for titulo in titulos ]
titulos = [titulo.strip() for titulo in titulos]
for titulo in titulos:
    print(titulo)
