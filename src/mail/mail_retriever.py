import easyimap
import re

def retrieve_candilib_link(host, mail, password):
  server = easyimap.connect(host, mail, password)
  email = server.mail(server.listids()[0])
  return re.findall("\[(.*?=.*?)\]", email.body)[0]


