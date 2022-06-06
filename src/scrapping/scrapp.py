import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def get_page_with_selenium(url: str):
    """Wrapper over selenium driver.get(url).

    Args:
        url: url to scrap
        secret: if true, call secret_get_page_with_selenium() instead. Safe proxy + user agent.
        scroll: if true, scroll down the page before returning its content. Useful for dynamic web sites.
    """

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.implicitly_wait(30)

    driver.get(url)

    page_source = driver.page_source

    return page_source, driver


def request_mail_from_candilib(mail: str):
  """Fill the request on candilib to recieve a connexion token.

  Args:
    mail: user email to retrieve the token from
  """

  url = "https://beta.interieur.gouv.fr/candilib/qu-est-ce-que-candilib"

  _, driver = get_page_with_selenium(url)

  try:
    # Here we select the 'Déjà inscrit' button
    button = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/main/div/div[2]/div/section/div[1]/button')

    button.click() 

    driver.implicitly_wait(3)

    email_field = driver.find_element(by=By.XPATH, value='//*[@id="input-70"]')
    email_field.send_keys(mail)

    driver.implicitly_wait(2)
    time.sleep(2)

    email_field.send_keys(Keys.ENTER)
    

  except Exception as e:
    print(e)  

  driver.quit()