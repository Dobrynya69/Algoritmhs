from django import forms

class BinarySearch(forms.Form):
    number = forms.IntegerField(label="Number")

class SearchUppercase(forms.Form):
    string = forms.CharField(max_length=50, label="String")