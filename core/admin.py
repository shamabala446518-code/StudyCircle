from django.contrib import admin
from .models import StudyGroup, StudySession, Note, Task, StudyFile, ContactMessage

admin.site.register(StudyGroup)
admin.site.register(StudySession)
admin.site.register(Note)
admin.site.register(Task)
admin.site.register(StudyFile)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)