while True:
    try:
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        from selenium.webdriver.common.action_chains import ActionChains
        import time
        import random
        import string
        import pyautogui
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
        driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'D:\\geckodriver.exe')
    except:
        print('Open browser error: An error occured, retrying..')
        continue
    else:
        print('Success!')
        break  

def get_random_alphanumeric_string(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Zet de string om naar random letters en cijfers
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

def makeAccount():
    driver.get('https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')
    #voornaam
    voornaam = driver.find_element_by_id("firstName")
    voornaam.clear();
    voornaam.send_keys("Teun");
    #achternaam
    achternaam = driver.find_element_by_id("lastName")
    achternaam.clear();
    achternaam.send_keys("Van den Broek");
    #gmail 
    gmail = driver.find_element_by_id("username")
    gmail.clear();
    randomname = get_random_alphanumeric_string(6, 1)
    gmail.send_keys(randomname)
    #wachtwoord
    wachtwoord = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/div[1]/input")
    wachtwoord.clear();
    wachtwoord.send_keys("scheurneus")
    #herhaal wachtwoord
    wachtwoord = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/div/div[1]/div/div[1]/input")
    wachtwoord.clear();
    wachtwoord.send_keys("scheurneus")
    #druk op 'volgende' knop
    nextbtn = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span").click()
    #open een nieuw tablad met de fake sms site
    driver.execute_script('''window.open("https://www.receivesms.co/us-phone-number/3433/","_blank");''')
    time.sleep(10)
    copynumber = driver.find_element_by_xpath('//div[@class="btn2 h3 font-weight-bold"]').click()
    copynumber.click()
    #kopieer telefoonnummer

    time.sleep(23333)


makeAccount()
