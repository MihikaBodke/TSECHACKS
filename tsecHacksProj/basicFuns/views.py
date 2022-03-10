from fer import FER
import matplotlib.pyplot as plt 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import SelectPatient
from .models import *
import cv2
# improt redirect
from django.shortcuts import redirect

def index(request):
    if request.method == 'POST':

        request.session['patientID'] = request.POST.get('patientID')
        print(request.session['patientID'])
        return redirect('/patientHome/')
    form = SelectPatient()
    return render(request, 'selectPatient.html', {"form": form})

def login(request):
    print("METHOD CALLED") 
    if request.method == 'POST':
        print("IT IS POSR")
        email = request.POST.get("email")
        password = request.POST.get("password")
        return redirect('/careTakerAddMedicine/')
        return render(request, 'careTakerAddMedicine.html')
    else:

        return render(request, 'login.html')


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
    import requests
    url = 'https://api.jokes.one/jod?category=jod'
    headers = {'content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    print(response)
    print(response.text)
    joke = str(response.json()['contents']['jokes'][0]['joke']['text'])
    print(joke)
    joke = joke.replace('\r\n', '    ')
    return render(request, 'patientHome.html', {'joke': joke})

# def getEmotion(img, detector):
#     emotion, score = detector.top_emotion(img)
#     obj = DailyRemarks.objects.create( remark = [emotion, score], patient = Patient.objects.get(patientID = 1))
#     print(emotion, score)

def getMemory(request):
    # add an option to suggest memories also
    patientID = request.session['patientID']

    memories = Memories.objects.filter(
        patient=Patient.objects.filter(patientID=int(patientID))[0])

    # memory = suggestMemory(memories)
    # face mood detection here
    # videoCaptureObject = cv2.VideoCapture(0)
    # result = True
    # while(result):
    #     ret,frame = videoCaptureObject.read()
    #     cv2.imwrite("img.jpg",frame)
    #     result = False
    # videoCaptureObject.release()
    # cv2.destroyAllWindows()

    # detector = FER(mtcnn=True)

    # img = plt.imread("img.jpg")
    # getEmotion(img, detector)
    # # emotion, score = detector.top_emotion(img)
    # print(emotion,score)
    # print("HELLOOOOOOOO ")


    return render(request, 'memories.html')


def games(request):
    return render(request, 'games.html')


# def agoraCall(request):

def quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions = PersonalDetails.objects.filter(patient=Patient.objects.filter(patientID=int(request.session['patientID']))[0])
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quizresult.html',context)
    else:
        questions = PersonalDetails.objects.filter(patient=Patient.objects.filter(patientID=int(request.session['patientID']))[0])
        context = {
            'questions':questions
        }
        return render(request,'quiz.html',context)
import datetime
def getDailyRemarks(request):
    if request.method == "POST":
        print("POSTTT")
        remark = request.POST.get('remarks')
        patientID = request.session['patientID']
        remarkDate = datetime.datetime.now().date()
        positive = [
        "remember", "good", "followed", "passed", "happy", "recognised",
        "recognize", "understanding", "great", "grow", "positive", "enthusiastic",
        "energetic", "joy", "playful", "fun", "recovering", "healthy", "healing",
        "relaxed", "restored", "cheerful", "friendly"
        ]

        negative = [
            "bad", "unhappy", "depressed", "sad", "angry", "fear", "anxious", "tense",
            "unhealthy", "anxiety", "swings", "loss", "dull", "uncomfortable",
            "restless", "unstable", "poor", "bad", "panic", "forget", "failed",
            "unsuccessful", "negative", "sick", "ill", "unwell", "dizzy",
            "deteoriating", "confused", "irritated", "stressed", "nervous", "paranoid",
            "scared", "terrified", "jumbled", "disorder"
        ]

        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize

        # example_sent = """This is a sample sentence,
        #   showing off the stop words filtration."""

        example_sent = "The patient did not recognize his girlfriend"
        stop_words = set(stopwords.words('english'))

        word_tokens = word_tokenize(example_sent)
        filtered_sentence = word_tokens  #[w for w in word_tokens if not w.lower() in stop_words]

        print(word_tokens)
        print(filtered_sentence)

        notList = ['not', 'no', 'did not', "didn't"]

        notCount = 0
        posCount = 0
        notBool = False
        for i in filtered_sentence:
            if i in notList:
                notBool = True
            elif i in positive:
                if notBool:
                    posCount -= 1
                    notBool = False
                else:
                    posCount += 1
            elif i in negative:
                if notBool:
                    posCount += 1
                    notBool = False
                else:
                    posCount -= 1

        if (posCount >= 0):
            remarkFeedback = "POSITIVE"
        else:
            remarkFeedback = "NEGATIVE"

        obj = DailyRemarks.objects.create(
        patient=Patient.objects.filter(patientID=int(patientID))[0],
        remarkDate=remarkDate,
        remark=remark,
        remarkFeedback=remarkFeedback
        
        )
        obj.save()
        return HttpResponse("Response saved!    ")
    else:

        return render(request, 'getDailyRemarks.html')  


def numbergame(request):
    return render(request, 'numbergame.html')

def matchcards(request):
    return render(request, 'matchcards.html')