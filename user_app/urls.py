from django.urls import path,re_path
from .views import (
   HomeView,SignUpView,LogoutView
   ) #FOR REGULAR VIEWS
from . import views
from django.contrib.auth import views as auth_views


app_name='user_app'

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('signup/', SignUpView.as_view(), name="signup"),
   path('login/', auth_views.LoginView.as_view(template_name='user_app/registration/login.html'), name="login"),
   path('password/reset/form/', auth_views.PasswordResetView.as_view(template_name='user_app/registration/password_reset_form.html'), name='password_rest_form'),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user_app/registration/password_reset_done.html'), name='password_reset_done'),
   path(r'^verify/(?P<uuid>[a-z0-9\-]+)/', views.verify, name='verify'),
   path('survey/dashboard/', views.dashboard, name='login_success'),
   path('logout/success/', auth_views.LogoutView.as_view(template_name='user_app/registration/logout_success.html'), name='logout'),
   re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='user_app/registration/password_reset_confirm.html'), name='password_reset_confirm'),
   path('reset/completed/', auth_views.PasswordResetCompleteView.as_view(template_name='user_app/registration/password_reset_complete.html'), name='password_reset_complete'),
]


