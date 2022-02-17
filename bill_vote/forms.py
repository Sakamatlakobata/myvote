from .forms_choices import *
from django import forms

class GetBillForm(forms.Form):
    bill_name           = forms.CharField(help_text="Enter bill name")
    status              = forms.ChoiceField(choices=status)
    committee           = forms.ChoiceField(choices=committee)
    policy_area         = forms.ChoiceField(choices=billPolicyArea)
    legislative_subject = forms.ChoiceField(choices=billSubjectTerm)

