from django.shortcuts import render


# Create your views here.
from newsletter.forms import SignUpFrom


def index(request):
    title = "Hi, %s" % request.user if request.user.is_authenticated() else "Hello"
    form = SignUpFrom(request.POST or None)

    if form.is_valid():
        title = "Thank you for subscribing to our newsletter %s " % form.cleaned_data.get('full_name')
        form.save()
        form = None

    return render(request, 'newsletter.html', {
        "title": title,
        "form": form
    })
