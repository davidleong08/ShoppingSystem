import re
from django.core.exceptions import ValidationError
from django import forms
from apps.users.models import MyUser


# mobile number validator
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('the formate of mobile number has some problems')


# user register form
class UserRegForm(forms.Form):
    username = forms.CharField(label='username', min_length=6, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'please input username'}),
                               error_messages={'required': 'username cannot be empty',
                                               'min_length': 'the length of username at least is 6 digit'}),
    password = forms.CharField(label="password", min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(
                                   render_value=True,
                                   attrs={"class": "form-control"},
                               ),
                               error_messages={'max_length': 'the max length of password is 10 digit',
                                               'required': 'password cannot be empty',
                                               'min_length': 'the length of password at least is 6 digit'})
    re_password = {'max_length': 'the max length of password is 10 digit',
                   'required': 'password cannot be empty',
                   'min_length': 'the length of password at least is 6 digit'}
    user_img = forms.ImageField(label="user_avatar", required=False, widget=forms.widgets.FileInput(
        attrs={'class': 'form-control'}))
    mobile = forms.IntegerField(label='mobile_number', validators=[mobile_validate], widget=forms.widgets.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'please input your mobile number'}),
                                error_messages={'invalid': 'Please enter a valid bid'})
    email = forms.CharField(label='email', min_length=4, max_length=50, widget=forms.widgets.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'please input email address'}),
                            error_messages={
                                'min_length': 'the length of email at least is 6 digit',
                                'max_length': 'the max length of email is 64'
                            }),

    def clean_username(self):
        new_username = self.cleaned_data.get("username")
        users = MyUser.objects.all()
        for user in users:
            if user.username == new_username:
                self.add_error("username", ValidationError("the username has been existed"))

    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        print(password)
        if password != re_password:
            # raise forms.ValidationError("The two passwords are different")
            self.add_error("re_password", ValidationError("The two passwords are different"))

    def clean_email(self):
        new_email = self.cleaned_data.get("email")
        users = MyUser.objects.all()
        for user in users:
            if user.email == new_email:
                self.add_error("email", ValidationError("the email address has been existed"))
