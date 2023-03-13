from time import *
from selenium.webdriver.support.ui import Select


def new_variable(browser, ua_key, variable_id):
    print('Tworzenie nowej zmiennej dla kodu ' + ua_key + '...')
    while True:
        try:
            select6 = browser.find_elements_by_tag_name('select')[6]
            options = select6.find_elements_by_tag_name('option')
            select = Select(select6)
            i = 0
            while True:
                option_label = options[i].get_attribute('label')
                if 'Nowa zmienna...' in option_label:
                    correct_option = options[i].get_attribute('value')
                    break
                i = i + 1
            while True:
                try:
                    select.select_by_value(correct_option)
                    break
                except:
                    sleep(1)
            break
        except:
            sleep(1)
    while True:
        try:
            ua_id = browser.find_element_by_id(str(variable_id) + '-variable.data.vendorTemplate.param.trackingId'). \
                find_element_by_tag_name('input')
            break
        except:
            sleep(1)
    ua_id.send_keys(ua_key)
    ua_id.submit()
    sleep(2)
    browser.find_element_by_class_name('has-footer').find_element_by_tag_name('button').click()
    sleep(2)


def beginning(browser, domain):
    print('Generowanie tagów...')
    print('Zakładanie konta...')
    while True:
        try:
            browser.find_element_by_class_name('blg-form-input').find_element_by_id('1-form.account.data.name'). \
                send_keys(domain)
            browser.find_element_by_tag_name('select').click()
            break
        except:
            sleep(1)
    while True:
        try:
            select = Select(browser.find_element_by_tag_name('select'))
            select.select_by_visible_text('Polska')
            break
        except:
            sleep(1)
    print('Konfiguracja kontenera...')
    browser.find_element_by_class_name('hide-read-only').find_element_by_tag_name('input').send_keys(domain)
    browser.find_element_by_class_name('blg-indented-icon').click()

    btns = browser.find_elements_by_tag_name('button')
    create = ''
    i = 0
    while btns[i].text != 'Utwórz':
        i = i + 1
        create = btns[i]
    sleep(1)
    create.click()

    print('Akceptowanie warunków korzystania z Menedżera tagów Google...')
    return 0


def tags(browser, config, keys, domain, ua_key):
    print('Otwieranie menedżera tagów...')
    browser.get(config.get('urls', 'tag'))
    sleep(2)

    i = beginning(browser, domain)
    while True:
        try:
            browser.find_elements_by_class_name('material-container')[1].find_element_by_class_name('material-icon').\
                click()
            break
        except:
            print('\tPróba ' + str(i+1) + '/5')
            i = i + 1
            if i >= 5:
                browser.refresh()
                i = beginning(browser, domain)
            sleep(1)
    print('Akceptowanie...')
    btns = browser.find_elements_by_tag_name('button')
    yes = ''
    i = 0
    while btns[i].text != 'Tak':
        i = i + 1
        yes = btns[i]
    yes.click()

    print('Sprawdzanie miejsca na tagi...')
    sleep(1)
    try:
        toast = browser.find_element_by_class_name('toast-msg')
        if 'Masz już maksymalną dozwoloną liczbę kont. Usuń jedno z nich, zanim utworzysz nowe.' in toast.text:
            print('\t\t!!!\t' + toast.text)
            keys.writelines('\nTAGS:\n' + '\t\t!!!\t' + toast.text + '\n\n')
            keys.close()
            return 0
    except:
        sleep(1)

    print('Konfiguracja tagów...')
    while True:
        try:
            gtm = browser.find_element_by_class_name('gms-container-status-header').find_element_by_tag_name('a').text
            break
        except:
            try:
                btns = browser.find_elements_by_tag_name('button')
                yes = ''
                i = 0
                while btns[i].text != 'Tak':
                    i = i + 1
                    yes = btns[i]
                yes.click()
            except:
                sleep(1)
            sleep(1)
    head = "<!-- Google Tag Manager -->\n<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'" \
           "gtm.start':\nnew Date()." \
           "getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],\nj=d.createElement(s)," \
           "dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=\n'https://www.googletagmanager.com/" \
           "gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);\n})(window,document,'script','" \
           "dataLayer','" + gtm + "');</script>\n<!-- End Google Tag Manager -->"
    body = '<!-- Google Tag Manager (noscript) -->\n<noscript><iframe src=' \
           '"https://www.googletagmanager.com/ns.html?id=' \
           '' + gtm + '"\nheight="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n<!-- ' \
                      'End Google Tag Manager (noscript) -->'
    print('Zapisywanie kodów...\n')
    print('\thead:\n' + head)
    print('\tbody:\n' + body + '\n')
    keys.writelines('\nhead:\n' + head + '\n\n')
    keys.writelines('body:\n' + body + '\n\n')
    keys.close()

    okey = ''
    while True:
        try:
            btns = browser.find_elements_by_tag_name('button')
            i = 0
            while btns[i].text != 'OK':
                i = i + 1
                okey = btns[i]
            okey.click()
            break
        except:
            sleep(1)

    if config.get('domain', 'manyUAs') != '1':
        print('Dodawanie nowego tagu...')
        while True:
            try:
                browser.find_element_by_link_text('Dodaj nowy tag').click()
                break
            except:
                sleep(1)
        while True:
            try:
                browser.find_element_by_class_name('gtm-veditor-section-overlay').click()
                break
            except:
                sleep(1)

        while True:
            try:
                browser.find_element_by_class_name('blg-body-and-caption').click()
                break
            except:
                sleep(1)

    # -------  dodawanie zmiennych
    variable_id = 1
    if config.get('domain', 'alreadyHaveUA') == '1':
        ua_key = config.get('domain', 'ua')
        new_variable(browser, ua_key, variable_id)
    elif config.get('domain', 'manyUAs') == '1':
        uas_file = open('ua_keys.txt', 'r')
        lines = uas_file.readlines()
        ua_counter = 0
        for line in lines:
            if list(line)[0] != '#':
                if ua_counter > 0:
                    browser.refresh()
                print('Dodawanie nowego tagu...')
                while True:
                    try:
                        browser.find_element_by_link_text('Dodaj nowy tag').click()
                        break
                    except:
                        sleep(1)
                while True:
                    try:
                        browser.find_element_by_class_name('gtm-veditor-section-overlay').click()
                        break
                    except:
                        sleep(1)
                while True:
                    try:
                        browser.find_element_by_class_name('blg-body-and-caption').click()
                        break
                    except:
                        sleep(1)
                ua_counter = ua_counter + 1
                ua_key = line.split('\n')
                ua_key = ua_key[0]
                new_variable(browser, ua_key, variable_id)
                while True:
                    try:
                        browser.find_elements_by_class_name('gtm-veditor-section-overlay')[1].click()
                        break
                    except:
                        sleep(1)
                browser.find_elements_by_class_name('trigger-picker-row')[1].click()
                while True:
                    try:
                        browser.find_element_by_class_name('left-spacer').click()
                        break
                    except:
                        sleep(1)
                while True:
                    try:
                        browser.find_element_by_class_name('gtm-ng-dialog-footer').\
                            find_element_by_class_name('btn-action').click()
                        break
                    except:
                        sleep(1)
    else:
        new_variable(browser, ua_key, variable_id)

    if config.get('domain', 'manyUAs') != '1':
        while True:
            try:
                browser.find_elements_by_class_name('gtm-veditor-section-overlay')[1].click()
                break
            except:
                sleep(1)
        browser.find_elements_by_class_name('trigger-picker-row')[1].click()
        while True:
            try:
                browser.find_element_by_class_name('left-spacer').click()
                break
            except:
                sleep(1)
        while True:
            try:
                browser.find_element_by_class_name('gtm-ng-dialog-footer').find_element_by_class_name('btn-action')\
                    .click()
                break
            except:
                sleep(1)

    print('Publikowanie tagu...')
    while True:
        try:
            browser.find_element_by_class_name('gtm-container-page-header__toolbar').find_elements_by_tag_name(
                'button')[1].click()
            break
        except:
            sleep(1)
    while True:
        try:
            browser.find_element_by_class_name('gtm-sheet-header__actions').find_element_by_tag_name('button').click()
            break
        except:
            sleep(1)
    browser.find_element_by_class_name('gtm-ng-dialog-footer').find_element_by_tag_name('button').click()

    while True:
        try:
            if 'Wersja' in browser.find_element_by_class_name('blg-title').text:
                print('Tagi zapisane')
                break
        except:
            sleep(1)
