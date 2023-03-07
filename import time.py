from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pygame
import time

driver = webdriver.Chrome()
pygame.init()
pygame.mixer.music.load("anya.ogg")

opt = Options()
opt.add_argument("--disable-infobars")
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
time.sleep(1)
print("Cheguei até aqui 1")
time.sleep(1)
element2 = driver.find_element(By.XPATH, '//*[@id="try"]/form/textarea')
time.sleep(1)
element2.send_keys('おはようございました')
pygame.mixer.music.play()
botao_site_japones = driver.find_element(By.XPATH, '//*[@id="try"]/form/input[2]')
botao_site_japones.click()
time.sleep(3)
texto = driver.find_element(By.XPATH, '//*[@id="source"]/span[1]')
time.sleep(1)
texto_transcrito = texto.get_attribute('innerHTML')

print(texto_transcrito)

pygame.quit()
driver.quit()