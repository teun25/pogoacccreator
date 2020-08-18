while True:
    try:
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        from selenium.webdriver.common.action_chains import ActionChains
    except:
        print('Failed to import selenium tools, retrying...')
        continue
    else:
        print('Selenium import success!')
        break

while True:
    try:
        #locatie firefox
        binary = FirefoxBinary('D:\\Program Files\\Mozilla Firefox\\firefox.exe')
        #locatie geckodriver
        browser = webdriver.Firefox(firefox_binary=binary, executable_path=r'D:\\geckodriver.exe')
    except:
        print('Open browser error: An error occured, retrying..')
        continue
    else:
        print('Success!')
        break  


browser.get('https://club.pokemon.com/us/pokemon-trainer-club/sign-up/')