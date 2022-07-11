from django import forms

class BinarySearchForm(forms.Form):
    number = forms.IntegerField(label='Number')

class LowerBoundForm(forms.Form):
    number = forms.IntegerField(label='Number')

class UpperBoundForm(forms.Form):
    number = forms.IntegerField(label='Number')

class KMPForm(forms.Form):
    needle = forms.CharField(max_length=120, label='')

