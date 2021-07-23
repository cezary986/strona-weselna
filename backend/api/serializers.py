from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist


class VersionSerializer(serializers.Serializer):
    version = serializers.CharField()


class SectionConfigSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Gdzie = serializers.BooleanField(read_only=True)
    Kiedy = serializers.BooleanField(read_only=True)
    Transport = serializers.BooleanField(read_only=True)
    Trzaskanie = serializers.BooleanField(read_only=True)
    Kontakt = serializers.BooleanField(read_only=True)


class WhereSectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Tytul = serializers.CharField(read_only=True)
    Tresc = serializers.CharField(read_only=True)
    TekstDodatkowy = serializers.CharField(read_only=True)
    TekstPrzycisku = serializers.CharField(read_only=True)
    Zdjecie = serializers.CharField(read_only=True)


class ContactSectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Tytul = serializers.CharField(read_only=True)
    Tresc = serializers.CharField(read_only=True)
    TekstPrzycisku = serializers.CharField(read_only=True)
    Zdjecie = serializers.CharField(read_only=True)


class TransportSectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Tytul = serializers.CharField(read_only=True)
    Tresc = serializers.CharField(read_only=True)


class WhenSectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Tytul = serializers.CharField(read_only=True)
    Tresc = serializers.CharField(read_only=True)
    Data_Slubu = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S.000Z", read_only=True)
    Zdjecie = serializers.CharField(read_only=True)

class TrzaskanieSectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Tytul = serializers.CharField(read_only=True)
    Tresc = serializers.CharField(read_only=True)
    Data = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S.000Z", read_only=True)
    Zdjecie = serializers.CharField(read_only=True)
