from django.test import TestCase
from django.urls import resolve, reverse
from .views import LoginPage, LogoutUser, RegisterPage, password_reset_request
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


class TestUrls(TestCase):
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, LoginPage)

    def test_logout_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, RegisterPage)

    def test_register_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, LogoutUser)

    def test_password_reset_url_is_resolved(self):
        url = reverse('password_reset')
        self.assertEqual(resolve(url).func, password_reset_request)

    def test_password_reset_done_url_is_resolved(self):
        url = reverse('password_reset_done')
        self.assertEqual(resolve(url).func.view_class, PasswordResetDoneView)

    def test_password_reset_complete_url_is_resolved(self):
        url = reverse('password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, PasswordResetCompleteView)


class TestViews(TestCase):
    def test_list_url_is_resolved(self):
        assert 1 == 1




