from django.urls import path
from .views import sendmail,History,mail
urlpatterns = [
    path('newmail',sendmail,name='sendmail'),
    path('',History,name='history'),
    path('history/<int:id>', mail, name='index'),
]
