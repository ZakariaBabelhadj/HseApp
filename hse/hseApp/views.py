from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import UserForm, LoisForm, LoginForm, SearchLois
from .models import User, Lois
from django.urls import reverse

# Create your views here.

def members(request, usrName = None):
    if request.method == 'GET':
        search = SearchLois(request.GET)
        if search.is_valid():
            namee = search.cleaned_data['name']
            dat = search.cleaned_data['date']
            if namee:
                data = Lois.objects.filter(name = namee)
            elif dat:
                data = Lois.objects.filter(date = dat)
            else:
                data = Lois.objects.all()
            return render(request, 'main.html', {'data': data, 'form': search, 'user': usrName})
    else:
        search = SearchLois()
        my_data = Lois.objects.all()
        return render(request, 'main.html', {'my_data': my_data, 'form': search, 'user': usrName})

def loisAdmin(request):
    if request.method == 'GET':
        search = SearchLois(request.GET)
        if search.is_valid():
            namee = search.cleaned_data['name']
            dat = search.cleaned_data['date']
            if namee:
                data = Lois.objects.filter(name = namee)
            elif dat:
                data = Lois.objects.filter(date = dat)
            else:
                data = Lois.objects.all()
            return render(request, 'main.html', {'data': data, 'form': search})
    else:
        search = SearchLois()
        my_data = Lois.objects.all()
        return render(request, 'admin.html', {'my_data': my_data, 'form': search})


# forms handling

def SignUp(request):
    if request.method == "POST":
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userModel = User(
                userName = userForm.cleaned_data['username'],
                pwd = userForm.cleaned_data['pwd'],
                email = userForm.cleaned_data['email'],
            )

            userModel.save()
            return redirect(reverse('main'))
    else:
        userForm = UserForm()
    return render(request, 'SignUp.html', {'form': userForm})


def Login(request):

    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            email = loginForm.cleaned_data['email']
            password = loginForm.cleaned_data['password']
            print("\nthe name of the userName is {} and his password is {}\n".format(email, password))
            try:
                user = User.objects.get(email = email, pwd = password)
                print("\nUser is  {} and {}\n".format(user.email, user.pwd))
                return redirect(members, usrName = user)
            except:
                return HttpResponseNotFound('Object not found')
    else:
        loginForm = LoginForm()
    return render(request, 'Login.html', {'form': loginForm})

def AddLois(request):

    if request.method == "POST":
        loisForm = LoisForm(request.POST)
        if loisForm.is_valid():
            dat = loisForm.cleaned_data['date'],
            if dat[5] == '0':
                dat[5].replace('0','')
            loisModel = Lois(
                name = loisForm.cleaned_data['name'],
                description = loisForm.cleaned_data['description'],
                date = dat,
                section = loisForm.cleaned_data['section'],
            )
            loisModel.save()
            return redirect(reverse('main'))
    else:
        loisForm = LoisForm()
    return render(request, 'LoisAdd.html', {'form': loisForm})

# display data

