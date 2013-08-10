from django import template
from django.core import urlresolvers
from mysite.students.models import Student, Group
register = template.Library()
grp = template.Library()
def s_tag(self):
    student = Student.objects.get(pk=self)
    return  urlresolvers.reverse("admin:%s_%s_change" %
        (student._meta.app_label, student._meta.module_name), args=(student.id,))

def g_tag(self):
    group = Group.objects.get(pk=self)
    return  urlresolvers.reverse("admin:%s_%s_change" %
        (group._meta.app_label, group._meta.module_name), args=(group.id,))

register.simple_tag(s_tag)
register.simple_tag(g_tag)