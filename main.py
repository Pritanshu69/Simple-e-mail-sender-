import os
from email.message import EmailMessage  # pre-installed python library function
import ssl  # for security
import smtplib

email_sender = ' '    # sender mail in the quote
email_password = ' '  # app password of google here
email_receiver = ' '  # receiver mail in the quote


subject = 'Prototype test'
body = """
Hey how are you?
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender , email_password)
    smtp.sendmail(email_sender, email_receiver , em.as_string())
