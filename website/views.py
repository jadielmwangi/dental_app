from django.shortcuts import render
from django.core.mail import send_mail
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog_details(request):
    return render(request, 'blog_details.html' , {})



def contact(request):
    if request.method == "POST":

        message_name =request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'Message from:' +  message_name, # subject
            'The message is:' + message, # message
            message_email, # from email
            ['jedielmwangi@gmail.com'], # to Email

        )

        return render(request, 'contact.html', {'message_name' : message_name})


    else: 

        return render(request, 'contact.html', {})

