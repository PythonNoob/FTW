from django.db import models
import datetime
# Create your models here.

class Grupi(models.Model):
    oblast = models.CharField(max_length = 30)
    datum_kreiranje = models.DateField('datum na sozdavanje')
    def __unicode__(self):
        return self.oblast

class Kompanija(models.Model):
    grupi = models.ForeignKey(Grupi)
    ime = models.CharField(max_length=20)
    opis = models.TextField(max_length=200)
    datum_kreiranje = models.DateField('datum na sozdavanje')
    def __unicode__(self):
        return u'%s %s' % (self.ime, self.opis)

class Lice(models.Model):
    kompanija = models.ForeignKey(Kompanija)
    ime = models.CharField(max_length = 30)
    adresa = models.CharField(max_length = 30)
    grad = models.CharField(max_length = 20)
    telefon = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    datum_regist = models.DateField(default = datetime.date.today)
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.ime, self.adresa, self.grad, self.telefon, self.email)
    