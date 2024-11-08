import requests

### Tu clave de API de OpenWeather
api_key = "Tu clave api"
ciudad = input("Ingrese el nombre de la Ciudad: ")
pais = input("Ingrese el codigo ISO de su pais: ")  ### Código de país de Colombia (usando el código del país en formato ISO)

### hacer la solicitud api
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}"
respuesta = requests.get(url)
data = respuesta.json()

### verificar su fue exitosa la solicitud
if respuesta.status_code == 200:
    city_id = data['id']
    print(f"El ID de la ciudad {ciudad} es: {city_id}")
else:
    print("No se encontró la ciudad.")
