# coding: utf-8

from django.db import models

class Instance(models.Model):
    STATUS_TYPES = (
        (u'P', u'Piloto'),
        (u'C', u'Certificado'),
        (u'D', u'Em Desenvolvimento'),
        (u'T', u'Temporário'),
        (u'F', u'Desativado'),
    )
    PORTAL_TYPES = (
        (u'T', u'Temático'),
        (u'N', u'Nacional'),
        (u'I', u'Institucional'),
    )
    
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS_TYPES)
    interface = models.CharField(max_length=50) #Need to be a multi value attribute
    portal_type = models.CharField(max_length=1,choices=PORTAL_TYPES)
    certification_date = models.DateField()
    notes = models.CharField(max_length=300) #Need to be a multi value attribute
    conformation_url = models.CharField(max_length=50)
    
    
class Responsible(models.Model):
    instances = models.ManyToManyField(Instance)
    name = models.CharField(max_length=50)
    initial_date = models.DateField()
    final_date = models.DateField()
    
class Evaluation(models.Model):
    instance = models.ForeignKey(Instance)
    avaliator = models.CharField(max_length=50)
    note = models.CharField(max_length=300)
    date = models.DateField()
    is_instance_available = models.BooleanField()
    is_minutes_available = models.BooleanField()
    is_committe_active = models.BooleanField()
    
class Contact(models.Model):
    instances = models.ManyToManyField(Instance)
    name = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=14) #Need to be a multi value attribute
    role = models.CharField(max_length=50)
    
class InformationSource(models.Model):
    instance = models.ForeignKey(Instance)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    source_type = models.CharField(max_length=150)
    aplication = models.CharField(max_length=50)
    
class Server(models.Model):
    information_source = models.ManyToManyField(InformationSource)
    name = models.CharField(max_length=50)
    
    
    
    
    
