from django.shortcuts import render
from django.http.response import HttpResponse
from .tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
# Create your views here.
def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=21, minute = 1)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"12", task='mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")
