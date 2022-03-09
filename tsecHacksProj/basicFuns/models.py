from django.db import models

# Create your models here.
class Patient(models.Model):
    patiendID = models.IntegerField(primary_key=True)
    patientName = models.CharField(max_length=50)
    patientAge = models.IntegerField()
    patientGender = models.CharField(max_length=10)
    # patientAddress = models.CharField(max_length=100)
    patientPhone = models.CharField(max_length=20)
    # patientEmail = models.CharField(max_length=50)
    # patientPassword = models.CharField(max_length=50)
    patientBloodGroup = models.CharField(max_length=10)
    patientMedicalHistory = models.CharField(max_length=50)
    patientEmergencyContact = models.CharField(max_length=50)
    patientEmergencyPhone = models.CharField(max_length=20)

class Doctor(models.Model):
    doctorID = models.IntegerField(primary_key=True)
    doctorName = models.CharField(max_length=50)
    doctorAge = models.IntegerField()
    doctorGender = models.CharField(max_length=10)
    doctorAddress = models.CharField(max_length=100)
    doctorPhone = models.CharField(max_length=20)
    doctorEmail = models.CharField(max_length=50)
    doctorPassword = models.CharField(max_length=50)
    doctorSpecialization = models.CharField(max_length=50)
    doctorExperience = models.IntegerField()
    doctorFees = models.IntegerField()
    doctorAvailability = models.CharField(max_length=50)

class Family(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    relation = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)

class Caretaker(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    caretakerName = models.CharField(max_length=50)
    caretakerPhone = models.CharField(max_length=20)
    caretakerAddress = models.CharField(max_length=100)

class Reminders(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    reminder = models.CharField(max_length=50)
    remindTimeStamp = models.DateTimeField()

class DailyRemarks(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    remark = models.CharField(max_length=100)
    remarkDate = models.DateField()
    remarkFeedback = models.CharField(choices=[('POSTIVE', "POSITIVE"),  ("NEGATIVE","NEGATIVE"), ("NEUTRAL", "NEUTRAL")], max_length=100)


class Memories(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    memory = models.FileField(upload_to='memories/')
    memoryDate = models.DateField()
    peopleInMemory = models.CharField(max_length=100)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    prescription = models.FileField(upload_to='prescriptions/')
    prescriptionDate = models.DateField()

class PersonalDetails(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

class Quiz(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    quizTimeStamp = models.DateTimeField()
    quizScore = models.IntegerField()
    quizScoreOutOf = models.IntegerField()

class Game(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    gameName = models.CharField(max_length=100)
    gameDate = models.DateField()
    gameScore = models.IntegerField()

class Diet(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dietDetails = models.FileField(upload_to='diet_details/')
    dietDuration = models.DurationField()
    dietFollowup = models.CharField(choices=[('YES', "YES"), ("NO", "NO")], max_length=100)

