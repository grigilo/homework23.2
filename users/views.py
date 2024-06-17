import secrets

from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from config import settings
from config.settings import EMAIL_HOST_USER, DOMAIN_NAME
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm
from users.models import User
from utils import TitleMixin


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
        Создание пользователя
        Создание токена
        Отправка письма с сылкой
        """

        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f'Для подтверждения почты перейдите по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_varification(request, token):
    """
    Подтверждение почты
    :param request:
    :param token:
    :return:
    """
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserResetPasswordView(TitleMixin, TemplateView):
    title = 'Восстановление пароля'
    template_name = 'users/pwd_reset.html'
    success_url = reverse_lazy('users:login')

    def post(self, request):
        """
        Обрабатывает запрос на восстановление пароля.
        """
        if self.request.method == 'POST':
            email = self.request.POST.get('email')
            try:
                user = User.objects.get(email=email)
                token = secrets.token_hex(10)
                link = f'{DOMAIN_NAME}/users/login/'
                if User.objects.filter(email=user.email).exists():
                    subject = 'Восстановление пароля'
                    message = (
                        f'Для восстановления доступа к личному '
                        f'кабинет пройдите по ссылке: {link} '
                        f'и воспользуйтесь временным паролем:\n {token}')
                    send_mail(
                        subject=subject,
                        message=message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user.email],
                        fail_silently=False,
                    )
                    user.password = make_password(token, salt=None,
                                                  hasher="default")
                    user.save()
            except User.DoesNotExist:
                # return HttpResponse(f'Пользователь с электронной почтой
                # {email} не найден.')
                return HttpResponseRedirect(reverse('users:login'))
        return render(request, self.template_name)
