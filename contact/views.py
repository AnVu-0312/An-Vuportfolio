from django.shortcuts import render
from .forms import ContactForm

<<<<<<< HEAD
def contact_view(request):
    return HttpResponse("Contact app works!")
=======

def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
>>>>>>> parent of affdaf0 (Update contact button)
# Create your views here.
