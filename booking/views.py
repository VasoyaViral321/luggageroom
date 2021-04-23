from django.shortcuts import render,redirect
from .models import Contact
from .models import Storages,Booking
from login.models import Customer
from django.contrib import messages
from django.http import HttpResponse
import datetime
def index(request):
    return render(request,'booking/index.html',{})
def contact(request):
    if request.method=="GET":
     return render(request,"contact/contact.html",{})
    else:
     username=request.POST['name']
     email=request.POST['email']
     message=request.POST['message']
     data=Contact(name=username,email=email,message=message)
     data.save()
     return render(request,"contact/contact.html",{'message':'Thank you for contacting us.'})
def about(request):
    return render(request,"about/about.html")
def howitworks(request):
    return render(request,"How-It-Works/how-it-works.html")
def book(request):
    if request.method=="POST":
        #city_name=request.POST['city_name']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        request.session['start_date']=start_date
        request.session['end_date']=end_date
        #request.session['city_name']=city_name
        #print(city_name)
        start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
        end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
        #no_of_days=(end_date-start_date).days
        data=Storages.objects.filter(is_available=True,start_date__lte=start_date)
        #request.session['no_of_days']=no_of_days
        return render(request,'booking/book.html',{'data':data})
    else:
        return redirect('index')
def book_now(request,id):
    if request.session.get("username",None) and request.session.get("type",None)=='customer':
        if request.session.get("no_of_days",1):
            no_of_days=request.session['no_of_days']
            start_date=request.session['start_date']
            end_date=request.session['end_date']
            request.session['storage_location']=id
            data=Storages.objects.get(storage_location=id)
            bill=data.price*int(no_of_days)
            request.session['bill']=bill
            roomManager=data.manager.username
            return render(request,"booking/book-now.html",{"no_of_days":no_of_days,"room_no":id,"data":data,"bill":bill,"roomManager":roomManager,"start":start_date,"end":end_date})
        else:
            return redirect("index")
    else:
        next="book-now/"+id
        return redirect('user_login')
def book_confirm(request):
    city_name=request.session['city_name']
    storage_location=request.session['storage_location']
    start_date=request.session['start_date']
    end_date=request.session['end_date']
    username=request.session['username']
    user_id=Customer.objects.get(username=username)
    room=Storages.objects.get(storage_location=storage_location)
    amount=request.session['bill']
    start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
    end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
    data=Booking(storage_location=room,start_day=start_date,end_day=end_date,amount=amount,user_id=user_id)
    data.save()
    room.is_available=False
    room.save()
    del request.session['start_date']
    del request.session['end_date']
    del request.session['bill']
    #del request.session['room_no']
    messages.info(request,"Room has been successfully booked")
    return redirect('user_dashboard')
def cancel_storage(request,id):
    data=Booking.objects.get(id=id)
   
    data.delete()
    return HttpResponse("Booking Cancelled Successfully")
def delete_storage(request,id):
    data=Storages.objects.get(id=id)
    manager=data.manager.username
    if manager==request.session['username']:
        data.delete()
        return HttpResponse("You have deleted the storage successfully")
    else:
        return HttpResponse("Invalid Request")


            



    
