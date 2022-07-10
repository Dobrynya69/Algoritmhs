from django import forms

class BinarySearchForm(forms.Form):
    number = forms.IntegerField(label="Number")

class LowerBoundForm(forms.Form):
    number = forms.IntegerField(label="Number")

class UpperBoundForm(forms.Form):
    number = forms.IntegerField(label="Number")
