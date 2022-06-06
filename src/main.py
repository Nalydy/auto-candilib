import time
import json
import datetime
import concurrent.futures

from mail.mail_retriever import retrieve_candilib_link
from scrapping.scrapp import request_mail_from_candilib, log_with_token


def retrieve_candilib_token(host: str, mail: str, password: str):

  request_mail_from_candilib(mail)

  # Wait to be sure we recieved the mail
  time.sleep(5)

  url_with_token = retrieve_candilib_link(host, mail, password)

  with open(f'urls/{datetime.datetime.now().strftime("%Y-%m-%d")}', 'w') as file:
     file.write(url_with_token)


def thread_function(interest: str, id: int):

  # So all threads don't start at the same time and spam candilib (may be safer this way)

  time.sleep(id)

  if id == 1:

    department, city, month = interest.values()

    print(f"starting thread {id} : {department}, {city}, {month}")

    driver = log_with_token()

    driver.get(f"https://beta.interieur.gouv.fr/candilib/candidat/{department}/{city}/{month}/undefinedDay/selection/selection-place")

    while True:
      # TODO : check and detect if there are exams possible
      time.sleep(1)



if __name__ == "__main__":

  with open('ressources/config.json') as file:
    config: dict = json.load(file)
    mail = config["email"]
    password = config["password"]
    host = "imap.gmail.com" if "gmail" in mail else "imap.free.fr"
    interests = config["interests"]

  retrieve_candilib_token(host, mail, password)

  nb_threads = len(interests)

  with concurrent.futures.ThreadPoolExecutor(max_workers=nb_threads) as executor:
    executor.map(thread_function, interests, range(nb_threads))

  # Keep alive
  while True:
    time.sleep(1)













