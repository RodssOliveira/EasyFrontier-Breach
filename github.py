from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

import time, os
from tqdm import tqdm

def crawler(email):
    url = 'https://github.com/search?q={}&type=code'.format(email)

    pbar = tqdm(total=3)
    pbar.set_description('Entrando no GitHub')

    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    
    time.sleep(10)

    pbar.set_description('Efetuando Autenticação')
    pbar.update(1)

    login_field = driver.find_element_by_id('login_field')
    login_field.send_keys('EasyFrontier-Dummy')

    password_field = driver.find_element_by_id('password')
    password_field.send_keys("'Fiap.20")

    entrar_btn = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')
    entrar_btn.click()

    pbar.set_description('Verificando se email existe no Site')
    pbar.update(1)
    
    time.sleep(10)

    result = driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div[2]/nav[1]/a[2]/span')
    result = result.text

    pbar.set_description('Finalizado')
    pbar.update(1)

    driver.close()
    pbar.close()


    return result
    

def getPass():
    PRIVATE_KEY = os.environ['EasyFrontier']
    return PRIVATE_KEY
    


if __name__ == '__main__':
    email = 'easyfrontier@fiap.com.br'
    crawler(email)
        
        
