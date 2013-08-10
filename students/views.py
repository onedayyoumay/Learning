# Create your views here.
from django.shortcuts import render_to_response
from models import Student, Group
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from forms import AuthForm, Add_group, Add_student
from django.core.context_processors import csrf
from django.template import RequestContext
def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/students/')



def groups(request):
    groups_info = Student.objects.raw('''select students_group.id, students_group.group_number,a.full_name, count(students_student.id) as amount
                                from students_student right join students_group
                                on students_student.group_id_id=students_group.id left join students_student as a on a.id=students_group.group_head_id
                                group by students_group.id''')
    return render_to_response('students/groups.html', {'groups': groups_info, 'form': AuthForm,}, context_instance=RequestContext(request))

def group_info(request):
    if request.method == 'GET' and 'g_num' in request.GET:
        group_n = request.GET['g_num']
        g_students = Student.objects.filter(group_id=group_n)
        paginator = Paginator(g_students, 1)
        # Make sure page request is an int. If not, deliver first page.
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        # If page request (9999) is out of range, deliver last page of results.
        try:
            contacts = paginator.page(page)
        except (EmptyPage, InvalidPage):
            contacts = paginator.page(paginator.num_pages)
        return render_to_response('students/group_info.html', {"students": contacts, 'g_num': group_n}, context_instance=RequestContext(request))

@login_required
def delete(request):
    if request.method == 'GET' and 'type' in request.GET and 'nmb' in request.GET:
        if request.GET['type'] == 'Student':
            Student.objects.get(id=request.GET['nmb']).delete()
            return HttpResponseRedirect('/students/')
        if request.GET['type'] == 'Group':
            Group.objects.get(id=request.GET['nmb']).delete()
            return HttpResponseRedirect('/students/')

@login_required
def new_group(request):
    if request.method == 'POST':
        form = Add_group(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        return render_to_response('students/create_group.html', {'form': Add_group,}, context_instance=RequestContext(request))

@login_required
def new_student(request):
    if request.method == 'POST':
        form = Add_student(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
        else:
           return HttpResponse(request.FILES, request.POST)
    else:
        return render_to_response('students/create_student.html', {'form': Add_student,}, context_instance=RequestContext(request))

@login_required
def manage_student(request):
    if request.method == 'GET' and 's_nmb' in request.GET:
        form = Add_student()
        article = Student.objects.get(pk=request.GET['s_nmb'])
        form = Add_student(instance=article)
        return render_to_response('students/m_student.html', {'student': '?s_nmb='+request.GET['s_nmb'],'form': form,}, context_instance=RequestContext(request))
    if request.method == 'POST' and 's_nmb' in request.GET:
        form = Add_student()
        article = Student.objects.get(pk=request.GET['s_nmb'])
        form = Add_student(request.POST, request.FILES, instance=article)
        form.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

@login_required
def manage_group(request):
    if request.method == 'GET' and 'g_nmb' in request.GET:
        form = Add_group()
        article = Group.objects.get(pk=request.GET['g_nmb'])
        form = Add_group(instance=article)
        return render_to_response('students/m_group.html', {'group': '?g_nmb='+request.GET['g_nmb'],'form': form,}, context_instance=RequestContext(request))
    if request.method == 'POST' and 'g_nmb' in request.GET:
        form = Add_group()
        article = Group.objects.get(pk=request.GET['g_nmb'])
        form = Add_group(request.POST, instance=article)
        form.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')