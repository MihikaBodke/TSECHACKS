from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == 'POST':
        print(request.POST)
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')