from django.contrib import admin
from api.models import \
    SectionConfig, \
    WhenSection, \
    WhereSection, \
    TransportSection, \
    TrzaskanieSection, \
    ContactSection
# Register your models here.

admin.site.register(SectionConfig)
admin.site.register(WhenSection)
admin.site.register(WhereSection)
admin.site.register(TransportSection)
admin.site.register(TrzaskanieSection)
admin.site.register(ContactSection)