# coding=utf-8

import urllib.request
import requests
import json 

def GetNameToURL(name):
	nombre = name
	nombre = nombre.replace(' ', '+')
	return nombre


def GetInfoDBLP(autor):
    
    autorName = GetNameToURL(autor)
    #Formato de la respuesta
    formato = 'json'
    #Lista de retorno con los articulos
    typeArticles = []
    #URL donde se lee la información
    url = 'https://dblp.org/search/publ/api?q={}&format={}'.format(autorName,formato)

    #Acceso a la URL
    contents = urllib.request.urlopen(url).read() #Lee con la estructura del formato pero guarda en tipo bytes
    contents = contents.decode('utf-8') #Convierte bytes a str
    contents = json.loads(contents) #Convierte en un diccionario de python
    data = contents['result']['hits']['hit'] #Guarda en data lista de resultados 
    
    for hit in data:
        result = {}

        result['title'] = hit['info']['title']
        result['venue'] = hit['info']['venue']
        result['type'] = hit['info']['type']
        typeArticles.append(result)

    return typeArticles









