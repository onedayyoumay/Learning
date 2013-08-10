from django.core.management.base import BaseCommand
from mysite.students.models import Student, Group

class Command(BaseCommand):
    args = '<Group_id Student_id ...>'
    help = 'Show all groups and students'

    def handle(self, *args, **options):
        groups = Group.objects.all() 
        for i in range(0,len(groups)):
            print 'Group:'+groups[i].group_number
            students = Student.objects.filter(group_id=groups[i].id)
            for n in range(0, len(students)):
                print '    Student:'+students[n].full_name