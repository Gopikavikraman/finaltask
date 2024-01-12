from django.contrib.auth.forms import User, AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields = ['username','password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2']