# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from models import tasks
from forms import TaskForm
def task(request):
    return render_to_response('todo/base.html', {'tasks': tasks.objects.all(), 'form': TaskForm},  context_instance=RequestContext(request))

def addtask(request):
    if request.method == 'POST': # If the form has been submitted...
        form = TaskForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            task = form.cleaned_data['task']
            newtask = tasks(task=task)
            newtask.save()
            return HttpResponseRedirect('/tasks/')
        else:
            return HttpResponse("Here's the tex.")
    else:
        return HttpResponse("Here's the text.")

def finishtask(request):
    if request.is_ajax(): # If the form has been submitted...
        ftask = tasks.objects.get(id=request.POST['id'])
        ftask.status = 1
        ftask.save()
        return HttpResponse("Finished")