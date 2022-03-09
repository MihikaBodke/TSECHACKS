from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import SelectPatient
from .models import *
# improt redirect
from django.shortcuts import redirect


def index(request):
    if request.method == 'POST':

        request.session['patientID'] = request.POST.get('patientID')
        print(request.session['patientID'])
        return redirect('/patientHome/')
    form = SelectPatient()
    return render(request, 'selectPatient.html', {"form": form})


def getReminders(request):
    patientID = request.session['patientID']
    reminders = Reminders.objects.filter(
        patient=Patient.objects.filter(patientID=int(patientID))[0])

    for i in reminders:
        print(i)
    return render(request, 'reminders.html', {'reminders': reminders})


def suggestMemory(memories):
    # ADD A MEMORY SUGGESTOR ALGORITHM TODO
    return memories[0]


def patientHome(request):
    return render(request, 'patientHome.html')


def getMemory(request):
    # add an option to suggest memories also
    patientID = request.session['patientID']

    memories = Memories.objects.filter(
        patient=Patient.objects.filter(patientID=int(patientID))[0])

    memory = suggestMemory(memories)
    return render(request, 'memories.html', {'memory': memory})


def games(request):
    return render(request, 'games.html')


# def agoraCall(request):

# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = Quiz.objects.all()
        p = Paginator(questions, 1)
        page_number = request.POST.get('page')
        try:
            # returns the desired page object
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)
        if page_number == 1:
            score = 0
            wrong = 0
            correct = 0
            total = 1
        q = page_obj.object_list[0]
        print(q.question)
        print(q.ans)
        print()
        if q.ans == request.POST.get(q.question):
            score += 10
            correct += 1
        else:
            wrong += 1
        context = {'page_obj': page_obj,
                   'time': request.POST.get('timer'),
                   'score': score, 'total': total, 'correct': correct, 'wrong': wrong}
        if page_number == p.num_pages:
            percent = score/(total*10) * 100
            context = {
                'score': score,
                'time': request.POST.get('timer'),
                'correct': correct,
                'wrong': wrong,
                'percent': percent,
                'total': total
            }
        return render(request, 'Quiz/result.html', context)
    else:
        questions = Quiz.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'Quiz/home.html', context)
