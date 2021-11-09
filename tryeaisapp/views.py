import decimal
import json
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from tryeaisapp.models import Accounts, Profile

# Create your views here.
def home(request):
    return render(request, "index.html")

def login_user(request):
    # handling a get request (reponding with the login page)
    if request.method == "GET":
        return render(request, "login.html")

    # POST request = login request (authenticating user and logging user in)
    elif request.method == "POST":
        # getting credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # authenticating user
        user = authenticate(request, username=username, password=password)
        
        if user != None:
            # user exist
            login(request, user)
            print("User logged in")
            return HttpResponseRedirect('/dashboard')
        else:
            # invalid user
            messages.error(request, "Email/Password is invalid")
            return render(request, "login.html", { "username": username, "password": password })


def dashboard(request):
    return render(request, "dashboard.html")

def accounts(request):
    # fetching all accounts data from the database
    context = {}
    context['filter'] = 'all'
    # post request = filter
    if request.method == "POST" and request.POST.get('category') != "all":
        accounts = Accounts.objects.filter(category=request.POST.get('category')).order_by('-created_on')
        context['filter'] = request.POST.get('category')
    else:
        accounts = Accounts.objects.all().order_by('-created_on') # returns a QuerySet holding a list of objects that match the query
    # In simple words, a queryset is a collection of objects from the database.
    # We can use a 'for in' loop to access each object in our queryset
    context['accounts'] = accounts

    # calculating totals (total records for each category)
    context['total_income'] = 0
    context['total_expense'] = 0
    context['total_loan'] = 0
    context['total_amount'] = 0

    # for each object in accounts, we are accessing the category variable
    # if category is foo, access the amount property and add it to total_foo
    for account in accounts:
        context['total_' + account.category] += account.amount
        context['total_amount'] += account.amount
        
    return render(request, "accounts.html", context)

def settings(request):

    # updating settings
    if (request.method == "POST"):
        print(request.POST)
        field_list = [
            "d-reminders", 
            "w-reminders", 
            "m-reminders", 
            "y-reminders", 
            "d-reports",
            "w-reports",
            "m-reports",
            "y-reports"
        ]
        # initializing fields to False
        fields = {field: False for  field in field_list}
        
        for field in field_list:
            if field in request.POST.keys():
                fields[field] = True

        print(request.FILES)
        # creating or updating of exists
        Profile.objects.update_or_create(
            user = request.user,
            defaults={
                "budget": request.POST.get('budget'),
                "photo": request.FILES.get('photo'),
                "daily_reminder": fields["d-reminders"],
                "weekly_reminder": fields["w-reminders"],
                "monthly_reminder": fields["m-reminders"],
                "yearly_reminder": fields["y-reminders"],
                "daily_report": fields["d-reports"],
                "weekly_report": fields["w-reports"],
                "monthly_report": fields["m-reports"],
                "yearly_report": fields["y-reports"]
            }
        )

    # fetching data
    context = {}
    context['profile'] = Profile.objects.get(user=request.user)
    return render(request, "settings.html", context)

def save_records(request):
    # returning method not allowed for methods other than POST
    if request.method != "POST":
        return HttpResponse("<h1>Method Not Allowed</h1>")

    else:
        name = request.POST.get('name')
        type = request.POST.get('type')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        category = request.POST.get('category')
    
        accounts = Accounts(name=name, type=type, amount=float(amount), date=date, category=category)
        accounts.save()
        return HttpResponseRedirect('/accounts')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')

def delete_record(request, id):
    #  delete record
    # fetching record with id
    account = Accounts.objects.get(id=id)
    account.delete()
    return JsonResponse({ "status": 200})