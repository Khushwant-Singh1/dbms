from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('house', 'House'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    size = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amenities = models.ManyToManyField('Amenity', blank=True)

class Photo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='listing_photos/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
