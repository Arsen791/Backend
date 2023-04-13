from django.forms import Form
from django import forms


class CreateNameForm(Form):
    firstname = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    secondname = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your second name'}))
    
class CreateInfoForm(Form):
    specialization = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    orga_of_education = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    
    year_of_graduation = forms.IntegerField(required=True,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your second name', 'type':'number'}))
    
class CreateBirthForm(Form):
    date_of_birth = forms.DateField(required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter your date of birth', 'type': 'date'}))
    place_of_birth = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your place of birth'}))
    
class CreateWorkForm(Form):
    organization = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your organization '}))
    address = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your place of birth'}))
    
class CreatePracticeForm(Form):
    experience = forms.IntegerField(required=True,
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your experience '}))
    
class CreateCriminalForm(Form):
    criminal_record = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Yes or No   '}))
    
class CreateMedicineForm(Form):
    medicine_number = forms.IntegerField(required=True,
                               widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter your medicine number  '}))
    medicine_date = forms.DateField(required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter your medicine date  ', 'type': 'date'}))
    
