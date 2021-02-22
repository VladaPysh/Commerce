from django.forms import ModelForm
from .models import Listing, Comment

class CreateListing(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'start_bid', 'image', 'category']

class LeaveComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']