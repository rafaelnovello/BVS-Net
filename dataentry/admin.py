# -*- coding: utf-8 -*-	
from bvsnet.dataentry.models import *
#from bvsnet.dataentry import 
from django.contrib import admin

class ContactPhoneAdmin(admin.TabularInline):
	model = ContactPhone
	fieldsets = [
		(None, {'fields' : ['phone']}),
	]
	extra = 1

class ContactEmailAdmin(admin.TabularInline):
	model = ContactEmail
	fieldsets = [
		(None, {'fields' : ['email']}),
	]
	extra = 1

class InstanceNotesAdmin(admin.TabularInline):
	model = InstanceNotes
	fieldsets = [
		(None, {'fields' : ['note']}),
	]
	extra = 1

class InformationSourceAdmin(admin.TabularInline):
	model = InformationSource
	fieldsets = [
		(None, {'fields' : ['name','url', 'source_type', 'aplication', 'server']}),
	]
	extra = 1

class InstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'portal_type')
    fieldsets = [
		(None, {'fields' : ['name', 'portal_type', 'status', 'interface', 'contacts', 'evaluation', 'responsible']}),
		('Certificação', {'fields' : ['certification_date', 'conformation_url']}),
	]
    inlines = [InstanceNotesAdmin, InformationSourceAdmin]
    
class InstanceNotesAdmin(admin.ModelAdmin):
    list_display = ('instance', 'note')
    
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('avaliator', 'date')
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')
    fields = ('name', 'institution', 'role')
    inlines = [ContactPhoneAdmin, ContactEmailAdmin]
    
'''class ContactPhoneAdmin(admin.ModelAdmin):
    list_display = ('contact', 'phone')

class ContactEmailAdmin(admin.ModelAdmin):
    list_display = ('contact', 'email')'''


admin.site.register(Instance, InstanceAdmin)
admin.site.register(Responsible)
admin.site.register(Server)
admin.site.register(Contact, ContactAdmin)
