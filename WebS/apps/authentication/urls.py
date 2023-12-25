from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.LoginPage, name="login"),
    path('register/', views.RegisterPage, name="register"),
    path('logout/', views.LogoutUser, name="logout"),

    path('password_reset/', views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
]
