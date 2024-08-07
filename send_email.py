
import smtplib
from email.mime.text import MIMEText

from decouple import config


def send_test_msg(recipient):
    msg = MIMEText("test text message")
    msg['Subject'] = "Sent from python"
    msg['From'] = config('EMAIL_HOST_USER')
    msg['To'] = recipient
    server = smtplib.SMTP_SSL(config('EMAIL_HOST'), config('EMAIL_PORT'))
    server.login(config('EMAIL_HOST_USER'), config('EMAIL_HOST_PASSWORD'))
    server.sendmail(config('EMAIL_HOST_USER'), [recipient], msg.as_string())
    server.quit()


if __name__ == '__main__':
    send_test_msg(str(input('Еnter recipient email: ')))
