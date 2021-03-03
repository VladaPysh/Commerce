from django.forms import ModelForm, Textarea, NumberInput
from .models import Listing, Comment, Bid

class CreateListing(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'image', 'category']
        widgets = {
            'title': Textarea(attrs={'cols': 50, 'rows': 1}),
            'description': Textarea(attrs={'cols': 45, 'rows': 4}),
            'price': NumberInput(attrs={"class": "form-control mt-4"})
        }

class LeaveComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment']

class Bid(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']