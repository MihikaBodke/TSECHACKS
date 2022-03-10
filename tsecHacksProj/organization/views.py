from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == 'POST':
        print(request.POST)
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def patientAnalysis(request):
    return render(request, 'graphOfUserProgress.html')

def orgnHome(request):
    return render(request, 'orgnHome.html')

# import redirect
from django.shortcuts import redirect
def orgnLogin(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('patientAnalysis')
        return render(request, '.html')
    return render(request, 'orgnLogin.html')

def orgnPatientAnalysis(request):
    return render(request, 'orgnPatientAnalysis.html')