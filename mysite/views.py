from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def index(request):
    return render(request=request, template_name="index.html")


def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)