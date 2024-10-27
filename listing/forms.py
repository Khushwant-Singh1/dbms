from django import forms
from .models import Listing, Photo, Amenity

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'price',
            'location',
            'property_type',
            'size',
            'number_of_rooms',
            'status',
            'amenities'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'amenities': forms.CheckboxSelectMultiple()
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Add a caption...'}),
        }

class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe the amenity...'}),
        }
