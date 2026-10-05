from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    sent = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_subject = f"[Portfolio Contact] {subject}"
            full_message = f"From: {name} <{email}>\n\n{message}"

            send_mail(
                full_subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['tim.strubell@icloud.com'],
                fail_silently=False,
            )
            sent = True
    else:
        form = ContactForm()

    return render(request, 'contactapp/contact.html', {'form': form, 'sent': sent})
