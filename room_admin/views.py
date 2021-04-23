from django.shortcuts import render,redirect
from login.models import Admin
from booking.models import Booking,Storages
from datetime import date
from django.contrib import messages
import datetime
def dashboard(request):
  if not request.session.get('username',None):
      return redirect('manager_login')
  if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
  if request.session.get('username',None) and request.session.get('type',None)=='manager':
      username=request.session['username']
      data=Admin.objects.get(username=username)
      room_data=data.storages_set.all()
      booked=room_data.filter(is_available=False).count()
      print(booked)
      return render(request,"manager_dash/index.html",{"room_data":room_data,"manager":data,"booked":booked})
  else:
      return redirect("manager_login")
def add_storage(request):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.method=="GET":
        return render(request,"manager_dash/add-room.html",{})
    else:
            state_name=request.POST['state_name']
            city_name=request.POST['city_name']
            price=request.POST['price']
            room_image=request.FILES.get('room_image',None)
            storage_location=request.POST['storage_location']
            start_day=request.POST['start_day']
            error=[]
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter price")
            if(len(start_day)<3):
                error.append(1)
                messages.warning(request,"Please add the starting day")
            if(not len(error)):
                manager=request.session['username']
                manager=Admin.objects.get(username=manager)
                room=Storages(state_name=state_name,city_name=city_name,price=price,storage_location=storage_location,start_date=datetime.datetime.strptime(start_day, "%d %B, %Y").date(),room_image=room_image,manager=manager)
                room.save()
                messages.info(request,"Room Added Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-storage/new/')
def update_storage(request,storage_location):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    room=Storages.objects.get(storage_location=storage_location)
    if request.method=="GET":
        return render(request,"manager_dash/edit-room.html",{"room":room})
    else:
            price=request.POST['price']
            storage_location=request.POST['storage_location']
            error=[]
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter correct price")
            if(not len(error)):
                manager=request.session['username']
                manager=Admin.objects.get(username=manager)
                room.price=price
                room.storage_location=storage_location
                room.save()
                messages.info(request,"Room Data Updated Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-storage/update/'+room.city_name,{"room":room})

