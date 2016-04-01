from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from studentdb.forms import StudentForm, UserForm
from studentdb.models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/studentdb/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/studentdb/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'studentdb/login.html', {})

def register(request):
    registred = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registred = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,'studentdb/register.html',{'user_form':user_form, 'registred':registred})

def index(request):
    return render(request, 'studentdb/index.html', {})

def view(request):
    student_list = Student.objects.all()
    context_dict = {'students': student_list}
    return render(request, 'studentdb/view.html',context_dict)

@login_required
def add(request):
    registred = False
    if request.method == 'POST':
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            student_form.save()
            registred = True
        else:
            print student_form.errors
    else:
        form = StudentForm()
    return render(request,'studentdb/add.html',{'student_form' : student_form, 'registred':registred})

@login_required
def delete(request):
    if request.GET:
        delete_term = request.GET.get('D')
        result = Student.objects.get(pk=delete_term)
        Student.objects.get(pk=delete_term).delete()
        return render_to_response('studentdb/delete.html',{'result':result})
    return render(request,'studentdb/delete.html',{})

"""def modify(request):
    #if request.GET:
    if request == 'POST':
       # mod = request.GET.get('M')
        modi = Student.objects.get(pk=1)
        form = StudentForm(request.POST,instance=modi)
        if form.is_valid():
            modi = form.save(commit=False)
            modi.studid = request.studid
            modi.name = request.name
            modi.age = request.age
            modi.sex = request.sex
            modi.marks = request.marks
            modi.save()
        else:
             print StudentFrom.errors
    else:
        form = StudentForm()
    return render(request,'studentdb/modify.html',{'form':form})
   # return render(request,'studentdb/modify.html',{})
"""
def search(request):
    if request.GET:
        search_term = request.GET.get('S')
        results = Student.objects.filter(name__istartswith=search_term)
        return render_to_response('studentdb/search.html',{'results':results})
    return render(request,'studentdb/search.html',{})
