from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .decorators import unauthenticated_user, allowed_user, staff_only
from django.contrib.auth.models import Group


def home(request):
    return HttpResponse('successfully setup done.')

#
# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             if user.is_superuser or user.is_staff:
#                 return redirect('staff_stat')
#             return redirect('home')
#         else:
#             messages.info(request, 'Username or Password is incorrect')
#             return render(request, 'login.html')
#     return render(request, 'login.html', {})
#
#
# def logoutUser(request):
#     logout(request)
#     return redirect('home')
#
#
# @csrf_protect
# def register(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         # form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             name = form.cleaned_data.get('username')
#
#             group = Group.objects.get(name='Customer')
#             user.groups.add(group)
#
#             messages.success(request, 'Account is Created successfully for ' + name)
#             return redirect('register_login')
#     context = {'form': form}
#     return render(request, 'signup.html', context)
