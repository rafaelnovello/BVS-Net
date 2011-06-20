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
    
    name = models.CharField(u'Nome', max_length=200)
    status = models.CharField(u'Status', max_length=1, choices=STATUS_TYPES)
    interface = models.CharField(u'Gerenciador de Interface', 
        max_length=50) #Need to be a multi value attribute
    portal_type = models.CharField(u'Tipo do Portal', max_length=1,
        choices=PORTAL_TYPES)
    certification_date = models.DateField(u'Data de Certificação')
    notes = models.CharField(u'Notas', 
        max_length=300) #Need to be a multi value attribute
    conformation_url = models.CharField(u'Endereço da Corformação do Comitê', 
        max_length=50)
    
    def __unicode__(self):
        return self.name
    
class Responsible(models.Model):
    instances = models.ManyToManyField(Instance, verbose_name="Instancias")
    name = models.CharField(u'Nome', max_length=50)
    initial_date = models.DateField(u'Data de inicio do Acompanhamento')
    final_date = models.DateField(u'Data de fim do Acompanhamento')
    
    def __unicode__(self):
        return self.name
    
class Evaluation(models.Model):
    instance = models.ForeignKey(Instance, verbose_name=u'Instancia')
    avaliator = models.CharField(u'Avaliador', max_length=50)
    note = models.CharField(u'Nota', max_length=300)
    date = models.DateField(u'Data da avaliação')
    is_instance_available = models.BooleanField(
        u'Instancia ativa')
    is_minutes_available = models.BooleanField(
        u'Instancia com atas publicadas')
    is_committe_active = models.BooleanField(
        u'Instancia com comitê ativo')
    
    
class Contact(models.Model):
    instances = models.ManyToManyField(Instance, verbose_name=u'Instancias')
    name = models.CharField(u'Nome', max_length=50)
    institution = models.CharField(u'Instituição', max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(u'Telefone', max_length=14) #Need to be a multi value attribute
    role = models.CharField(u'Cargo', max_length=50)
    
    def __unicode__(self):
        return self.name
    
class InformationSource(models.Model):
    instance = models.ForeignKey(Instance, verbose_name=u'Instancia')
    name = models.CharField(u'Nome', max_length=50)
    url = models.CharField(u'URL', max_length=150)
    source_type = models.CharField(u'Tipo da Fonte de Informação', max_length=150)
    aplication = models.CharField(u'Aplicação usada', max_length=50)
    
    def __unicode__(self):
        return self.name
    
class Server(models.Model):
    information_source = models.ManyToManyField(InformationSource, 
        verbose_name=u'Instancias')
    name = models.CharField(u'Nome', max_length=50)
    
    def __unicode__(self):
        return self.name
    
