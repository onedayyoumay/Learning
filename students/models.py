from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
import datetime
# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    photography = models.ImageField(upload_to="images")
    b_date = models.DateField()
    ticket_number = models.CharField(max_length=12)
    group_id = models.ForeignKey('Group', related_name='+')

class Group(models.Model):
    group_number = models.CharField(max_length=3)
    group_head = models.OneToOneField('Student', related_name='+', blank=True, null=True)

class Loggs(models.Model):
    action = models.CharField(max_length=200)
    date = models.DateField()
    base = models.CharField(max_length=200)

@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Group)
def my_handler(sender, **kwargs):
    try:
        Loggs(action="Modified", date=datetime.datetime.now().date(), base=sender.objects.get(id=kwargs['instance'].pk)).save()
    except:
        Loggs(action="Created", date=datetime.datetime.now().date(), base=kwargs['instance']).save()

@receiver(pre_delete, sender=Student)
@receiver(pre_delete, sender=Group)
def my_deleter(sender, **kwargs):
    Loggs(action="Delete", date=datetime.datetime.now().date(), base=kwargs['instance']).save()