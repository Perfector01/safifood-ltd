from django.urls import path
from . views import home, about,contact_us,tenders,products, contact_view
from products import views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact_us, name='contact'),
    path('Tenders/', tenders, name='tenders'),
    path('products/', products, name='products'),

]
