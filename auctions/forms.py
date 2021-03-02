from django.forms import ModelForm
from .models import Listing, Comment, Bid

class CreateListing(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'image', 'category']
        
        def __init__(self, *args, **kwargs):
            super(CreateListing, self).__init__(*args, **kwargs)
            self.fields['price'].widget.attrs['min'] = 10

class LeaveComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment']

class Bid(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']