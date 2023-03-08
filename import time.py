from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pygame
import time
import keyboard
import speech_recognition as sr



driver = webdriver.Chrome()
pygame.init()
pygame.mixer.music.load("anya.ogg")

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--headless")
opt.add_argument("--disable-extensions")
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })



driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Python39\chromedriver.exe')
driver.get('https://voicevox.su-shiki.com/#try')


def gravarAudio():

    
    # Executa a música previamente carregada
    pygame.mixer.music.play()

    # Cria um objeto do Recognizer
    r = sr.Recognizer()

    # Define o tempo máximo de silêncio para 2 segundos
    silence_time = 5


    # Usa o microfone como fonte de áudio
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = r.listen(source, phrase_time_limit=silence_time)

        try:
            # Transcreve o áudio em texto
            texto = r.recognize_google(audio, language='ja-JP')
            print("Você disse: ", texto)
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
        except sr.RequestError as e:
            print("Não foi possível conectar-se ao serviço de reconhecimento de fala; {0}".format(e))

    return texto


def toVtuber(texto):

    element2 = driver.find_element(By.XPATH, '//*[@id="try"]/form/textarea')
    element2.send_keys(Keys.CONTROL, 'a')
    element2.send_keys(texto)
    botao_site_japones = driver.find_element(By.XPATH, '//*[@id="try"]/form/input[2]')
    botao_site_japones.click()
    time.sleep(3)


def callback_function():
        texto = gravarAudio()
        toVtuber(texto)


def finalizar_programa():
    pygame.quit()
    driver.quit()
    exit()


keyboard.add_hotkey('ctrl+alt+a', callback_function)

keyboard.add_hotkey('ctrl+alt+p', finalizar_programa)


keyboard.wait()

