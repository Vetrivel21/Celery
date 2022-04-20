from django.contrib import admin
from django.urls import path, include
from task.views import ReviewEmailView
from app.views import send_notification
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', ReviewEmailView.as_view(), name="reviews"),
    path('send_notification', send_notification),
    path('', include('app1.urls')),
]
