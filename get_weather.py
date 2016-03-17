import pyowm
import json
import azimuth


class GetWeather:

    def __init__(self, location):

        if location == "Норильск" or location == "норильск":
            self.location = "Norilsk"
        elif location == "Краснодар" or location == "краснодар":
            self.location = "Krasnodar"
        elif location == "Сочи" or location == "сочи":
            self.location = "Sochi"
        else:
            self.location = location

        # openweathermap API key
        # please use you own api key!
        self.owm_api_key = '3ede2418f1124401efcd68e5ae3bddcb'

        self.owm = pyowm.OWM(self.owm_api_key, language='ru')
        self.observation = self.owm.weather_at_place('{0}'.format(self.location))
        self.w = self.observation.get_weather()
        self.l = self.observation.get_location()

    def town(self):
        return str(json.loads(json.dumps(self.l.get_name())))

    def wind_direction(self):
        return str(azimuth.degree(round(json.loads(json.dumps(self.w.get_wind()), 1)['deg'])))

    def wind_speed(self):
        return str(round(json.loads(json.dumps(self.w.get_wind()))['speed']))

    def temperature(self):
        return str(round(json.loads(json.dumps(self.w.get_temperature('celsius')))['temp']))

    def humidity(self):
        return int(round(json.loads(json.dumps(self.w.get_humidity()))))

    def status(self):
        return str(json.loads(json.dumps(self.w.get_detailed_status())))
