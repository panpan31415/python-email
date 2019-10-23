import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path("index.html").read_text())

email = EmailMessage()
email["from"] = "Panpan Zhang"
email["to"] = "panpan@motosumo.com"
email["subject"] = "test python email"

email.set_content(html.substitute({"name", "panpan"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # say hello
    smtp.starttls()  # encryption
    smtp.login("panpan31415@gmail.com", "***************")
    smtp.send_message(email)
    print("email sent!")
