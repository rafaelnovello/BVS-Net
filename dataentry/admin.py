from bvsnet.dataentry.models import *
#from bvsnet.dataentry import 
from django.contrib import admin

class InstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'portal_type')
    
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('instance', 'avaliator', 'date')
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')
    


admin.site.register(Instance, InstanceAdmin)
admin.site.register(Responsible)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(InformationSource)
admin.site.register(Server)
admin.site.register(Contact, ContactAdmin)
