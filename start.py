from api import *
from recaptcha import *
from jch import *
from firewall import *
from form import *
from ua import *
from tags import *


def start(domain, browser, config):
    keys = open('keys.txt', 'a')
    keys.writelines('----------------------------------------------------\n' + domain + '\n')
    keys.close()
    print('----------------')
    print('@@@@ Generowanie kluczy dla ' + domain + ' @@@@')
    print('----------------')
    keys = open('keys.txt', 'a')
    if config.get('keys', 'recaptcha2') != '0':
        recaptcha(browser, config, keys, domain, 2)
        print('----------------')
    keys.close()
    keys = open('keys.txt', 'a')
    if config.get('keys', 'recaptcha3') != '0':
        recaptcha(browser, config, keys, domain, 3)
        print('----------------')
    keys.close()
    keys = open('keys.txt', 'a', encoding='utf-8')
    if config.get('keys', 'api') != '0':
        api(browser, config, keys, domain)
        print('----------------')
    keys.close()
    keys = open('keys.txt', 'a')
    if config.get('keys', 'jch') != '0':
        jch(browser, config, keys, domain)
        print('----------------')
    keys.close()
    keys = open('keys.txt', 'a')
    if config.get('keys', 'firewall') != '0':
        firewall(browser, config, keys, domain)
        print('----------------')
    keys.close()
    keys = open('keys.txt', 'a')
    if config.get('keys', 'form') != '0':
        form(browser, config, keys, domain)
        print('----------------')
    keys.close()
    keys = open('keys.txt', 'a', encoding='utf-8')
    ua_key = ''
    if config.get('keys', 'ua') != '0':
        ua_key = ua(browser, config, keys, domain)
        print('----------------')
    keys.close()
    keys = open('keys.txt', 'a')
    if config.get('keys', 'tags') != '0':
        tags(browser, config, keys, domain, ua_key)
        print('----------------')
