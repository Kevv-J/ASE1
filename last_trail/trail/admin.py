from django.contrib import admin
from .models import candidateLog,voterLog
admin.site.register(voterLog)
admin.site.register(candidateLog)

