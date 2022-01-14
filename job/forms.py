from django import forms
from .models import *
from django.contrib.auth.models import User


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['category', 'title' , 'description','prequests',
                  'benefits','job_type','created_by','salary',
                  'vacancy','logo','supervisor',
                  'location' ]
        
class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['title','image','location','description']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
          
class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class CandidateRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Candidates
        fields = [
            'username',
            'full_name',
            'email',
            'password',
            'address'
        ]
    def clean_username(self):
        user_name = self.cleaned_data["username"]
        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError("Candidate with this username already exists.")
        return user_name

class CandidateLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_username(self):
        user_name = self.cleaned_data["username"]
        if User.objects.filter(username=user_name).exists():
           pass
        else:
            raise forms.ValidationError('Candidate with this username is not exists.')
        return user_name
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = ['full_name','about','bio','profession','experience','hour_rate','projects_num','english_level','address','image','phone','cv']
        widgets = {    
            "image" : forms.ClearableFileInput(attrs={
                "class":"form-control",
            }),
            
            "experience" : forms.Select(attrs={
                "class":"form-control",
                "style":"height:30px"
                
            }),
            
            "english_level" : forms.Select(attrs={
                "class":"form-control",
                "style":"height:30px"
            }), 
           }
             
class CandidateSkills(forms.ModelForm):
    class Meta:
        model = skills
        fields = ['skill','percent']
    
class ApplyToJobForm(forms.ModelForm):
    class Meta:
        model = Candidate_Applying
        fields = ['name','email','cv','about']
        
        
class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    msg = forms.CharField(widget=forms.TextInput())