def check_headless(config):
    headless = config.get('client', 'headless')

    if headless == 'True':
        headless = True
    else:
        headless = False
    return headless
