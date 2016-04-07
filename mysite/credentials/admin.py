from django.contrib import admin
from credentials.models import contact,internships,postgrad,undergrad,srsec,sec,languages,projects,photo
# Register your models here.

admin.site.register(contact)
admin.site.register(postgrad)
admin.site.register(undergrad)
admin.site.register(srsec)
admin.site.register(sec)
admin.site.register(internships)
admin.site.register(languages)
admin.site.register(projects)
admin.site.register(photo)