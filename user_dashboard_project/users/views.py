from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm, LoginForm
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            # Create User object but don't save to database yet
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set the password
            user.save()  # Now save the User object

            # Create UserProfile object
            profile = profile_form.save(commit=False)
            profile.username = user  # Assign the User object to UserProfile.username
            profile.save()

            messages.success(request, 'Account created successfully')
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
    
    return render(request, 'signup.html', {'form': form, 'profile_form': profile_form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    user_profile = UserProfile.objects.get(username=user)
                    # Redirect to appropriate dashboard based on user type
                    if user_profile.user_type == 'doctor':
                        return redirect('doctor_dashboard')
                    elif user_profile.user_type == 'patient':
                        return redirect('patient_dashboard')
                    else:
                        # Handle other user types or errors
                        pass
                except UserProfile.DoesNotExist:
                    # Handle case where UserProfile does not exist
                    pass
            else:
                # Set error message for invalid username or password
                messages.error(request, 'Invalid username or password')
        else:
            # Form is invalid
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

@login_required
def profile_create_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile created successfully')
            return redirect('profile_create')
    else:
        form = UserProfileForm()
    return render(request, 'profile_create.html', {'form': form})
