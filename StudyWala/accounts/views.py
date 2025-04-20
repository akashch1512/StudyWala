from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login page after successful signup
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'registration/signup.html', {'form': form})



def custom_password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Get the email address from the form
            email = form.cleaned_data["email"]
            
            # Get the associated user object
            users = form.get_users(email)
            for user in users:
                # Generate a unique token and email
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(user.pk.encode('utf-8'))
                token_url = f"{request.scheme}://{get_current_site(request).domain}/password_reset/{uid}/{token}/"
                
                email_subject = "Password Reset"
                email_message = render_to_string('accounts/password_reset_email.html', {
                    'user': user,
                    'token_url': token_url,
                })
                
                send_mail(email_subject, email_message, 'no-reply@example.com', [email])
                
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/password_reset_form.html', {'form': form})