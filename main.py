# mail sending
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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