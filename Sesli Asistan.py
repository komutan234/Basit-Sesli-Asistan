import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import random

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Metni sesli olarak okur."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Mikrofondan sesi dinler ve metne dönüştürür."""
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="tr-TR")
            print(f"Algıladım: {text}")
            return text.lower()  # Küçük harfe çevir
        except sr.UnknownValueError:
            speak("Anlayamadım. Lütfen tekrarlayın.")
        except sr.RequestError:
            speak("İnternet bağlantısı yok.")
        return ""

def process_command(command):
    """Gelen komutu işler ve uygun yanıtı verir."""

    # Temel komutlar
    if "merhaba" in command:
        speak("Merhaba! Size nasıl yardımcı olabilirim?")
    elif "saat kaç" in command:
        now = datetime.datetime.now()
        speak(f"Saat {now.hour}:{now.minute}")
    elif "arama yap" in command:
        search_query = command.replace("arama yap", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"{search_query} için arama yapıyorum.")
    elif "fıkra anlat" in command:
        jokes = [
            "Fıkra 1...",
            "Fıkra 2...",
            # Fıkra listenizi buraya ekleyebilirsiniz.
        ]
        speak(random.choice(jokes))
    
    # Özel komutlar (istediğiniz kadar ekleyebilirsiniz)
    elif "nasılsın" in command:
        speak("Ben bir yapay zeka olduğum için duygularım yok ama her zaman hizmetinizdeyim.")
    elif "hava durumu" in command:
        speak("Hava durumu bilgisi için henüz bir bağlantım yok. Ama geliştirme aşamasındayım!")

    else:
        speak("Bu komutu anlayamadım.")

while True:
    command = listen()
    if command:
        process_command(command)
