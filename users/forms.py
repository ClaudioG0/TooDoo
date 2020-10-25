from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()


class LoginUserForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
                                                    'type':'email',
                                                    'class':"input",
                                                    'id':"email",
                                                    'name':"email",
                                                    'placeholder':'Email',
                                                    'maxlength': 40,
                                                    'required': True}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs ={
                                                    'type':'password',
                                                    'class':"input",
                                                    'id':"password",
                                                    'name':"password",
                                                    'placeholder':'Password',
                                                    'maxlength': 40,
                                                    'required': True})
                                            )

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("ERROR! TRY AGAIN!")

        return super(LoginUserForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={
                                                'type': 'text',
                                                'class': 'input',
                                                'id': 'name',
                                                'name': 'name',
                                                'placeholder': 'Name',
                                                'maxlength': 40,
                                                'required': True
    }))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={
                                                'type': 'email',
                                                'class': 'input',
                                                'id': 'email2',
                                                'name': 'email',
                                                'placeholder': 'Email',
                                                'maxlength': 40,
                                                'required': True
    }))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={
                                                'type': 'password',
                                                'class': 'input',
                                                'id': 'password',
                                                'name': 'password',
                                                'placeholder': 'Password',
                                                'maxlength': 40,
                                                'required': True}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={
                                                'type': 'password',
                                                'class': 'input',
                                                'id': 'confirmpassword',
                                                'name': 'confirmpassword',
                                                'placeholder': 'Confirm Password',
                                                'maxlength': 40,
                                                'required': True}))


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]


    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        email_qs = User.objects.filter(email=email)

        if email_qs.exists():
            raise forms.ValidationError("ERROR! EMAIL IS ALREADY USED")

        if password != password2:
            raise forms.ValidationError('PASSWORDS MUST MATCH')

        return super(UserRegisterForm, self).clean(*args, **kwargs)
