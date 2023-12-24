from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if User.objects.filter(email=email).exists():
            self.add_error('email', "Эта почта уже зарегистрирована!")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            self.add_error('username', "Это имя пользователя недоступно!")
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user object without saving
            user.is_active = False  # Set 'is_active' field to False
            form.save()  # Save the user object to the database
            user_name = form.cleaned_data.get('username')
            subject = 'Завершение регистрации'
            email_template_name = 'registration/template_activate_account.html'
            cont = {
                "domain": get_current_site(request).domain,
                "site_name": 'binance',
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": account_activation_token.make_token(user),
                "protocol": 'https' if request.is_secure() else 'http',
            }
            msg_html = render_to_string(email_template_name, cont)
            try:
                send_mail(subject, "ссылка", "admin@django-project123123.site"
                          , [user.email], fail_silently=True, html_message=msg_html)
            except Exception as e:
                return print(str(e))
            messages.success(request, f'Аккаунт создан {user_name}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'main/register.html', context)



def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Неверное имя пользователя или пароль!')
    context = {}
    return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def password_reset_request(request):
    if request.method == 'POST':
        print('post')
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            mail = password_reset_form.cleaned_data['email']
            try:
                user = User.objects.get(email=mail)
            except:
                user = False

            if user:
                subject = 'Запрос сброса пароля'
                email_template_name = 'registration/password_reset_email.html'
                cont = {
                    "email": user.email,
                    "domain": '127.0.0.1:8000',
                    "site_name": 'binance',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    "token": default_token_generator.make_token(user),
                    "protocol": 'http',
                }
                msg_html = render_to_string(email_template_name, cont)
                try:
                    send_mail(subject, "ссылка", "admin@django-project123123.site"
                              , [user.email], fail_silently=True, html_message=msg_html)
                except Exception as e:
                    return print(str(e))
                return redirect('password_reset_done')
            else:
                messages.error(request, 'Пользователь не найден, напишите о проблеме администратору')
                return redirect('client:password_reset')
    return render(request, template_name='registration/password_reset_form.html')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Успех")
        return redirect('login')
    return redirect('home')
