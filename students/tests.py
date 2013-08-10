from django.test import TestCase
from models import Group, Student
from django.contrib.auth.models import User
from django.test import Client
import datetime
class SimpleTest(TestCase):
    def test_secure_page(self):
        c = Client()
        self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('hello')
        self.user.save()
        response = c.post('/login/', {'username': 'testuser', 'password': 'hello'})
        response = c.post('/students/add_group/', {'group_number': '13K'})
        g = Group.objects.get(group_number='13K')
        with open('/home/peacefulgarden/mysite/media/images/1d34b535468c_3.jpg') as fp:
            response = c.post('/students/add_student/', {'full_name': 'John Smith', 'photography': fp,'b_date': datetime.datetime.now().date(), 'ticket_number':'07','group_id': g.pk})
        grp = Group.objects.get(pk=1)
        std = Student.objects.get(pk=1)
        print 'Group {0} is created'.format(grp.group_number)
        print 'Student {0} is created in group {1}'.format(std.full_name, std.group_id.group_number)