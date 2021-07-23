from django.db import models
from datetime import datetime

from django.db.models.fields import BooleanField, CharField


class ArrivalConfirmation(models.Model):
    Kto = CharField(null=False, max_length=500)
    Przyjedzie = BooleanField(null=False)

class SectionConfig(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    Gdzie = models.BooleanField(null=False, default=True)
    Kiedy = models.BooleanField(null=False, default=True)
    Transport = models.BooleanField(null=False, default=False)
    Kontakt = models.BooleanField(null=False, default=False)
    Trzaskanie = models.BooleanField(null=False, default=False)


class WhereSection(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    Tytul = models.CharField(null=False, default=True, max_length=200)
    Tresc = models.TextField(null=False)
    TekstDodatkowy = models.TextField(null=False)
    TekstPrzycisku = models.CharField(null=False, default=True, max_length=200)
    Zdjecie = models.CharField(null=False, default=True, max_length=800)


class ContactSection(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    Tytul = models.CharField(null=False, default=True, max_length=200)
    Tresc = models.TextField(null=False)
    TekstPrzycisku = models.CharField(null=False, default=True, max_length=200)
    Zdjecie = models.CharField(null=False, default=True, max_length=800)


class TransportSection(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    Tytul = models.CharField(null=False, default=True, max_length=200)
    Tresc = models.TextField(null=False)


class WhenSection(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    Tytul = models.CharField(null=False, default=True, max_length=200)
    Tresc = models.TextField(null=False)
    Data_Slubu = models.DateTimeField(null=False, default=datetime(
        year=2021, month=8, day=28, hour=11, minute=30, second=0))
    Zdjecie = models.CharField(null=False, default=True, max_length=800)

class TrzaskanieSection(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    Tytul = models.CharField(null=False, default=True, max_length=200)
    Tresc = models.TextField(null=False)
    Data = models.DateTimeField(null=False, default=datetime(
        year=2021, month=8, day=14, hour=17, minute=00, second=0))
    Zdjecie = models.CharField(null=False, default=True, max_length=800)
