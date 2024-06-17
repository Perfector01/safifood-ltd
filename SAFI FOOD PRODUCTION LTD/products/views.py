from django.shortcuts import render
from django.http import HttpResponse
from .models import Logo, WhatsAppIcon, Product
from .models import ContactInfo


def home(request):

    return render(request, 'index.html',)

def about(request):
    logos = Logo.objects.all()
    return render(request, 'about.html', {'logos':logos})


def contact_us(request):
    whatsapp_icons = WhatsAppIcon.objects.all()
    logos = Logo.objects.all()
    context = {'whatsapp_icons': whatsapp_icons, 'logos':logos}
    return render(request, 'contact_us.html', context )


def contact_view(request):
    # Assuming there's only one contact info record
    contact_info = ContactInfo.objects.first()
    return render(request, 'contact_us.html', {'contact_info': contact_info})


def tenders(request):
    logos = Logo.objects.all()
    return render(request, 'tenders.html', {'logos':logos})


def home(request):
    products = Product.objects.all()
    logos = Logo.objects.all()
    context = {'products':products, 'logos':logos}
    return render(request, 'home.html',  context)


def products(request):
    logos = Logo.objects.all()
    return render(request, 'products.html', {'logos':logos})


def navigation_view(request):
    logos = Logo.objects.all()  # Note the parentheses after all
    return render(request, 'nav.html', {'logos': logos})
