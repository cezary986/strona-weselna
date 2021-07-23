  
from django.urls import path
from api.views import VersionView

from api.views import \
    SectionConfigView, \
    WhenSectionView, \
    WhereSectionView, \
    TransportSectionView, \
    TrzaskanieSectionView, \
    ContactSectionView


urlpatterns = [
    path('version/', VersionView.as_view(), name='version'),

    path('konfiguracja-sekcji/', SectionConfigView.as_view(), name='section_config'),
    path('sekcja-kiedy/', WhenSectionView.as_view(), name='when'),
    path('sekcja-gdzie/', WhereSectionView.as_view(), name='where'),
    path('sekcja-transport/', TransportSectionView.as_view(), name='transport'),
    path('sekcja-trzaskanie/', TrzaskanieSectionView.as_view(), name='trzaskanie'),
    path('sekcja-kontakt/', ContactSectionView.as_view(), name='contact'),
]