from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Caretaker)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Family)
admin.site.register(Reminders)
admin.site.register(DailyRemarks)
admin.site.register(PersonalDetails)
admin.site.register(Memories)
admin.site.register(Medicines)

admin.site.register(Quiz)
