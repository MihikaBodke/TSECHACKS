from django import forms
from basicFuns.models import *


class CreateReminderForm(forms.ModelForm):
    class Meta:
        model = Reminders
        exclude = ['patient']



class EnterQuestionsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        exclude = ['patient']