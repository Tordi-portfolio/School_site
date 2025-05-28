from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegistrationForm
from .models import Result, StudentUser
from datetime import datetime
from .forms import ProfileUpdateForm

# Create your views here.

# Profile picture view
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})
# End of profile picture view


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html', {'year': datetime.now().year})

def profile(request):
    return render(request, 'profile.html')


@login_required
def dashboard(request):
    student = request.user
    result = Result.objects.filter(student=student).first()
    all_results = Result.objects.filter(student__classroom=student.classroom)
    ranked = sorted(all_results, key=lambda r: r.total_score(), reverse=True)
    position = ranked.index(result) + 1 if result in ranked else None
    return render(request, 'dashboard.html', {'student': student, 'result': result, 'position': position})

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user: login(request, user); return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')