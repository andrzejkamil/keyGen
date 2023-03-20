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
    sleep(5)

    key_value = browser.find_element_by_id('_0rif_mat-input-0').get_attribute('value')
    print(key_value)

    keys.writelines('api:\t\t' + key_value + '\n')
    sleep(1)
    edit_key=browser.find_element_by_link_text("Edit API key")
    edit_key.click()


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
    sleep(1)
    print('Dodawanie elementów...')
    sleep(2)
    add_btn = browser.find_element(By.XPATH, "//button[@aria-label='Add']")
    add_btn.click()
    print("klika")
    sleep(1)
    new_el = browser.find_element_by_name('referrerInput')
    new_el.send_keys('http://' + domain + '/*')
    sleep(1)
    doneBtns = browser.find_elements_by_xpath("//*[@class='mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base cm-button']")
    print(doneBtns)
    for btn in doneBtns:
        if btn.text == 'Done' or btn.text == 'DONE' or btn.text == 'GOTOWE':
            btn.click()
            sleep(1)

    #add_btn=browser.find_element(By.XPATH("/html/body/pan-shell/pcc-shell/cfc-panel-container/div/div/cfc-panel[1]/div/div/div[3]/cfc-panel-container/div/div/cfc-panel/div/div/cfc-panel-container/div/div/cfc-panel[1]/div/div/cfc-panel-container/div/div/cfc-panel[2]/div/div/central-page-area/div/div/pcc-content-viewport/div/div/pangolin-home/cfc-router-outlet/div/ng-component/cfc-single-panel-layout/cfc-panel-container/div/div/cfc-panel/div/div/services-api-key-details-page/apikey-details/cfc-panel-body/cfc-virtual-viewport/div[1]/div/cfc-column-layout/div/cfc-main-column/cfc-panel-body/cfc-virtual-viewport/div[1]/div/form/div[2]/services-key-browser-restrictions/div/services-app-restrictions-table/cfc-table/div[1]/span/cfc-table-action-container/button"))
    add_btn = browser.find_element(By.XPATH, "//button[@aria-label='Add']")
    add_btn.click()
    sleep(1)
    new_el = browser.find_elements_by_name('referrerInput')
    new_el = new_el[0]
    new_el.send_keys('*.' + domain + '/*')
    sleep(1)
    doneBtns = browser.find_elements_by_xpath("//*[@class='mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base cm-button']")
    for btn in doneBtns:
        if btn.text == 'Done' or btn.text == 'DONE' or btn.text == 'GOTOWE':
            btn.click()
            sleep(1)
    #doneBtn.click()
    saveButtons = browser.find_elements_by_class_name("mdc-button__label")

    print('Zapisywanie...')
    i = 0
    while saveButtons[i].text != 'ZAPISZ' and saveButtons[i].text != 'SAVE' and saveButtons[i].text != 'Save':
        i = i + 1
        save = saveButtons[i]
    save.click()
    print(f'Generowanie klucza {key_value} zakończone')
    sleep(2)
