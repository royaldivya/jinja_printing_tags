from django.shortcuts import render

# Create your views here.
def send_date(request):
    return render(request,'send_date.html',context={'name':'DIVYA','age':20})