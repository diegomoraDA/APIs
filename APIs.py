# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:19:29 2024

@author: Mora
"""

import requests

def get_artworks(api_key, size=10, page=1):
   
    URL = 'https://api.harvardartmuseums.org/object'
    params = {
        'apikey': api_key,
        'size': size,
        'page': page
    }

    respuesta_API = requests.get(URL, params=params)
    
    if respuesta_API.status_code == 200:
        datos = respuesta_API.json()
        for i, record in enumerate(datos['records'], start=1):
            print(f"{i}. {record.get('title', 'Sin título')} - {record.get('dated', 'Fecha desconocida')}")
    else:
        print(f"Error al consultar la API: {respuesta_API.status_code}")

if __name__ == '__main__':
    api_key = 'd7a5ebe1-b2be-4b5a-b258-907519168c54'  # Reemplaza esto con tu clave de API real
    get_artworks(api_key)