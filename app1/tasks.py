from project.celery import app
import datetime
from django.core.mail import send_mail
from django.conf import settings
from .models import profile

@app.task(name="send_notification")
def send_notification():
    try:
        time_thresold = datetime.now() - datetime.timedelta(minutes=10)
        profile_objs = profile.objects.filter(is_verified=False, created_at_gte=time_thresold)

        for profile_obj in profile_objs:
            subject = 'How are you'
            message = 'Message is sent'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [profile_obj.email]
            send_mail(subject, message, email_from, recipient_list)

    except Exception as e:
        print(e)





