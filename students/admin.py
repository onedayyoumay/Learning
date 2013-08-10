from django.contrib import admin
from models import Group, Student

class GroupAdmin(admin.ModelAdmin):
    fields = ('group_number', 'group_head')
    list_display = ('group_number',)
admin.site.register(Group, GroupAdmin)


class StudentAdmin(admin.ModelAdmin):
    fields = ('full_name', 'photography', 'b_date', 'ticket_number', 'group_id')
    list_display = ('full_name',)
admin.site.register(Student, StudentAdmin)