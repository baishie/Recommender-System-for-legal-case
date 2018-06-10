from django import forms

class SubmitForm(forms.Form):
	facts = forms.CharField(widget=forms.Textarea(attrs={'class':'facts-input','placeholder':'Please Enter Facts'}))

