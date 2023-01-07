from django.contrib.auth.forms import UserCreationForm

from app.models import Registration


class LoginForm(UserCreationForm):
    class Meta:
        model= Registration
        fields = ('username','password1','password2','name','email','contact_no','profile')
