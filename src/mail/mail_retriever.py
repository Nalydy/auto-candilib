import easyimap
import re

def retrieve_candilib_link(host: str, mail: str, password: str):
  server = easyimap.connect(host, mail, password)
  email = server.mail(server.listids()[0])
  return re.findall("\[(.*?=.*?)\]", email.body)[0]


