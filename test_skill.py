# test_skill.py
import time
from ovos_bus_client.bus import MessageBusClient
from ovos_bus_client.message import Message

# MessageBusClient başlat
bus = MessageBusClient()
bus.run_in_thread()

# Bus'a bağlanmayı bekle
if not bus.connected_event.wait(5):
    print("Bus'a bağlanılamadı!")
    exit(1)

# Hedef skill'e örnek bir utterance gönder
utterance = "hava durumu İstanbul"
message = Message(
    "recognizer_loop:utterance",
    {
        "utterances": [utterance],
        "lang": "tr-tr"
    }
)
bus.emit(message)

# Skill'in yanıt vermesi için biraz bekle
time.sleep(3)

print(f"'{utterance}' komutu gönderildi ve işlenmesi bekleniyor.")