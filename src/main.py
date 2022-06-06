import time
import json
import datetime

from mail.mail_retriever import retrieve_candilib_link
from scrapping.scrapp import request_mail_from_candilib


if __name__ == "__main__":

  with open('ressources/config.json') as file:
    config: dict = json.load(file)
    mail = config["email"]
    password = config["password"]
    host = "imap.gmail.com" if "gmail" in mail else "imap.free.fr"

  request_mail_from_candilib(mail)

  time.sleep(5)

  url_with_token = retrieve_candilib_link(host, mail, password)

  current_date = datetime.datetime.now().strftime("%Y-%m-%d")

  with open(f'urls/{current_date}', 'w') as file:
     file.write(url_with_token)


  print("URL TO USE:")
  print(url_with_token)











