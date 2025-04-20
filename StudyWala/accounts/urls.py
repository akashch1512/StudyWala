from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('signup/', views.signup, name='signup'),
    # path('password_reset/', views.custom_password_reset, name='password_reset'),
]


# Step 4: Set Up the Password Reset Template (Optional)
# Django comes with default templates for password reset. If you'd like to customize them, you can create the following template:

# Password Reset Form Template: templates/registration/password_reset_form.html

# Password Reset Done Template: templates/registration/password_reset_done.html

# Password Reset Confirm Template: templates/registration/password_reset_confirm.html

# Password Reset Complete Template: templates/registration/password_reset_complete.html

# For now, the default Django templates should work fine.