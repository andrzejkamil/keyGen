import re
from time import *
from selenium.webdriver.common.by import By

def ua(browser, config, keys, domain):
    print('Otwieranie Google Analytics...')
    browser.get(config.get('urls', 'ua'))
    print('Generowanie klucza UA...')
    sleep(5)

    accounts_message = browser.find_element_by_css_selector('p.quota-status.ng-star-inserted')
    print(accounts_message.text)
    #if accounts_message.text != '':
     #   accounts_message = accounts_message.text.split(' The maximum is ')[0]
      #  print(accounts_message)
       # accounts_amount = accounts_message.replace('You have access to ', '')
        #if ' accounts.' in accounts_amount:
         #   accounts_amount = accounts_amount.replace(' accounts.', '')
        #else:
         #   accounts_amount = accounts_amount.replace(' account.', '')

        #accounts_amount = int(accounts_amount)
        #if accounts_amount <= int(config.get('uaAccounts', 'limit')):
         #      print('\t---UWAGA POZOSTAŁO JUŻ TYLKO ' + str(accounts_amount) + ' WOLNYCH MIEJSC NA KODY UA---')
          #     keys.writelines('\t---UWAGA POZOSTAŁO JUŻ TYLKO ' + str(accounts_amount) +
           #                         ' WOLNYCH MIEJSC NA KODY UA---\n')

    #while True:
    #try:
    #   browser.find_element_by_css_selector('button.suite.suite-gaia-switcher.md-icon-button.md-button.'
   #                                              'md-standard-theme.md-ink-ripple').click()
    #   google_account = browser.find_element_by_css_selector('span.suite-gaia-header-secondary-text').text
     #  print('Zakładanie konta na ' + google_account + '...')
      # if config.get('client', 'uaGoogleAccount') == '1':
       #   keys.writelines(google_account + '\n')

    #except:
     #     sleep(1)
    #browser.refresh()

    inputfield = browser.find_element(By.XPATH, "//input[starts-with(@id, 'create-firebase-account-')]")
    print(inputfield)
    inputfield.send_keys(domain)
    sleep(1)

    btn = browser.find_element(By.XPATH, "/html/body/ga-hybrid-app-root/ui-view-wrapper/div/app-root/div/div/ui-view-wrapper/div/admin-home/div/div[2]/section/admin-view/div/ga-create-account/mat-vertical-stepper/div[1]/div/div/div/button")
    #i = 0
    #while btns[i].text != 'Następny' and btns[i].text != 'Next':
     #   i = i + 1
      #  next_btn = btns[i]
       # next_btn.click()
        #browser.find_element_by_id('name').send_keys(domain)
        #break
    btn.click()
    sleep(1)
    print('Konfiguracja usługi...')
    name = browser.find_element(By.ID, "name")
    name.send_keys(domain)
    sleep(1)
    country = ''
    btns = browser.find_elements_by_tag_name('button')
    i = 0
    while btns[i].text != 'Stany Zjednoczone\narrow_drop_down' and btns[i].text != 'United States\narrow_drop_down':
        i = i + 1
        country = btns[i]
    while True:
        try:
            country.click()
            break
        except:
            sleep(1)

    country = ''
    btns = browser.find_elements_by_tag_name('button')
    i = 0
    while btns[i].text != 'Polska' and btns[i].text != 'Poland':
        i = i + 1
        country = btns[i]
    country.click()

    while True:
        try:
            currency = ''
            btns = browser.find_elements_by_tag_name('button')
            i = 0
            while btns[i].text != 'dolar amerykański ($)\narrow_drop_down' and \
                    btns[i].text != 'dolar amerykański ($)\narrow_drop_down':
                i = i + 1
                currency = btns[i]
            currency.click()
            break
        except:
            sleep(1)

    currency = ''
    btns = browser.find_elements_by_tag_name('button')
    i = 0
    while btns[i].text != 'złoty polski (zł)' and btns[i].text != 'Polish Zloty (zł)':
        i = i + 1
        currency = btns[i]
    currency.click()

    print('Konfigurowanie opcji zaawansowanych...')
    advanced = ''
    btns = browser.find_elements_by_tag_name('button')
    i = 0
    while btns[i].text != 'Pokaż opcje zaawansowane' and btns[i].text != 'Show advanced options':
        i = i + 1
        advanced = btns[i]
    advanced.click()

    browser.find_element_by_class_name("mdc-switch__icons").click()
    browser.find_element(By.XPATH, "//input[starts-with(@id, 'mat-input-')]").send_keys(domain)

    # while True:
    #     try:
    #         browser.find_elements_by_class_name('mat-radio-outer-circle')[0].click()
    #         break
    #     except:
    #         sleep(1)
    btns = browser.find_elements_by_tag_name('button')
    for btn in btns:
        if btn.text == 'Dalej' or btn.text == 'DALEJ' or btn.text == "Next":
            nextBtn = btn
            nextBtn.click()

    # while True:
    #     try:
    #         next_btn = ''
    #         btns = browser.find_elements_by_tag_name('button')
    #         i = 0
    #         while btns[i].text != 'Dalej' and btns[i].text != 'Next':
    #             i = i + 1
    #             next_btn = btns[i]
    #         next_btn.click()
    #         break
    #     except:
    #         sleep(1)

    create = ''
    btns = browser.find_elements_by_tag_name('button')
    i = 0
    while btns[i].text != 'Utwórz' and btns[i].text != 'Create':
        i = i + 1
        create = btns[i]
    create.click()

    country = ''
    btns = browser.find_elements_by_tag_name('button')
    i = 0
    while 'Stany Zjednoczone' not in btns[i].text and 'United States' not in btns[i].text:
        i = i + 1
        country = btns[i]
    country.click()

    country = ''
    btns = browser.find_elements_by_tag_name('button')
    i = 0
    while 'Polska' not in btns[i].text and 'Poland' not in btns[i].text:
        i = i + 1
        country = btns[i]
    country.click()
    form_fields = browser.find_elements_by_class_name('mdc-form-field')
    for form_field in form_fields:
        if 'RODO' in form_field.text or 'GDPR' in form_field.text:
            form_field.find_element_by_class_name("mdc-checkbox__native-control").click()
    confirmBtn = browser.find_element_by_class_name('confirm-button')

    confirmBtn.click()

    sleep(15)

    content = browser.find_element(By.CLASS_NAME, "card-content").text
    content = content.split(" ")
    g4key = content[-1].split()[1]

    g4codehead = f'<script async src="https://www.googletagmanager.com/gtag/js?id={g4key}"></script>';

    g4codebody = '<script>\n' \
                 'window.dataLayer = window.dataLayer || [];\n' \
                 'function gtag(){dataLayer.push(arguments);}\n' \
                 f"gtag('js', new Date());\n" \
                 '\n'\
                 f"gtag('config', '{g4key}');\n" \
                 '</script>\n' \

    print(g4key)
    print(g4codehead)
    print(g4codebody)
    if config.get('domain', 'plusOurUa') != '0':
        ua_keys = open('ua_keys.txt', 'a')
        ua_keys.writelines('\n' + g4key)
        ua_keys.writelines('\n' + g4codehead)
        ua_keys.writelines('\n' + g4codebody)

    keys.writelines('\n' + g4key)
    keys.writelines('\n' + g4codehead)
    keys.writelines('\n' + g4codebody)

    print('Generowanie klucza zakończone')
    return g4key, g4codehead, g4codebody
