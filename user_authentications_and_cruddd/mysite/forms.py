from django import forms
from .models import User ,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


class CustomUserCreationForm(UserCreationForm):
    PLAYER_CHOICES = (
        ("Cricket", "Cricket"),
        ("Hockey", "Hockey"),
        ("Swimming", "Swimming"),
        ("Cycling", "Cycling"),
    )
    JOB_CHOICES = (
        ("CEO", "CEO"),
        ("Developer", "Developer"),
        ("Graphic_Designer", "Graphic_Designer"),

    )
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    )

    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                 attrs={'style': 'width: 1000px; margin-top:60px;', 'placeholder': 'Name',
                                        'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'style': 'width: 1000px; '
                                                                                             'margin-top:20px;',
                                                                                    'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'style': 'width: 1000px; '
                                                                                                     'margin-top:20px;',
                                                                                            'class': 'form-control'}))
    job_title = forms.ChoiceField(choices=JOB_CHOICES)
    user_Img = forms.ImageField(widget=forms.FileInput(
        attrs={'style': 'width: 250px; margin-top:30px;', 'placeholder': 'Name',
               'class': 'form-control'}))
    npi_number = forms.CharField(label='Npi_number', widget=forms.NumberInput(attrs={'style': 'width: 1000px; '
                                                                                              'margin-top:20px;',
                                                                                     'class': 'form-control'}))
    player = forms.ChoiceField(choices=PLAYER_CHOICES)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender',
                               )

    class Meta:
        model = User
        fields = ('email', 'user_Img')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.exists():
            raise ValidationError("User Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            npi_number=self.cleaned_data['npi_number'],
            job_title=self.cleaned_data['job_title'],
            player=self.cleaned_data['player'],
            gender=self.cleaned_data['gender'],
            user_Img=self.cleaned_data['user_Img'],

        )
        return user


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 500px; '
                     'margin-top:20px;',

        })
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'width: 500px;margin-top:20px;',
        })


class DashboardForm(forms.Form):
    nick_name = forms.CharField(label='nick_name', widget=forms.TextInput(attrs={'style': 'width: 1000px; '
                                                                                          'margin-top:20px;',
                                                                                 'class': 'form-control'}))
    Family_detail = forms.CharField(label='Family_detail', widget=forms.Textarea(attrs={'style': 'width: 1000px; '
                                                                                                 'height: 120px; '
                                                                                                 'margin-top:20px;',
                                                                                        'class': 'form-control'}))

    work_description = forms.CharField(label='Work_description', widget=forms.Textarea(attrs={'style': 'width: 1000px; '
                                                                                                       'margin-top:20px;',
                                                                                              'class': 'form-control'}))


class DashboardViewForm(forms.Form):
    nick_name = forms.CharField(label='nick_name', widget=forms.Textarea(attrs={'style': 'width: 1000px; '
                                                                                          'margin-top:20px;',
                                                                                 'class': 'form-control'}))
    Family_detail = forms.CharField(label='Family_detail', widget=forms.Textarea(attrs={'style': 'width: 1000px; '
                                                                                                 'height: 120px; '
                                                                                                 'margin-top:20px;',
                                                                                        'class': 'form-control'}))

    work_description = forms.CharField(label='Work_description', widget=forms.Textarea(attrs={'style': 'width: 1000px; '
                                                                                                       'margin-top:20px;',
                                                                                              'class': 'form-control'}))


class EditForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Profile

        # specify fields to be used
        fields = [
            "nick_name",
            "Family_detail",
            "work_description",
            "user_Img",
                ]


class DashboardForm(forms.ModelForm):
    # create metaclass
    class Meta:
        # specify model to be used
        model = Profile

        # specify fields to be used
        fields = [
            "nick_name",
            "Family_detail",
            "work_description",
            "user_Img",
                ]

