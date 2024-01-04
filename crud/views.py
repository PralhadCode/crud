from django.shortcuts import render, redirect
from .forms import CreateForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

# Password Encryption Module

from django.contrib.auth.hashers import make_password, check_password


# print(make_password('1234'))


# HomePage

def home(request):
    return render(request, 'crud/index.html')


# Register Page

def register(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully ")
            return redirect('login')

    return render(request, 'crud/register.html', {'forms': form})


# User Login Page

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    return render(request, 'crud/login.html', {'forms': form})

# Dashboard


@login_required(login_url='login')
def dashboard(request):
    my_records = Record.objects.all()
    return render(request, 'crud/dashboard.html', {'records': my_records})

# Create a Record


@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Created Successfully ")
            return redirect("dashboard")
    return render(request, 'crud/create-record.html', {'forms': form})

# Update a record


@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully ")
            return redirect("dashboard")

    return render(request, 'crud/update-record.html', {'forms': form})

# View/ Read a record


@login_required(login_url='login')
def view_record(request, pk):
    all_records = Record.objects.get(id=pk)
    return render(request, 'crud/view-record.html', {'record': all_records})


# Delete a record

@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Record Deleted Successfully ")
    return redirect('dashboard')


# User logout

def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successfully ")
    return redirect("login")
