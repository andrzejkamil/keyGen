from functions import *
from start import *
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from configparser import *
import os
import winsound
import warnings

start_time = time()

config = ConfigParser()
config.read('config.ini', encoding='utf-8-sig')
headless = check_headless(config)
domain = ''

if config.get('client', 'ignoreWarnings') == '1':
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=UserWarning)

print('Tworzenie pliku tekstowego na gotowe klucze...')
keys_file = open('keys.txt', 'a')
keys_file.close()

print('Otwieranie przeglądarki...')
profile_path = r'' + config.get('client', 'profile') + ''
options = Options()
options.headless = headless
options.profile = profile_path
if config.get('client', 'defaultFirefox') == '0':
    options.binary = 'Firefox64/firefox.exe'
service = Service('geckodriver.exe')

browser = Firefox(service=service, options=options)

if config.get('domain', 'manyDomains') == '1':
    domains_file = open('domains.txt', 'r')
    lines = domains_file.readlines()
    for line in lines:
        domain = line.split('\n')
        domain = domain[0]
        start(domain, browser, config)

else:
    domain = config.get('domain', 'domain')
    start(domain, browser, config)
browser.quit()
if config.get('client', 'finitoSound') == '1':
    winsound.PlaySound('assets/Yahoo!.wav', winsound.SND_FILENAME)
print('Program zakończył pracę\n\tKlucze zostały zapisane w pliku keys.txt')
finito_time = int((time() - start_time)/60)
print('Czas wykonania: ' + str(finito_time) + ' min')
os.system('PAUSE')
