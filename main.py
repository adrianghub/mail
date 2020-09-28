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