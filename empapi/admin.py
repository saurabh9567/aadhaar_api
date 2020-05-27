from django.contrib import admin

# Register your models here.
from .models import Candidate, Match_result, Uan_response

admin.site.register(Candidate)
admin.site.register(Match_result)
admin.site.register(Uan_response)