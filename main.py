import requests
import json

def consultar_api(ciudad_origen, ciudad_destino):
    url = f'https://graphhopper.com/api/1/route?point={ciudad_origen}&point={ciudad_destino}&vehicle=car&locale=en&key=api_key'
    response = requests.get(url)
    data = response.json()
    return data

def calcular_duracion(data):
    if 'paths' in data and data['paths']:
        path = data['paths'][0]
        time = path['time'] / 1000  # tiempo en segundos
        horas = int(time / 3600)
        minutos = int((time % 3600) / 60)
        segundos = int(time % 60)
        return horas, minutos, segundos
    return None

def mostrar_narrativa(data):
    if 'paths' in data and data['paths']:
        path = data['paths'][0]
        distancia = path['distance'] / 1000  # distancia en kilómetros
        return f"El viaje de {ciudad_origen} a {ciudad_destino} es de {distancia:.2f} km y tomará aproximadamente {horas} horas, {minutos} minutos y {segundos} segundos."
    return "No se encontró información para la ruta especificada."

def main():
    while True:
        ciudad_origen = input("Ingrese la ciudad de origen (o 'q' para salir): ")
        if ciudad_origen.lower() == 'q':
            break
        ciudad_destino = input("Ingrese la ciudad de destino: ")
        
        data = consultar_api(ciudad_origen, ciudad_destino)
        if data:
            horas, minutos, segundos = calcular_duracion(data)
            if horas is not None:
                narrativa = mostrar_narrativa(data)
                print(narrativa)
            else:
                print("No se pudo calcular la duración del viaje.")
        else:
            print("No se pudo obtener datos de la API.")

if __name__ == "__main__":
    main()
