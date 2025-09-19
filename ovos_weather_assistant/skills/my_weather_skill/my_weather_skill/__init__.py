

from ovos_bus_client.message import Message
from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
import requests
from datetime import datetime


class WeatherSkill(OVOSSkill):
    def __init__(self,*args,**kwargs):
        super().__init__(name="my_weather_skill",*args, **kwargs)
    @intent_handler("hava_durumu.intent")
    def handle_weather_intent(self, message: Message):
        city = message.data.get("city", "Istanbul")
        api_key = self.settings.get("openweather_api_key", "b97736c847554163833234556251609")
        url = "http://api.openweathermap.org/data/2.5/weather"
        params ={ "q" : city, "appid": api_key, "units" : "metric", "lang": "tr"}
        try:
            response = requests.get(url,params=params, timeout=10)
            data = response.json()

        except Expection:
                self.speak("Hava durumu erişilemedi")
                return

        if data.get("main"):
            temp = data.get("main",{}).get("temp")
            weather_items = data.get("weather") or []
            desc = weather_items[0].get("description") if weather_items else None
            if temp is not None and desc:
                self.speak(f"{city} şehrinde hava {desc}, sıcaklık {temp}°C.")
            else:
                self.speak("Hava durumu bilgisi eksik görünüyor.")
        else:
            self.speak("Şehir bulunamadı.")

    @intent_handler("saat.intent")
    def handle_time_intent(self, message: Message):
        now = datetime.now().strftime("%H:%M:%S")
        self.speak(f"Şu an saat {now}")



