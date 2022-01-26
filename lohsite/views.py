from django.shortcuts import render, HttpResponse
from datetime import datetime
from lohsite.models import Contact,Donate
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail

from django.template.loader import render_to_string




def index(request):
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       query = request.POST.get('query')
       submit = Contact(name=name, email=email, query=query, date=datetime.today())
       submit.save()
       messages.success(request, 'Profile details updated.')
    return render(request,'index.html')

def donate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        money=int(request.POST.get('money'))*100
        # print(name,email,phone,money)
        client= razorpay.Client(auth=("rzp_test_QjQaIruAHkIeuC" , "T2F5lhIpTdMDubb3NTnckfS1"))
        payment = client.order.create({'amount': money, 'currency':'INR','payment_capture': '1'})
        # print(payment)
        fill=Donate(name=name,email=email,phone=phone,money=money,payment=payment['id'],date=datetime.today())
        fill.save()
        return render(request, 'donte.html',{'payment':payment})

    return render(request,'donte.html')

@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        # print(a)


        order_id= ""

        for key,value in a.items():
            if key == "razorpay_order_id":
                order_id=value
                break
        # print(order_id)

        user=Donate.objects.filter(payment=order_id).first()
        user.paid=True
        user.save()
        msg_plain = render_to_string('email.txt')
        msg_html= render_to_string('email.html')
        send_mail("your donation has been recieved",msg_plain,settings.EMAIL_HOST_USER,
                  [f'{user.email}'] , html_message = msg_html )
    return render(request,'success.html')