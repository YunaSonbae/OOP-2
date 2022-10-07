
from django.shortcuts import render

from .forms import RegisterUserForm



def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})

    else:
        user_form = RegisterUserForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def profile(request):
    return render(
        request,
        'registration/profile.html'
    )