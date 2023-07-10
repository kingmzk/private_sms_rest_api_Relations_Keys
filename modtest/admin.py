from django.contrib import admin
from .models import Accelerator, OptyTracker, OptyAcc, Competation, OppCompetation, Microservice, OppMicroservice

@admin.register(Accelerator)
class AccleratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'acc_name']

@admin.register(OptyTracker)
class OptyTrackerAdmin(admin.ModelAdmin):
    list_display = ['id', 'op_id', 'op_name', 'client_name']
    
@admin.register(OptyAcc)
class OptyAccAdmin(admin.ModelAdmin):
    list_display = ['id', 'opty_id', 'acc_id']
    
@admin.register(Competation)
class CompetationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
@admin.register(Microservice)
class MicroserviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(OppCompetation)
class OppCompetationAdmin(admin.ModelAdmin):
    list_display = ['id', 'opty_id', 'comp_id'] 
    
@admin.register(OppMicroservice)
class OppMicroserviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'opty_id', 'micro_id']
