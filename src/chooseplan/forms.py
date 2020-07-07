from django import forms
from .models import demographics
from django.forms import ModelForm

class chooseplanform(forms.ModelForm):
    class Meta:
        model = demographics
        fields = '__all__'
        widgets = {'Gender': forms.RadioSelect, 'Age': forms.RadioSelect, 'Height': forms.RadioSelect,  'Weight': forms.RadioSelect, 'Activity_Level': forms.RadioSelect, \
        'Level_of_excerise': forms.RadioSelect, 'Do_you_smoke': forms.RadioSelect, 'Do_you_take_non_presribed_drugs': forms.RadioSelect, 'Do_you_often_participate_in_sports': \
         forms.RadioSelect, 'Do_you_have_a_labor_intensive_job': forms.RadioSelect, \
         } #START OF SYMPTOMS

#class symptomsplanform(forms.ModelForm):
#    class Meta:
#        model = Symptoms
#        fields = '__all__'
#        widgets = {'Depression': forms.RadioSelect, 'Heart Issues': forms.RadioSelect}
