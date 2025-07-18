from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

@login_required
def dashboard(request):
    # you can add more context here, like user orders
    return render(request, 'store/dashboard.html', {'user': request.user})