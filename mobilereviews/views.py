from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Mobiles, User, UserRatings
# Create your views here.

def index(request):
    items=Mobiles.objects.all()
    return render(request,"mobilereviews/index.html",{
        "items":items
    })        
        
def submitrating(request,mobileid):
    curr_mobile = Mobiles.objects.get(id=mobileid)
    curr_rate = curr_mobile.rating
    curr_count = curr_mobile.rcount
    if request.method == "POST":
        user_rate = float(request.POST.get("urate"))
        user_rate = round(user_rate,1)
        nrate = curr_rate+((user_rate-curr_rate)/(curr_count+1))
        curr_mobile.rating = nrate
        curr_mobile.rcount=curr_count+1
        curr_mobile.save()
        #saving the user and mobile in the userratings tabele
        x = UserRatings() 
        x.xuser = request.user.username
        x.mobileid = mobileid
        x.save()
        #redirecting
        response = redirect('mobile',mobileid=mobileid)
        response.set_cookie('errorgreen','you have rated the mobile',max_age=3)
        return response
    else:
        return redirect('index')

def mobile(request,mobileid):
    try:
        item = Mobiles.objects.get(id=mobileid)
    except:
        return redirect('index')
    if request.user.username:
        try:
            if UserRatings.objects.get(xuser = request.user.username, mobileid = mobileid):
                added = True
        except:
            added = False
    else:
        added = False
    return render(request,"mobilereviews/mobilepage.html",{
        "i":item,
        "added":added
    })

def profile(request,username):
    if request.user.username:
        try:
            w=UserRatings.objects.filter(xuser=username)
            items = []
            for i in w:
                items.append(Mobiles.objects.filter(id=i.mobileid))
            return render(request,"mobilereviews/profilepage.html",{
                "items":items
            })
        except:
             return render(request,"mobilereviews/profilepage.html",{
                "items":None
            })
    else:
        return redirect('index')                     

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "mobilereviews/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "mobilereviews/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mobilereviews/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mobilereviews/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "mobilereviews/register.html")