from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseServerError
from api import VERSION
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from api.serializers import \
    VersionSerializer, \
    SectionConfigSerializer, \
    WhenSectionSerializer, \
    WhereSectionSerializer, \
    ContactSectionSerializer, \
    TransportSectionSerializer, \
    TrzaskanieSectionSerializer
from api.models import \
    SectionConfig, \
    WhenSection, \
    WhereSection, \
    TransportSection, \
    TrzaskanieSection, \
    ContactSection, \
    ArrivalConfirmation


import json


def save_data(request):
    if request.method == 'POST':
        # request.raw_post_data w/ Django < 1.4
        json_data = json.loads(request.body)
        try:
            who = json_data['Kto']
            will_arrive = json_data['Przyjedzie']
            confirmation = ArrivalConfirmation.objects.create(
                Kto=who,
                Przyjedzie=will_arrive
            )
            confirmation.save()
        except KeyError:
            HttpResponseServerError("Malformed data!")
        HttpResponse("Got json data")


class VersionView(APIView):

    @swagger_auto_schema(
        operation_id='version',
        operation_description='Return current API version',
        responses={200: VersionSerializer}
    )
    def get(self, request):
        serializer = VersionSerializer({'version': VERSION})
        return JsonResponse(serializer.data)

# Konfiguracja sekcji


class SectionConfigView(APIView):

    @swagger_auto_schema(
        operation_id='Konfiguracja Sekcji',
        responses={200: SectionConfigSerializer}
    )
    def get(self, request):
        when_section = SectionConfig.objects.all()[0]
        serializer = SectionConfigSerializer(when_section)
        return JsonResponse(serializer.data)

# Sekcja Kiedy


class WhenSectionView(APIView):

    @swagger_auto_schema(
        operation_id='Sekcja Kiedy',
        responses={200: WhenSectionSerializer}
    )
    def get(self, request):
        when_section = WhenSection.objects.all()[0]
        serializer = WhenSectionSerializer(when_section)
        return JsonResponse(serializer.data)


# Sekcja Gdzie
class WhereSectionView(APIView):

    @swagger_auto_schema(
        operation_id='Sekcja Gdzie',
        responses={200: WhereSectionSerializer}
    )
    def get(self, request):
        when_section = WhereSection.objects.all()[0]
        serializer = WhereSectionSerializer(when_section)
        return JsonResponse(serializer.data)


# Sekcja Transport
class TransportSectionView(APIView):

    @swagger_auto_schema(
        operation_id='Sekcja Gdzie',
        responses={200: TransportSectionSerializer}
    )
    def get(self, request):
        when_section = TransportSection.objects.all()[0]
        serializer = TransportSectionSerializer(when_section)
        return JsonResponse(serializer.data)


# Sekcja Trzaskanie
class TrzaskanieSectionView(APIView):

    @swagger_auto_schema(
        operation_id='Sekcja Gdzie',
        responses={200: TrzaskanieSectionSerializer}
    )
    def get(self, request):
        when_section = TrzaskanieSection.objects.all()[0]
        serializer = TrzaskanieSectionSerializer(when_section)
        return JsonResponse(serializer.data)


# Sekcja Kontakt
class ContactSectionView(APIView):

    @swagger_auto_schema(
        operation_id='Sekcja Kontakt',
        responses={200: ContactSectionSerializer}
    )
    def get(self, request):
        when_section = ContactSection.objects.all()[0]
        serializer = ContactSectionSerializer(when_section)
        return JsonResponse(serializer.data)


def when_section(request):
    return JsonResponse({
        "id": 1,
        "Tytul": "Gdzie",
        "Tresc": "Nasz ślub odbędzie się w kościele Parafii Matki Bożej Królowej Pokoju w Tarnowskich Górach",
        "TekstDodatkowy": "Po ceremonii zapraszamy na\nuroczystość weselną, która odbędzie\nsię na sali Skarabeusz",
        "TekstPrzycisku": "Zobacz na mapie",
        "Zdjecie": "https://drive.google.com/u/0/uc?id=1IffrGr_3HJ9GO6vSwY1lrPZeKRdDMn7Q"
    })


def contact_section(request):
    return JsonResponse({
        "id": 1,
        "Tytul": "Kontakt",
        "Tresc": "#### Adres e-mail\n\ncezary.maszczyk@gmail.com\n\n#### Numer telefonu\n\n(48) 609 715 773 - Klaudia\n\n(48) 668 361 983 - Cezary",
        "TekstPrzycisku": "Potwierdź przybycie",
        "Zdjecie": "https://drive.google.com/u/0/uc?id=1IF0GiyWHbtT6az1s4Fz6uEfjstr-bnLM"
    })
