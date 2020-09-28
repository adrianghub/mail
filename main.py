# env variables
from dotenv import load_dotenv
from os import getenv

from gmail_adp import GmailAdapter
from messages import ClickbaitMessage

load_dotenv()

mailer = GmailAdapter(
  host='smtp.gmail.com',
  port=465,
  username=getenv('USERMAIL'),
  password=getenv('PASSWORD')
)
mailer.login()

clickbait = ClickbaitMessage()

mailer.send_mail(
  recipient_email='zinko.adrian00@gmail.com', 
  subject='You won 1000$!', 
  content=clickbait.render(name='Bruhhh')
  )