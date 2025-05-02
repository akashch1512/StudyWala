from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .views import signup_page, login_page, home, logout_view, activate_account_page

app_name = 'accounts'

urlpatterns = [
    # Auth routes
    path('accounts/signup/', signup_page, name='signup'),
    path('accounts/activate/<slug:uidb64>/<slug:token>/', activate_account_page, name='activate'),
    path('accounts/login/', login_page, name='login'),
    path('accounts/logout/', logout_view, name='logout'),

    # Password Reset routes
    path('accounts/reset-password/', auth_views.PasswordResetView.as_view(
    template_name='accounts/password_reset_form.html',
    email_template_name='accounts/password_reset_email.html',
    subject_template_name='accounts/password_reset_subject.txt',
    success_url=reverse_lazy('accounts:password_reset_done')
), name='reset_password'),


    path('accounts/reset-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),

    path('accounts/reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Home route
    path('', home, name='home'),
]
