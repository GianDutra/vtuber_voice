from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from googletrans import Translator
import pygame
import time
import keyboard
import speech_recognition as sr


pygame.init()
pygame.mixer.music.load("anya.ogg")
programa_rodando = True


# cria uma instância do objeto Translator
translator = Translator()

# Define o idioma padrão do aplicativo 
global idioma
idioma = "pt-br"

# Deixa a traducao ativada
global traducao
traducao = True

# Define o tamanho do audio
global tam_audio
tam_audio = 4

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

    global traducao
    # Executa a música previamente carregada
    pygame.mixer.music.play()

    # Cria um objeto do Recognizer
    r = sr.Recognizer()

    # Define o tempo máximo de silêncio para 2 segundos
    silence_time = tam_audio


    # Usa o microfone como fonte de áudio
    with sr.Microphone() as source:
        

        

        if traducao : 
            try:
                print("Fale algo...")
                audio = r.listen(source, phrase_time_limit=silence_time)   
                # Transcreve o áudio em texto
                texto_em_portugues = r.recognize_google(audio, language=idioma)

                if texto_em_portugues.startswith('Como') or texto_em_portugues.startswith('O que') or texto_em_portugues.startswith('Qual'):
                 texto_em_portugues += '?'

                print("Você disse(com traducao): ", texto_em_portugues)
                
                texto = translator.translate(texto_em_portugues, dest='ja')
                print("A traducao e: ", texto.text)
                
                texto = texto.text
            except sr.UnknownValueError:
                print("Não entendi o que você disse")
            except sr.RequestError as e:
                print("Não foi possível conectar-se ao serviço de reconhecimento de fala; {0}".format(e))
                
        else:
            try:
                print("Fale algo...")
                audio = r.listen(source, phrase_time_limit=silence_time)
                # Transcreve o áudio em texto
                texto = r.recognize_google(audio, language='ja-JP')
                print("Você disse(sem traducao): ", texto)
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


def parar_programa():
    global programa_rodando
    programa_rodando = False
    pygame.quit()
    keyboard.unhook_all_hotkeys()
    keyboard.clear_all_hotkeys()
    driver.quit()

def ingles():
    global idioma
    idioma = "en-US"
    print("Idioma atualizado para inglês")

def portugues():
    global idioma
    idioma = "pt-BR"
    print("Idioma atualizado para português")

def espanhol():
    global idioma
    idioma = "es-ES"
    print("Idioma atualizado para espanhol")


def traducao_desativada():
    global traducao
    if traducao:
        traducao = False
        print("Tradução desativada")
    else:
        traducao = True
        print("Tradução ativada")

def aumenta_tamanho_audio():
    global tam_audio
    tam_audio = tam_audio + 1
    print("O tamanho do áudio agora é:" + str(tam_audio))

def diminui_tamanho_audio():
    global tam_audio
    tam_audio = tam_audio - 1
    print("O tamanho do áudio agora é:" + str(tam_audio))

def mudarVozParaMochiko():
    combo_box = driver.find_element(By.XPATH, '//*[@id="charSelect"]')
    # selecione a opção com o valor "10"
    select = Select(combo_box)
    select.select_by_value("10")
    print("Sua voz agora é de uma mulher")

def mudarVozParaHomem():
    combo_box = driver.find_element(By.XPATH, '//*[@id="charSelect"]')
    # selecione a opção com o valor "21"
    select = Select(combo_box)
    select.select_by_value("21")
    print("Sua voz agora é de um homem")

def mudarVozParaDefault():
    combo_box = driver.find_element(By.XPATH, '//*[@id="charSelect"]')
    # selecione a opção com o valor "21"
    select = Select(combo_box)
    select.select_by_value("1")
    print("Sua voz agora é de uma menina")


keyboard.add_hotkey('ctrl+alt+a', callback_function)

keyboard.add_hotkey('ctrl+alt+h', parar_programa)

keyboard.add_hotkey('ctrl+3', portugues)

keyboard.add_hotkey('ctrl+4', espanhol)

keyboard.add_hotkey('ctrl+5', ingles)

keyboard.add_hotkey('ctrl+6', traducao_desativada)

keyboard.add_hotkey('ctrl+alt+o', diminui_tamanho_audio)

keyboard.add_hotkey('ctrl+alt+p', aumenta_tamanho_audio)

keyboard.add_hotkey('ctrl+alt+k', mudarVozParaMochiko)

keyboard.add_hotkey('ctrl+alt+l', mudarVozParaHomem)

keyboard.add_hotkey('ctrl+alt+j', mudarVozParaDefault)

while programa_rodando:
    keyboard.wait()
        

