from django.contrib import admin

from .models import Logo

admin.site.register(Logo)

from .models import WhatsAppIcon

admin.site.register(WhatsAppIcon)

from .models import Product

admin.site.register(Product)

from .models import ContactInfo

admin.site.register(ContactInfo)