from time import *
from selenium.webdriver.common.by import By

def api(browser, config, keys, domain):
    print('Otwieranie Google Cloud Platform...')
    browser.get(config.get('urls', 'api'))

    restrict_key = ''
    add_el = ''
    done = ''
    save = ''

    print('Sprawdzanie miejsca na klucze API...')
    for i in range(0, 5):
        try:
            if config.get('apiLimit', 'on') == '1':
                pagination_page = browser.find_element_by_class_name('cfc-table-pagination-page-info')
                keys_amount = pagination_page.find_element_by_class_name('ng-star-inserted')
                keys_amount = keys_amount.text.replace('of ', '')
                keys_amount = int(keys_amount)
                if keys_amount >= int(config.get('apiLimit', 'limit')):
                    print('\t---UWAGA NA TYM PROJEKCIE API JEST JUŻ ' + str(keys_amount) + ' KLUCZY---')
                    keys.writelines('\t---UWAGA NA TYM PROJEKCIE API JEST JUŻ ' + str(keys_amount) + ' KLUCZY---\n')
            break
        except:
            sleep(1)

    print('Ładowanie listy kluczy...')
    rows = browser.find_elements_by_tag_name('tr')
    while True:
        try:
            i = 0
            while 'HTTP referrers' not in rows[i].text:
                i = i + 1
            break
        except:
            rows = browser.find_elements_by_tag_name('tr')

    print('Tworzenie klucza API...')
    create_btn = browser.find_element_by_id('_0rif_action-bar-create-button')
    create_btn.click()
    sleep(2)
    #while True:
     #   try:
      #      add = browser.find_element_by_id('action-bar-create-button')
       #     add.click()
        #    break
        #except:
         #   sleep(1)
    print('Dodawanie klucza...')
    add_api_key = browser.find_elements_by_class_name('cfc-menu-item-label')
    add_api_key = add_api_key[0]
    sleep(2)
    add_api_key.click()
    i = 0
    print('Ograniczanie klucza...')
    sleep(10)
    # while True:
    #     try:
    #         print("tu dziala")
    #         try:
    #             while browser.find_elements_by_tag_name('button')[i].text != 'Close' and \
    #                     browser.find_elements_by_tag_name('button')[i].text != 'Zamknij':
    #                 try:
    #                     print("tu dziala tez")
    #                     restrict_key = browser.find_by_css_selector('a.cfc-ng2-region')[i]
    #                     i = i + 1
    #                     print(restrict_key.text)
    #                 except:
    #                     sleep(1)
    #         except:
    #             restrict_key.click()
    #             print('Kliknalem')
    #         break
    #     except:
    #         sleep(1)
    key_value = browser.find_element_by_id('_0rif_mat-input-0').get_attribute('value')
    print(key_value)

    keys.writelines('api:\t\t' + key_value + '\n')
    sleep(2)
    edit_key=browser.find_element_by_link_text("Edit API key")
    edit_key.click()

    # edit_api = browser.find_element_by_link_text("Edit API key")
    # edit_api.click()

    print('Dodawanie domeny...')
    while True:
        try:
            name = browser.find_element_by_name('displayName')
            name.clear()
            name.send_keys(domain)
            break
        except:
            sleep(1)
    browser.find_element_by_id('_0rif_mat-radio-3').click()

    print('Dodawanie elementów...')
    # while True:
    #      try:
    #          btns = browser.find_elements_by_class_name('cfc-form-list-new-item-text')
    #          i = 0
    #          while btns[i].text != 'DODAJ ELEMENT' and btns[i].text != 'ADD AN ITEM':
    #              i = i + 1
    #              add_el = btns[i]
    #          add_el.click()
    #          break
    #      except:
    #       sleep(1)
    btns = browser.find_elements_by_class_name('cfc-form-list-new-item-text')
    btns[0].click()
    new_el = browser.find_element_by_name('referrerInput')
    new_el.send_keys('http://' + domain + '/*')
    doneBtns = browser.find_elements_by_class_name('mat-button-wrapper')
    for btn in doneBtns:
        if btn.text == 'Done' or btn.text == 'DONE' or btn.text == 'GOTOWE':
            btn.click()
    # while True:
    #     try:
    #          btns = browser.find_elements_by_class_name('mat-button-wrapper')
    #          i = 0
    #          while btns[i].text != 'GOTOWE' and btns[i].text != 'DONE':
    #            i = i + 1
    #             done = btns[i]
    #             done.click()
    #          break
    #     except:
    #          sleep(1)
    #     donebtn = browser.find_elements_by_class_name("mdc-button__label")

    #donebtn[5].click()
    # btns = browser.find_elements_by_class_name('cfc-form-list-new-item-text')
    #
    # btns[0].click()
    btns = browser.find_elements_by_class_name('cfc-form-list-new-item-text')
    btns[0].click()
    new_el = browser.find_elements_by_name('referrerInput')
    new_el = new_el[1]
    new_el.send_keys('*.' + domain + '/*')
    sleep(1)

    doneBtns2 = browser.find_elements_by_class_name('mat-button-wrapper')
    for btn in doneBtns2:
        if btn.text == 'Done' or btn.text == 'DONE' or btn.text == 'GOTOWE':
            btn.click()

    # btns = browser.find_elements_by_class_name('mat-button-wrapper')
    # i = 0
    # while btns[i].text != 'GOTOWE' and btns[i].text != 'DONE':
    #     i = i + 1
    #     done = btns[i]
    # done.click()

    #key_value = browser.find_element_by_id('_0rif_mat-input-1').get_attribute('value')
    #print(key_value)

    #keys.writelines('api:\t\t' + key_value + '\n')

    saveButtons = browser.find_elements_by_class_name("mdc-button__label")

    print('Zapisywanie...')
    i = 0
    while saveButtons[i].text != 'ZAPISZ' and saveButtons[i].text != 'SAVE' and saveButtons[i].text != 'Save':
        i = i + 1
        save = saveButtons[i]
    save.click()
    print(f'Generowanie klucza {key_value} zakończone')
    sleep(2)
