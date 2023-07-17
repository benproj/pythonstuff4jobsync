from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('application')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


COMPANIES = [
'Microsoft',
'Google',
'Amazon',
'Apple',
'Facebook',
'IBM',
'Oracle',
'Intel',
'Cisco Systems',
'SAP',
'Adobe Systems',
'Salesforce',
'VMware',
'Tencent',
'Baidu',
'Netflix',
'Twitter',
'Uber',
'Airbnb',
'Tesla'
]
def application(request):
    if request.method == 'POST':
        selected_companies = request.POST.getlist('companies')
        # Logic to save the selected companies to the user's applications
        # You can store this information in the database or the user's session
        # and associate it with the user's account
    else:
        selected_companies = []

    context = {
        'companies': COMPANIES,
        'selected_companies': selected_companies,
    }
    return render(request, 'application.html', context)