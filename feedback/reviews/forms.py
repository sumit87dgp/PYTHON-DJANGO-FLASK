from pyexpat import model
from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100,error_messages={
#         "required" : "Your name must not be empty",
#         "max_length" : "Please enter at max of 100 characters"
#     })
#     review_text =  forms.CharField(label="Your Feedback", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=5)

# Example of Modelforms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review # Don't instantiate. Just point
        fields = '__all__'

        #excelude = ['owner']