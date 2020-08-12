import requests

class Current_Weather():

    def __init__(self, city_name):
        self.api_key = "4e72bb43d5953cd9516a2b41074fac7b"
        self.city_name = city_name

    def get_weather(self):
        request = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(self.city_name, self.api_key)
        response = requests.get(request)

        if response.json()["cod"] == "404":
            return "Такого города нет :(\n Попробуйте снова"
        else:
            real_temp = response.json()["main"]["temp"]
            pressure = response.json()["main"]["pressure"]
            speed = response.json()["wind"]["speed"]

            return round(real_temp - 273.15, 2), pressure, speed


if __name__ == '__main__':
    cur = Current_Weather('Moscow')
    print(cur.get_weather())


