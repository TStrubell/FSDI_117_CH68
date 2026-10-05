from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _

from .forms import ContactForm
from .models import Project, Skill


def home_view(request):
    """
    Displays the SGnG home page.
    """
    return render(request, 'portfolio/home.html')

def about_view(request):
    """
    Displays information about the user.
    """
    return render(request, 'portfolio/about_me.html')

def experience_view(request):
    """
    Displays the user's professional experience.
    """
    return render(request, 'portfolio/experience.html')

def contact_view(request):
    """
    SGnG Contact Page:
    Displays a contact form and sends an email using django.core.mail when submitted.
    """
    success = None
    success_message = None

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data["first_name"]
            last = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            full_subject = f"[SGnG Portfolio] {subject}"
            full_message = (
                f"New message from SGnG portfolio contact form:\n\n"
                f"Name: {first} {last}\n"
                f"Email: {email}\n\n"
                f"Message:\n{message}"
            )

            # SEND EMAIL USING DJANGO.CORE.MAIL
            send_mail(
                full_subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            # TRANSMIT SUCCESS MESSAGE
            success = True
            success_message = _("Your message has been sent successfully.")

            return render(request, "portfolio/contact.html", {
                "form": ContactForm(),
                "success": success,
                "success_message": success_message,
            })

        else:
            # FORM INVALID
            success = False
            success_message = None
            return render(request, "portfolio/contact.html", {
                "form": form,
                "success": success,
                "success_message": success_message,
            })

    else:
        form = ContactForm()

    return render(request, "portfolio/contact.html", {
        "form": form,
        "success": success,
        "success_message": success_message,
    })

def projects_view(request):
    """
    Displays all projects stored in the database.
    """
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def skills_view(request):
    """
    Displays all skills stored in the database.
    """
    skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skills})
