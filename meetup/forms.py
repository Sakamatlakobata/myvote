# from .forms_choices import *
from django import forms

class GetZIPcode(forms.Form):
    # ZIPcode = forms.IntegerField(label="ZIP code")
    # ZIPcode = forms.IntegerField(min_value='00001', label="ZIP code") # '<' not supported between instances of 'int' and 'str'
    # ZIPcode = forms.IntegerField(min_value='00001', max_value='99999', label="ZIP code") # '<' not supported between instances of 'int' and 'str'
    ZIPcode = forms.CharField(max_length=5, label="ZIP code")
