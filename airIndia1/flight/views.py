from decimal import Decimal
from django.shortcuts import render, get_object_or_404,redirect
from .models import Booking, airindia_Flight
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
@login_required(login_url='signin')
def bookflight(request):
    context={}
    if request.method=="POST":

        source=request.POST.get('from')
        dest=request.POST.get('to')
        date=request.POST.get('departure')
        flights=airindia_Flight.objects.filter(source=source, dest=dest, date=date)
        if flights:
            return render(request,'list.html',locals())
        else:
            context['error']="No flights available"
            return render(request, 'bookflight.html', context)   

    return render(request, 'bookflight.html', context)

from django.shortcuts import get_object_or_404

def bookings(request):
    context = {}
    if request.method == "POST":
        flight_id = request.POST.get('flight_id')
        nos = request.POST.get('no_seats')
        
        # Check if flight exists
        try:
            flight = airindia_Flight.objects.get(id=flight_id)
        except airindia_Flight.DoesNotExist:
            context["error"] = "Invalid flight selection"
            return render(request, 'bookflight.html', context)

        if flight:
            if flight.rem >= int(nos):
                # Proceed with booking
                name_r = flight.flight_name
                email_r = request.user.email
                total = int(nos) * flight.price
                source_r = flight.source
                dest_r = flight.dest
                nos_r = Decimal(flight.nos)
                price_r = flight.price
                time_r = flight.time
                date_r = flight.date
                username_r = request.user.username
                userid_r = request.user.id
                rem_r = flight.rem - int(nos)

                # Update remaining seats
                airindia_Flight.objects.filter(id=flight_id).update(rem=rem_r)

                # Create booking record
                book=Booking.objects.create(name=username_r, email=request.user.email,
                                            userid=userid_r, flightid=flight_id,    flight_name=name_r,
                                            source=source_r, dest=dest_r, price=price_r, nos=int(nos), date=date_r, time=time_r, status='B')
                print('book id', book.id)
                return render(request, 'bookings.html', locals())
            else:
                # Not enough seats
                context["error"] = "Sorry, select fewer seats"
                return render(request, 'bookflight.html', context)
    else:
    # If GET request or other, render the booking form
        return render(request, 'bookflight.html', context)
   
@login_required(login_url='signin')               
def seebookings(request,new={}):
         context={}
         id_r=request.user.id
         book_list=Booking.objects.filter(userid=id_r)
         if book_list:
                  return render(request,'seebookings.html',locals())
         else:
                  context["error"]="Sorry no flight booked"
                  return render(request,'seebookings.html',context)              

@login_required(login_url='signin')
def cancellings(request):
         context={}
         if request.method=='POST':
            id_r=request.POST.get('flight_id')
            try:
                book=Booking.objects.get(id=id_r)
                flight=airindia_Flight.objects.get(id=book.flightid)
                rem_r=flight.rem + book.nos
                airindia_Flight.objects.filter(id=book.flightid).update(rem=rem_r)
                Booking.objects.filter(id=id_r).update(status='CANCELLED')
                Booking.objects.filter(id=id_r).update(nos=0)
                return redirect(seebookings)
            except Booking.DoesNotExist:
                context["error"]="Sorry you have not booked"
                return render(request,'error.html',context)
         else:
                return render(request,'bookingflight.html',context)  
          
def signup(request):
     context={}
     if request.method=='POST':
         name_r=request.POST.get('name')
         email_r=request.POST.get('email')
         password_r=request.POST.get('password')
         user=User.objects.create_user(name_r,email_r,password_r)
         if user:
            login(request,user)
            return render(request,'thanks.html')
         else:
            context["error"]="Invalid credintial"
            return render(request,'signup.html',context)
     else:
        return render(request,'signup.html',context)

def signin(request):
     context={}
     if request.method=='POST':
         username_r=request.POST.get('username')
         password_r=request.POST.get('password')
         user=authenticate(request,username=username_r,password=password_r)
         if user is not None:
            login(request,user)
            return render(request,'thanks.html')
         else:
            context["error"]="Invalid credintial"
            return render(request,'signin.html',context)
     else:
        return render(request,'signin.html',context)
     
def signout(request):
    logout(request)
    return redirect(home)
