from time import *


def firewall(browser, config, keys, domain):
    browser.get(config.get('urls', 'rs'))
    print('Logowanie do rsJoomla...')
    while True:
        try:
            username = browser.find_element_by_name('username')
            username.clear()
            username.send_keys(config.get('pass', 'firewallLog'))
            password = browser.find_element_by_name('passwd')
            password.clear()
            password.send_keys(config.get('pass', 'firewallPass'))
            login_btn = browser.find_element_by_name('Submit')
            login_btn.click()
            break
        except:
            try:
                browser.get('https://www.rsjoomla.com/customer-login.html')
                logout = browser.find_element_by_name('Submit')
                logout.click()
            except:
                sleep(1)

    print('Generowanie klucza rsFirewall...')
    browser.get('https://www.rsjoomla.com/my-memberships/add-new-license/162131.html?tmpl=component')
    while True:
        try:
            domain_txt_box = browser.find_element_by_name('domain')
            break
        except:
            try:
                username = browser.find_element_by_name('username')
                username.clear()
                username.send_keys(config.get('pass', 'firewallLog'))
                password = browser.find_element_by_name('passwd')
                password.clear()
                password.send_keys(config.get('pass', 'firewallPass'))
                login_btn = browser.find_element_by_name('Submit')
                login_btn.click()
                browser.get('https://www.rsjoomla.com/my-memberships/add-new-license/162131.html?tmpl=component')
            except:
                browser.get('https://www.rsjoomla.com/my-memberships/add-new-license/162131.html?tmpl=component')
    domain_txt_box.clear()
    domain_txt_box.send_keys(domain)
    save_btn = browser.find_element_by_name('Submit')
    save_btn.click()
    sleep(1)
    # message = browser.find_element_by_id('system-message')
    # if 'Your license has been successfully saved!' in message.find_element_by_tag_name('strong').text:
    #     print('\t' + message.find_element_by_tag_name('strong').text)
    #     rows = browser.find_elements_by_class_name('rsj-no-input')
    #     key = rows[1].text
    #     keys.writelines('firewall:\t' + key + '\n')
    # else:
    #     print('\t' + message.find_element_by_tag_name('strong').text)

    # -------------------- jeśli brak powiadomień
    rows = browser.find_elements_by_class_name('rsj-no-input')
    key = rows[1].text
    keys.writelines('firewall:\t' + key + '\n')
    # -------------------- /jeśli brak powiadomień

    browser.get('https://www.rsjoomla.com/customer-login.html')
    logout = browser.find_element_by_name('Submit')
    logout.click()
    print('Generowanie klucza zakończone')
