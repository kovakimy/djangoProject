from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm, MakeRecordForm, MakeRecordEyebrowsForm, MakeRecordEyelashesForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from .models import Records, RecordsEyelashes, RecordsEyebrows
from django.views.generic import DeleteView


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Этот username уже занят.")
        else:
            email = request.POST.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Этот email уже занят.")
            else:
                role = request.POST.get('role')
                if (role == 'master') or (role == 'client'):
                    if form.is_valid():
                        ins = form.save()
                        password = form.cleaned_data['password1']
                        user = authenticate(email=email, username=username, password=password)
                        user_group = Group.objects.get(name=role)
                        user.groups.add(user_group)
                        ins.email = email
                        ins.username = username
                        ins.save()
                        form.save_m2m()
                        messages.success(request, 'Регистрация прошла успешно')
                        return redirect('login')
                else:
                    messages.error(request, "Неверно введена роль, нужно master или client")
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'main/register.html', context)


def logout_f(request):
    logout(request)
    return redirect('login')


def record(request):
    records_nails = None
    records_eyebrows = None
    records_eyelashes = None
    context = {}
    if request.user.is_authenticated:
        if (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'master'):
            records_nails = Records.objects.filter(master=request.user.username).order_by('time')
            context['master'] = True
        elif (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'client'):
            records_nails = Records.objects.filter(client=request.user.username).order_by('time')
            context['master'] = False
        context['records_nails'] = records_nails
    else:
        context['records_nails'] = records_nails

    if request.user.is_authenticated:
        if (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'master'):
            records_eyebrows = RecordsEyebrows.objects.filter(master=request.user.username).order_by('time')
            context['master'] = True
        elif (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'client'):
            records_eyebrows = RecordsEyebrows.objects.filter(client=request.user.username).order_by('time')
            context['master'] = False
        context['records_eyebrows'] = records_eyebrows
    else:
        context['records_eyebrows'] = records_eyebrows

    if request.user.is_authenticated:
        if (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'master'):
            records_eyelashes = RecordsEyelashes.objects.filter(master=request.user.username).order_by('time')
            context['master'] = True
        elif (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'client'):
            records_eyelashes = RecordsEyelashes.objects.filter(client=request.user.username).order_by('time')
            context['master'] = False
        context['records_eyelashes'] = records_eyelashes
    else:
        context['records_eyelashes'] = records_eyelashes

    return render(request, 'main/records.html', context)


def create_record_nails(request):
    form = None
    error = ''
    context = {}
    if (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'master'):
        return redirect('record')
    if request.method == 'POST':
        form = MakeRecordForm(request.POST)
        time = request.POST.get('time')
        master = request.POST.get('master')
        if Records.objects.filter(time=time, master=master).exists():
            messages.error(request, "Это время уже занято.")
            error = "Это время уже занято."
        else:
            form.time = time
            form.master = master
            if form.is_valid():
                ins = form.save()
                ins.client = request.user.username
                ins.master = master
                ins.save()
                form.save()
                messages.success(request, 'Запись прошла успешно')
                return redirect('record')
    else:
        form = MakeRecordForm()
    context['form'] = form
    context['error'] = error

    return render(request, 'main/create_record_nails.html', context)


class DeleteRecordNails(DeleteView):
    model = Records
    template_name = 'main/delete_record_nails.html'
    success_url = '/record'


def create_record_eyebrows(request):
    form = None
    error = ''
    if (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'master'):
        return redirect('record')
    if request.method == 'POST':
        form = MakeRecordEyebrowsForm(request.POST)
        time = request.POST.get('time')
        master = request.POST.get('master')
        if RecordsEyebrows.objects.filter(time=time, master=master).exists():
            messages.error(request, "Это время уже занято.")
            error = "Это время уже занято."
        else:
            form.time = time
            form.master = master

            if form.is_valid():
                ins = form.save()
                ins.client = request.user.username
                ins.master = master
                ins.save()
                form.save()
                messages.success(request, 'Запись прошла успешно')
                return redirect('record')
    else:
        form = MakeRecordEyebrowsForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create_record_eyebrows.html', context)


class DeleteRecordEyebrows(DeleteView):
    model = RecordsEyebrows
    template_name = 'main/delete_record_eyebrows.html'
    success_url = '/record'


def create_record_eyelashes(request):
    form = None
    error = ''
    if (len(request.user.groups.all()) > 0) and (request.user.groups.all()[0].name == 'master'):
        return redirect('record')
    if request.method == 'POST':
        form = MakeRecordEyelashesForm(request.POST)
        time = request.POST.get('time')
        master = request.POST.get('master')
        if RecordsEyelashes.objects.filter(time=time, master=master).exists():
            messages.error(request, "Это время уже занято.")
            error = "Это время уже занято."
        else:
            form.time = time
            form.master = master

            if form.is_valid():
                ins = form.save()
                ins.client = request.user.username
                ins.master = master
                ins.save()
                form.save()
                messages.success(request, 'Запись прошла успешно')
                return redirect('record')
    else:
        form = MakeRecordEyelashesForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create_record_eyelashes.html', context)


class DeleteRecordEyelashes(DeleteView):
    model = RecordsEyelashes
    template_name = 'main/delete_record_eyelashes.html'
    success_url = '/record'
