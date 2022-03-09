from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    return HttpResponse("Hello")

# PATIENT APP
def getReminders(request):
    user = request.user 
    reminders = Reminders.objects.filter(patient__patientID=user.patient.patientID)
    return render(request, 'basicFuns/reminders.html', {'reminders': reminders})

