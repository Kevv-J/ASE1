from django.contrib import admin
from .models import voterLog,candidateLog
# Register your models here.
admin.site.register(voterLog)
admin.site.register(candidateLog)
