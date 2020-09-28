import smtplib

class GmailAdapter:
  def __init__(
    self, 
    host:str, 
    port:int, 
    username:str, 
    password:str
  ):
    self.host = host
    self.port = port
    self.username = username
    self.password = password
    self.server = smtplib.SMTP_SSL(host, port)

  def login(self): 
    self.server.ehlo()
    self.server.login(self.username, self.password)
  
  def __del__(self):
    self.server.close()