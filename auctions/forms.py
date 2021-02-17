from django.forms import ModelForm
from .models import Listing

class CreateListing(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'