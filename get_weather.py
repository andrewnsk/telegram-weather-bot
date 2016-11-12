import json
import azimuth
import urllib.request

MMHG = 0.75006375541921


class GetWeather:

    def __init__(self, location):
        api_url = "api.openweathermap.org"
        appid = '3ede2418f1124401efcd68e5ae3bddcb'
        units = 'metric'
        lang = 'en'
        self.town = location
        url_str = 'http://{0}/data/2.5/weather?q={1}&APPID={2}&units={3}&lang={4}'.format(api_url,
                                                                                          self.town,
                                                                                          appid,
                                                                                          units,
                                                                                          lang)
        print(url_str)

        response = urllib.request.urlopen(url_str)
        json_str = response.read()
        u_json = json.loads(json_str.decode('utf-8'))
        self.data = u_json

    def wind_direction(self):
        return str(azimuth.degree(round(self.data['wind']['deg'])))

    def wind_speed(self):
        return str(self.data['wind']['speed'])

    def temperature(self):
        temp = self.data['main']['temp']
        return str(temp)

    def humidity(self):
        return str(self.data['main']['humidity'])

    def pressure(self):
        return str(self.data['main']['pressure'])

    def id(self):
        return str(self.data['weather']['id'])

