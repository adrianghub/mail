# mail sending
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# env variables
from dotenv import load_dotenv
from os import getenv

# templates
import jinja2

load_dotenv()

class GmailAdapter:
  def __init__(
    selt, 
    host:str, 
    port:int, 
    username:str, 
    password:str
  ):
  self.host = host
  self.port = port
  self.username = username
  self.password = password
  self.server = smtplib.SMTP_SSL(host, post)

  def login(self): 
    self.server.ehlo()
    self.server.login(self.username, self.password)
  
  def __del__(self):
    self.server.close()