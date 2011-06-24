from bvsnet.dataentry.models import *
#from bvsnet.dataentry import 
from django.contrib import admin

class InstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'portal_type')
    
class InstanceNotesAdmin(admin.ModelAdmin):
    list_display = ('instance', 'note')
    
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('instance', 'avaliator', 'date')
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')
    
class ContactPhoneAdmin(admin.ModelAdmin):
    list_display = ('contact', 'phone')

class ContactEmailAdmin(admin.ModelAdmin):
    list_display = ('contact', 'email')


admin.site.register(Instance, InstanceAdmin)
admin.site.register(InstanceNotes, InstanceNotesAdmin)
admin.site.register(Responsible)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(InformationSource)
admin.site.register(Server)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactPhone, ContactPhoneAdmin)
admin.site.register(ContactEmail, ContactEmailAdmin)
