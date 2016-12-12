from django.shortcuts import render

from contact.forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, "contact.html", {
        "form": form
    })
