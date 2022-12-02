from django.contrib import admin
from django.urls import path

from website.views import welcome, date, about
from meetings.views import detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('date', date),
    path('about', about),
    path('meeting/<int:room_id>', detail)
]
