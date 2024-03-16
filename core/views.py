from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    name = 'prime'

    if request.method == 'POST':
        title = request.POST.get('title')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Email: {email}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        # send_mail(title,message,'settings.EMAIL_HOST_USER',[email],fail_silently=False)
        send_mail(
            subject= title,
            message= message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list= [email],
            fail_silently= False
        )

    return render(request, 'home.html', {
        'name': name,
    })


