from django.core.mail import EmailMessage
from django.conf import settings

def emailAlert():
    email = EmailMessage(
            'Cron Job',
            'This mail is a cron remainder',
            settings.EMAIL_HOST_USER,
            ['rashidhussain060998@gmail.com'],
        )
    email.fail_silently = False
    email.send()