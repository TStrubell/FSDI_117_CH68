from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'pages/home.html')

def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')

        full_message = f"From: {name} <{email}>\n\n{message_body}"

        send_mail(
            subject=subject,
            message=full_message,
            from_email='no-reply@strubellpublishing.com',  # or your configured from address
            recipient_list=['tim.strubell@icloud.com'],
        )

        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact')

    return render(request, 'pages/contact.html')
