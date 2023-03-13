from time import *


def recaptcha(browser, config, keys, domain, version):
    print('Otwieranie Google reCaptcha...')
    browser.get(config.get('urls', 'captcha'))
    print('Generowanie kluczy reCaptcha...')
    browser.find_element_by_class_name('zHQkBf').send_keys(domain)
    if version == 2:
        if config.get('client', 'recaptchaVersion') == '1':
            print('recaptcha v2')
        browser.find_elements_by_class_name('Id5V1')[1].click()
    else:
        if config.get('client', 'recaptchaVersion') == '1':
            print('recaptcha v3')
        browser.find_elements_by_class_name('Id5V1')[0].click()
    browser.find_elements_by_class_name('zHQkBf')[1].send_keys(domain)
    browser.find_elements_by_class_name('Ce1Y1c')[4].click()
    browser.find_element_by_class_name('fsHoPb').click()
    browser.find_elements_by_class_name('rq8Mwb')[1].click()

    upload = ''
    i = 0
    btns = browser.find_elements_by_class_name('snByac')
    while btns[i].text != 'PRZEŚLIJ':
        i = i + 1
        upload = btns[i]
    upload.click()

    while True:
        try:
            site_key = browser.find_elements_by_class_name('PzWife')[0].text
            secret_key = browser.find_elements_by_class_name('PzWife')[1].text
            break
        except:
            sleep(1)
    if version == 2:
        if config.get('client', 'recaptchaVersion') == '1':
            keys.writelines('recaptcha V2:\n')
    else:
        if config.get('client', 'recaptchaVersion') == '1':
            keys.writelines('recaptcha V3:\n')
    keys.writelines('site:\t\t' + site_key + '\n')
    keys.writelines('secret:\t\t' + secret_key + '\n')
    print('Generowanie kluczy zakończone')
