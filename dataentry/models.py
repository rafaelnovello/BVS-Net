# -*- coding: utf-8 -*-

from django.db import models

class Contact(models.Model):
    class Meta:
        verbose_name = u'Contato da BVS'
        verbose_name_plural = u'Contatos das BVSs'
    
    name = models.CharField(u'Nome', max_length=50)
    institution = models.CharField(u'Instituição', max_length=100)
    role = models.CharField(u'Cargo', max_length=50, blank=True)
    
    def __unicode__(self):
        return self.name
        
class ContactPhone(models.Model):
    class Meta:
        verbose_name = u'Telefone do Contato da BVS'
    
    contact = models.ForeignKey(Contact, verbose_name=u'Contato da BVS')
    phone = models.CharField(u'Telefone', max_length=14)

    def __unicode__(self):
        return self.contact.name
    
class ContactEmail(models.Model):
    class Meta:
        verbose_name = u'Email do Contato da BVS'
    
    contact = models.ForeignKey(Contact, verbose_name=u'Contato da BVS')
    email = models.EmailField()

    def __unicode__(self):
        return self.contact.name

class Responsible(models.Model):
    class Meta:
        verbose_name = u'Responsável'
        verbose_name_plural = u'Responsáveis'
    
    name = models.CharField(u'Nome', max_length=50)
    initial_date = models.DateField(u'Data de inicio do Acompanhamento')
    final_date = models.DateField(u'Data de fim do Acompanhamento', blank=True)
    
    def __unicode__(self):
        return self.name  

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
    
    class Meta:
        verbose_name = u'Instancia BVS'
        verbose_name_plural = u'Instancias BVS'
    
    name = models.CharField(u'Nome', max_length=200)
    status = models.CharField(u'Status', max_length=1, choices=STATUS_TYPES)
    interface = models.CharField(u'Gerenciador de Interface', 
        max_length=50) #Need to be a multi value attribute
    portal_type = models.CharField(u'Tipo do Portal', max_length=1,
        choices=PORTAL_TYPES)
    certification_date = models.DateField(u'Data de Certificação', 
        blank=True, null=True)
    conformation_url = models.URLField(u'Endereço da Corformação do Comitê', 
        blank=True)
    contacts = models.ManyToManyField(Contact, verbose_name=u'Contato', 
        blank=True)
    responsible = models.ManyToManyField(Responsible, verbose_name=u'Responsáveis')
    
    def __unicode__(self):
        return self.name
            

class InstanceNotes(models.Model):
    class Meta:
        verbose_name = u'Nota da Instancia BVS'
        verbose_name_plural = u'Notas da Instancia BVS'
        
    instance = models.ForeignKey(Instance, verbose_name=u'Instancia')
    note = models.TextField(u'Notas', max_length=300)

class Evaluation(models.Model):
    class Meta:
        verbose_name = u'Avaliação'
        verbose_name_plural = u'Avaliações'
    
    avaliator = models.CharField(u'Avaliador', max_length=50)
    instace = models.ForeignKey(Instance, verbose_name=u'Instancia')
    date = models.DateField(u'Data da avaliação')
    is_instance_available = models.BooleanField(
        u'Instancia ativa')
    is_minutes_available = models.BooleanField(
        u'Instancia com atas publicadas')
    is_committe_active = models.BooleanField(
        u'Instancia com comitê ativo')
    note = models.TextField(u'Nota', max_length=300)
    
    def __unicode__(self):
        return self.instace.name
        
        
class Server(models.Model):
    class Meta:
        verbose_name = u'Servidor'
        verbose_name_plural = u'Servidores'
        
    name = models.CharField(u'Nome', max_length=50)
    
    def __unicode__(self):
        return self.name

class InformationSource(models.Model):
    class Meta:
        verbose_name = u'Fonte de Informação'
        verbose_name_plural = u'Fontes de Informação'
    
    instance = models.ForeignKey(Instance, verbose_name=u'Instancia')
    name = models.CharField(u'Nome', max_length=50)
    url = models.CharField(u'URL', max_length=150)
    source_type = models.CharField(u'Tipo da Fonte de Informação', max_length=150)
    aplication = models.CharField(u'Aplicação usada', max_length=50)
    server = models.ManyToManyField(Server, 
       verbose_name=u'Servidor')
    
    def __unicode__(self):
        return self.name
