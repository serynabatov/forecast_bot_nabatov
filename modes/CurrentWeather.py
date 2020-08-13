import aiohttp
import asyncio

class Current_Weather():

    def __init__(self, city_name):
        self.api_key = os.environ.get('API_KEY')
        self.city_name = city_name

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.json()


    async def get_weather(self):
        request = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(self.city_name, self.api_key)
        #response = requests.get(request)
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, request)

            if html["cod"] == "404":
                return "Такого города нет :(\n Попробуйте снова"
            else:
                real_temp = html["main"]["temp"]
                pressure = html["main"]["pressure"]
                speed = html["wind"]["speed"]
                return round(real_temp - 273.15, 2), pressure, speed


if __name__ == '__main__':
    cur = Current_Weather('Moscow')
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(cur.get_weather()))
