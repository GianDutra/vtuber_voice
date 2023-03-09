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

def print_portugues():
    print("Teclas de atalho e suas respectivas funções:\n")
    print("'ctrl+alt+a': Gravar o áudio")
    print("'ctrl+3': Idioma Português")
    print("'ctrl+4': Idioma Espanhol")
    print("'ctrl+5': Idioma Inglês")
    print("'ctrl+6': Ativar/desativar a tradução de idiomas")
    print("'ctrl+alt+o': Diminuir o volume do áudio")
    print("'ctrl+alt+p': Aumentar o volume do áudio")
    print("'ctrl+alt+k': Mudar a voz para Mochiko")
    print("'ctrl+alt+l': Mudar a voz para a de um homem")
    print("'ctrl+alt+j': Mudar a voz para a voz padrão")
    print("'ctrl+alt+n': Modo sussurro ativado(Apenas funciona com a menina)")
    print("'ctrl+alt+m': Modo sussurro desativado(Apenas funciona com a menina)")
    print("")

def print_espanhol():
    print("Teclas de acceso rápido y sus respectivas funciones:\n")
    print("'ctrl+alt+a': Grabar el audio")
    print("'ctrl+3': Idioma portugués")
    print("'ctrl+4': Idioma español")
    print("'ctrl+5': Idioma inglés")
    print("'ctrl+6': Activar/desactivar la traducción de idiomas")
    print("'ctrl+alt+o': Disminuir el volumen del audio")
    print("'ctrl+alt+p': Aumentar el volumen del audio")
    print("'ctrl+alt+k': Cambiar la voz a Mochiko")
    print("'ctrl+alt+l': Cambiar la voz a la de un hombre")
    print("'ctrl+alt+j': Cambiar la voz a la voz predeterminada")
    print("'ctrl+alt+n': Modo susurro activado (Solo funciona con la voz de la niña)")
    print("'ctrl+alt+m': Modo susurro desactivado (Solo funciona con la voz de la niña)")
    print("")

def print_ingles():
    print("Keyboard shortcuts and their respective functions:\n")
    print("'ctrl+alt+a': Record audio")
    print("'ctrl+3': Portuguese language")
    print("'ctrl+4': Spanish language")
    print("'ctrl+5': English language")
    print("'ctrl+6': Enable/disable language translation")
    print("'ctrl+alt+o': Decrease audio volume")
    print("'ctrl+alt+p': Increase audio volume")
    print("'ctrl+alt+k': Change voice to Mochiko")
    print("'ctrl+alt+l': Change voice to male voice")
    print("'ctrl+alt+j': Change voice to default voice")
    print("'ctrl+alt+n': Whisper mode activated (Only works with female voice)")
    print("'ctrl+alt+m': Whisper mode deactivated (Only works with female voice)")
    print("")

def ingles():
    global idioma
    idioma = "en-US"
    print("Idioma atualizado para inglês")
    print("-----------------------------------------------------:\n")
    print_ingles()

def portugues():
    global idioma
    idioma = "pt-BR"
    print("Idioma atualizado para português")
    print("-----------------------------------------------------:\n")
    print_portugues()

def espanhol():
    global idioma
    idioma = "es-ES"
    print("Idioma atualizado para espanhol")
    print("-----------------------------------------------------:\n")
    print_espanhol()


def traducao_ativar_desativar():
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

global voz_escolhida
voz_escolhida = 0


def mudarVozParaMochiko():
    combo_box = driver.find_element(By.XPATH, '//*[@id="charSelect"]')
    # selecione a opção com o valor "10"
    select = Select(combo_box)
    select.select_by_value("10")
    print("Sua voz agora é de uma mulher")
    global voz_escolhida
    voz_escolhida = 1

def mudarVozParaHomem():
    combo_box = driver.find_element(By.XPATH, '//*[@id="charSelect"]')
    # selecione a opção com o valor "21"
    select = Select(combo_box)
    select.select_by_value("21")
    print("Sua voz agora é de um homem")
    global voz_escolhida
    voz_escolhida = 2

def mudarVozParaDefault():
    combo_box = driver.find_element(By.XPATH, '//*[@id="charSelect"]')
    # selecione a opção com o valor "21"
    select = Select(combo_box)
    select.select_by_value("1")
    print("Sua voz agora é de uma menina")
    global voz_escolhida
    voz_escolhida = 0



def vozBaixa():
    if voz_escolhida == 0:
        alturaVoz_box = driver.find_element(By.XPATH, '//*[@id="speaker"]')
        selecionar = Select(alturaVoz_box)
        selecionar.select_by_value("22")
        print("Modo sussurro ativado")
    else:
        print("Você precisa estar usando a voz da menina para ativar o modo sussurro.")
      

def vozNormal():
    alturaVoz_box = driver.find_element(By.XPATH, '//*[@id="speaker"]')
    selecionar = Select(alturaVoz_box)
    selecionar.select_by_value("3")
    print("Modo sussurro desativado")


keyboard.add_hotkey('ctrl+alt+a', callback_function)

keyboard.add_hotkey('ctrl+alt+h', parar_programa)

keyboard.add_hotkey('ctrl+3', portugues)

keyboard.add_hotkey('ctrl+4', espanhol)

keyboard.add_hotkey('ctrl+5', ingles)

keyboard.add_hotkey('ctrl+6', traducao_ativar_desativar)

keyboard.add_hotkey('ctrl+alt+o', diminui_tamanho_audio)

keyboard.add_hotkey('ctrl+alt+p', aumenta_tamanho_audio)

keyboard.add_hotkey('ctrl+alt+k', mudarVozParaMochiko)

keyboard.add_hotkey('ctrl+alt+l', mudarVozParaHomem)

keyboard.add_hotkey('ctrl+alt+j', mudarVozParaDefault)

keyboard.add_hotkey('ctrl+alt+n', vozBaixa)

keyboard.add_hotkey('ctrl+alt+m', vozNormal)


print("\n\nVtuber voice 1.5 by Chikenator")
print("--------------------------------------------")
print_portugues()

while programa_rodando:
    keyboard.wait()
