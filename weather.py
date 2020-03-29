from speech import speak
from pyowm import OWM

def tellWeather(reg_ex):
	if reg_ex:
		city = reg_ex.group(1)
		owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
		obs = owm.weather_at_place(city)
		w = obs.get_weather()
		k = w.get_status()
		x = w.get_temperature(unit='celsius')
		speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
