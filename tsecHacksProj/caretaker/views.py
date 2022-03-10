from django.shortcuts import render
from .forms import CreateReminderForm, EnterQuestionsForm
# Create your views here.
from basicFuns.models import *
from django.shortcuts import redirect


def createReminder(request):
    if request.method == "POST":
        print(request.session['patientID'])
        form = CreateReminderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.patient = Patient.objects.get(
                patientID=int(request.session['patientID']))
            obj.save()
            return redirect('/reminders')
        else:
            return render(request, 'createReminder.html', {'form': form})
    else:
        form = CreateReminderForm()
        return render(request, 'createReminder.html', {'form': form})


def careTakerAddMedicine(request):
    if request.method == "POST":
        medicineName = request.POST['Medicine']
        dose = request.POST['Dose']
        patient = Patient.objects.get(
            patientID=int(request.session['patientID']))
        obj = Medicines.objects.create(
            patient=patient, medicineName=medicineName, medicineDosage=dose)
        obj.save()
        return render(request, 'careTakerAddMedicines.html', {"medicines": Medicines.objects.all().filter(patient=patient)})

    else:

        patient = Patient.objects.get(
            patientID=int(request.session['patientID']))

        return render(request, 'careTakerAddMedicines.html', {"medicines": Medicines.objects.all().filter(patient=patient)})


def careTakerHome(request):
    return render(request, 'caretakerHome.html')

# def getMedicines(request):

    # def createReminder(request):
    #     if request.method == "POST":
    #         print(request.session['patientID'])
    #         form = CreateReminderForm(request.POST)
    #         if form.is_valid():
    #             obj = form.save(commit=False)
    #             obj.patient = Patient.objects.get(
    #                 patientID=int(request.session['patientID']))
    #             obj.save()
    #             return redirect('/reminders')
    #         else:
    #             return render(request, 'createReminder.html', {'form': form})
    #     else:
    #         form = CreateReminderForm()
    #         return render(request, 'createReminder.html', {'form': form})


def enterQuestions(request):
    if request.method == "POST":
        print(request.session['patientID'])
        form = EnterQuestionsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.patient = Patient.objects.get(
                patientID=int(request.session['patientID']))
            obj.save()
            return redirect('/EnterQuestions')
        else:
            return render(request, 'EnterQuestions.html', {'form': form})
    else:
        form = EnterQuestionsForm()
        return render(request, 'EnterQuestions.html', {'form': form})



def about(request):
    return render(request, 'about.html')    
def famLogin(request):
    print("METHOD CALLED") 
    if request.method == 'POST':
        print("IT IS POSR")
        email = request.POST.get("email")
        password = request.POST.get("password")
        return redirect('/patientAnalysis')
        return render(request, 'careTakerAddMedicine.html')
    else:

        return render(request, 'famLogin.html')


def careTakerReminder(request):
    if request.method == "POST":
        reminder = request.POST['reminder']
        print(reminder)
        timestamp = request.POST['timestamp']
        patient = Patient.objects.get(
            patientID=int(request.session['patientID']))
        obj = Reminders.objects.create(
            patient=patient, reminder=reminder, remindTimeStamp = timestamp)
        obj.save()
        return render(request, 'careTakerAddReminders.html', {"reminders": Reminders.objects.all().filter(patient=patient)})

    else:

        patient = Patient.objects.get(
            patientID=int(request.session['patientID']))

        return render(request, 'careTakerAddReminders.html', {"reminders": Reminders.objects.all().filter(patient=patient)})

def diet(request):
    return render(request, 'diet.html')