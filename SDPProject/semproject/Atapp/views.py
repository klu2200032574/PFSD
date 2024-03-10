cdfrom django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Book, Contact, News


# Create your views here

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST.get('message')
        hr = Contact(name=name, email=email, subject=subject, message=message)
        hr.save()

    return render(request, "contact.html")


def services(request):
    return render(request, "services.html")


def team(request):
    return render(request, "team.html")


def gallery(request):
    return render(request, "gallery.html")


def faqs(request):
    return render(request, "faqs.html")


def terms(request):
    return render(request, "terms.html")


def thanks(request):
    return render(request, "thanks.html")


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']



        user = User.objects.create_user(username=username, email=email, password=password1, first_name=firstname,last_name=lastname)
        user.save()

        messages.success(request, "Your account is register succesfully created")
        return redirect('signin')

    return render(request, "signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            return render(request, "dashboard.html", )
        else:
            messages.error(request, "wrong details")
            return redirect('/')

    return render(request, "signin.html")


def signout(request):
    logout(request)

    return render(request, "signout.html")


def dashboard(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST.get('gender')
        age = request.POST['age']
        event = request.POST.get('event')
        venues = request.POST.get('venues')
        area = request.POST['area']
        city = request.POST['city']
        pincode = request.POST['pincode']
        state = request.POST['state']
        description = request.POST['description']

        har = Book(firstname=firstname, lastname=lastname, email=email, phone=phone, gender=gender, age=age,
                   event=event, venues=venues, area=area, city=city, pincode=pincode, state=state,
                   description=description)
        har.save()
        return render(request, "thanks.html")

    return render(request, "dashboard.html")
