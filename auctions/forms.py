from django.forms import ModelForm, Textarea, NumberInput, TextInput
from .models import Listing, Comment, Bid

class CreateListing(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'image', 'category']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': '5'})
        }

class LeaveComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment']
        widgets = {
            'subject': TextInput(attrs={'class': 'form-control'}),
            'comment': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }

class Bid(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']