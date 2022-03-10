"""tsecHacksProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from basicFuns import views
# import include
from caretaker import views as caretakerViews
from organization import views as orgnViews
# from agora.views import Agora
urlpatterns = [
    path('', views.index),

    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    path('games/', views.games, name="games"),
    path('reminders/', views.getReminders, name="reminders"),
    path('memory/', views.getMemory, name="memory"),
    path('createReminder/', caretakerViews.createReminder),
    path('patientHome/', views.patientHome, name="patientHome"),
    path('enterQuestions/', caretakerViews.enterQuestions),
    path('careTakerAddMedicine/', caretakerViews.careTakerAddMedicine),
    path('careTakerHome/', caretakerViews.careTakerHome),
    path('about/', caretakerViews.about, name="about"),
    path('careTakerReminders/', caretakerViews.careTakerReminder, name="careTakerReminder"),
    path('patientAnalysis', orgnViews.patientAnalysis),
    path('orgnHome', orgnViews.orgnHome),
    path('orgnLogin', orgnViews.orgnLogin, name="orgnlogin"),
    path('familyMemberLogin', caretakerViews.famLogin, name="familyMemberLogin"),
    path('quiz', views.quiz, name="quiz"),
    path('remarks/', views.getDailyRemarks, name="getRemarks"),

    path('numbergame/', views.numbergame, name="numbergame"),
    path('matchcards/', views.matchcards, name="matchcards"),
    path('diet/', caretakerViews.diet, name="diet"),


    # add agora calling link
    # path('agora-call/', Agora.as_view(
    # app_id="12f76ca2476C4a04aa0b307326fcb56e",
    # channel="00649bbac818ef54826993f78170626a3ecIADDmmMxHKvXHu4i3XGq2/J3pvTGQTi4jT2ipPGR5lw5IMtFOxEAAAAAEABOH1vQ+QoqYgEAAQD5Cipi",
    # channel="tsechacks"
    # )),
    # path('pusher/auth/', views.pusher_auth, name='agora-pusher-auth'),
    # path('token/', views.generate_agora_token, name='agora-token'),
    # path('call-user/', views.call_user, name='agora-call-user'),



]
