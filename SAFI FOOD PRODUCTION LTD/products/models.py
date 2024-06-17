from django.db import models


class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.alt_text or "Logo"

class WhatsAppIcon(models.Model):  # Changed 'models.model' to 'models.Model'
    image = models.ImageField(upload_to='whatsapp_icons/')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
    

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # Assuming a maximum length for the phone number

    def __str__(self):
        return f"{self.email} - {self.phone}"
