# env variables
from dotenv import load_dotenv
from os import getenv

# templates
import jinja2

from gmail_adp import GmailAdapter


load_dotenv()

mailer = GmailAdapter(
  host='smtp.gmail.com',
  port=465,
  username=getenv('USERMAIL'),
  password=getenv('PASSWORD')
)

mailer.login()
mailer.send_mail('zinko.adrian00@gmail.com', 'You won 1000$!', '<h1>Hello, brother</h1>')