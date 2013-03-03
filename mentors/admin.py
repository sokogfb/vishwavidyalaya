from django.contrib import admin
from mentors.models import Mentor, MenteeMeeting

class MentorAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'section', 'group')
    search_fields = ['faculty', 'section']

admin.site.register(Mentor, MentorAdmin)
admin.site.register(MenteeMeeting)
