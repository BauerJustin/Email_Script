import smtplib, ssl, csv

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "your_email@gmail.com"
password = "your_password"

def send_email(name, receiver_email):
    message = MIMEMultipart("alternative")
    message["Subject"] = "your_subject"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    your_message
    """
    html = """\
    <html>
      <body>
        <p>
            your_message
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Success sending to " + name + " at " + email)

with open("emails.txt") as file:
    csv_reader = csv.reader(file)
    for name, email in csv_reader:
        send_email(name, email)
