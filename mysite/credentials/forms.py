from django import forms
from django.forms import ModelForm,Textarea
from django.core.exceptions import NON_FIELD_ERRORS
from .models import contact,internships


    
    
class contactform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=contact
        widgets={'email':Textarea(attrs={'placeholder':'email','cols': 80, 'rows': 1}),'mobile':Textarea(attrs={'placeholder':'mobile','cols': 80, 'rows': 1}),'temporary_address':Textarea(attrs={'placeholder':'temporary_address','cols': 80, 'rows': 3}),'permanent_address':Textarea(attrs={'placeholder':'permanent address','cols': 80, 'rows': 3}),'website':Textarea(attrs={'placeholder':'link','cols': 80, 'rows': 1}),}
        fields=['email','mobile','temporary_address','permanent_address','website']
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        return email
    
    
class internshipsform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=internships
        
        fields=['field1','field2','field3']
        
