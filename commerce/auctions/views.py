from auctions.forms import newProductForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import *


def index(request):

    active = listings.objects.all()
    return render(request, "auctions/index.html",{"active":active})


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def product(request,item):
    item = int(item)
    print(item+1)
    print("####################################################")
    if request.method == "POST":
        new_bid = request.POST["bid"]
        product = listings.objects.get(pk = item)

        print(new_bid)
        if (int(new_bid) > product.current_bid):
            product.current_bid = new_bid
            product.save()


    try: 
        product = listings.objects.get(pk = item)
        comments = product.comments.all()
        return render(request,"auctions/product.html",{"product":product,"comments":comments})
    except:
        return redirect("index")

def watch_list(request):
    name = User.objects.get(username = request.user)
    list = name.list.all()
    return render(request,"auctions/watch_list.html",{"watch_list":list})

def new_product(request):
    if request.method == "POST":
        form = newProductForm(data=request.POST, files=request.FILES)
        new_item = form.save(commit=False)
        new_item.current_bid = new_item.start_bid
        new_item.save()

    form = newProductForm()
    return render(request,"auctions/new_product.html",{'form':form})
