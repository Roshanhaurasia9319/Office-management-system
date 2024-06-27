import random
import string
from django.core.mail import send_mail
from django.conf import settings


def generate_otp(length=4):
    digits = string.digits
    otp = ''.join(random.choices(digits, k=length))
    return otp


def send_otp(email, otp):
    subject = 'Your Otp Code'
    message = f'Your Otp Code is {otp}. It is valid for 10 minutes'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

