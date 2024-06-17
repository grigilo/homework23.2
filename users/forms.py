from django.contrib.auth.forms import UserCreationForm

from blogs.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserRestorePassForm(StyleFormMixin, UserCreationForm):
    """
    Форма для восстановления пароля.
    """

    class Meta:
        model = User
        fields = ('email', 'password',)
