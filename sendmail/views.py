from sqlite3 import Date
from django.shortcuts import render
from .models import UserMail
from django.core.mail import send_mail
from django.conf import settings
import datetime
# Create your views here.
def sendmail(request):
    data = reversed(UserMail.objects.all())
    # run = True
    # if l==0:
    #     run = False
    if request.method == 'POST':
        From = request.POST['from']
        to = list(request.POST['to'].split())
        sub = request.POST['sub']
        msg = request.POST['message']

        data = UserMail(FromMail = From,ToMail = to,Subject = sub,Message = msg,Date = datetime.datetime.now())
        data.save()
        print(data.Date)
        send_mail(sub,msg,settings.EMAIL_HOST_USER,to,fail_silently=False)
        
        return render(request,'main.html')
    else:
        return render(request,'main.html',{'data':data})
def History(request):
    data = reversed(UserMail.objects.all())
    # l = len(data)
    # run = True
    # if l==0:
    #     run = False
    # print(data)
    return render(request,'history.html',{'data':data})
def mail(request,id):
    data = reversed(UserMail.objects.all())
    print(data)
    data1 = UserMail.objects.get(id=id)
    return render(request,'mail.html',{'data':data,'data1':data1})