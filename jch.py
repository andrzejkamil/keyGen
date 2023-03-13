from time import *


def table_search(browser, domain):
    table_rows = browser.find_elements_by_tag_name('tr')
    for row in table_rows:
        cols = row.find_elements_by_tag_name('td')
        for td in cols:
            if td.text == domain:
                return cols[0].text
    return ''


def jch_login(browser, config):
    while True:
        try:
            login_txt_box = browser.find_element_by_name('username')
            login_txt_box.clear()
            login_txt_box.send_keys(config.get('pass', 'jchLog'))
            pass_txt_box = browser.find_element_by_name('password')
            pass_txt_box.clear()
            pass_txt_box.send_keys(config.get('pass', 'jchPass'))
            checkbox = browser.find_element_by_id('remember')
            checkbox.click()
            log_btn = browser.find_element_by_class_name('btn-primary')
            log_btn.click()

            sleep(1)
        except:
            break


def jch(browser, config, keys, domain):
    print('Logowanie do jch...')
    browser.get(config.get('urls', 'jch'))
    jch_login(browser, config)
    print('Generowanie klucza jch...')
    browser.get('https://www.jch-optimize.net/myaccount/add-on-download-ids.html')
    try:
        input_txt_box = browser.find_element_by_name('label')
    except:
        jch_login(browser, config)
        input_txt_box = browser.find_element_by_name('label')
    input_txt_box.clear()
    input_txt_box.send_keys(domain)
    input_txt_box.submit()
    while True:
        try:
            key = table_search(browser, domain)
            break
        except:
            sleep(1)
    if key == '':
        add_btn = browser.find_element_by_partial_link_text('New')
        add_btn.click()
        label = browser.find_element_by_name('label')
        label.clear()
        label.send_keys(domain)
        submit = browser.find_element_by_class_name('akeeba-btn')
        submit.click()
    while True:
        try:
            key = table_search(browser, domain)
            break
        except:
            sleep(1)
    keys.writelines('jch:\t\t' + key + '\n')
    print('Generowanie klucza zakończone')
