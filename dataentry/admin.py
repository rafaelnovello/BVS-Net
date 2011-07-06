# -*- coding: utf-8 -*-	
from bvsnet.dataentry.models import *
from django.contrib import admin
from django import forms

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
    
class EvaluationAdmin(admin.TabularInline):
    model = Evaluation
    fieldsets = [
        (None, {'fields' : ['avaliator', 'date', 'is_instance_available', 
                'is_minutes_available', 'is_committe_active', 'note']}),
    ]
    extra = 1

class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
    
    def clean_certification_date(self):
        date = self.cleaned_data['certification_date']
        status = self.cleaned_data['status']
        
        if status == 'C' and date is None:
            raise forms.ValidationError(u'Você esqueceu a data de certificação')
        
        return date    
        
        
class InstanceAdmin(admin.ModelAdmin):
    form = InstanceForm
    list_display = ('name', 'status', 'portal_type')
    fieldsets = [
		(None, {'fields' : ['name', 'portal_type', 'status', 'interface', 'contacts', 'responsible']}),
		('Certificação', {'fields' : ['certification_date', 'conformation_url']}),
	]
    inlines = [InstanceNotesAdmin, InformationSourceAdmin, EvaluationAdmin]
    
class InstanceNotesAdmin(admin.ModelAdmin):
    list_display = ('instance', 'note')
    
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')
    fields = ('name', 'institution', 'role')
    inlines = [ContactPhoneAdmin, ContactEmailAdmin]
    

admin.site.register(Instance, InstanceAdmin)
admin.site.register(Responsible)
admin.site.register(Server)
admin.site.register(Contact, ContactAdmin)
