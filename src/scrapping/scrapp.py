import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def get_first_page_with_selenium(url: str):
    """Wrapper over selenium driver.get(url).

    Args:
        url: url to scrap
    """

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.implicitly_wait(30)

    driver.get(url)

    return driver


def request_mail_from_candilib(mail: str):
  """Fill the request on candilib to recieve a connexion token.

  Args:
    mail: user email to retrieve the token from
  """

  url = "https://beta.interieur.gouv.fr/candilib/qu-est-ce-que-candilib"

  driver = get_first_page_with_selenium(url)

  try:
    # Here we select the 'Déjà inscrit' button
    button = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/main/div/div[2]/div/section/div[1]/button')

    button.click() 

    email_field = driver.find_element(by=By.XPATH, value='//*[@id="input-70"]')
    email_field.send_keys(mail)

    time.sleep(2)

    email_field.send_keys(Keys.ENTER)
    
  except Exception as e:
    print(e)  

  driver.quit()


def log_with_token():
  current_date = datetime.datetime.now().strftime("%Y-%m-%d")

  with open(f'urls/{current_date}', 'r') as file:
    url = file.read()

    return get_first_page_with_selenium(url)
