from django import forms

from portfolio.models import Contact



class FeedbackForm (forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
