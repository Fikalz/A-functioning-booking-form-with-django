from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('Date')
        time = request.POST.get('Time')
        person = request.POST.get('person')

        # Save the booking
        Booking.objects.create(
            name=name,
            email=email,
            date=date,
            time=time,
            person=person
        )
        # Booking.save()

        # Redirect after saving (prevents re-submitting on refresh)
        return redirect('success')

    return render(request, 'index.html')  # your HTML form file


def booking_success(request):
    return render(request, 'booking_success.html')

def showdb(request):
    
    individualbooking = Booking.objects.all()
    # context is dictionary
    context={
        'individualbooking':individualbooking
    }
    return render(request,'showdb.html',context)
    

def update(request, id):
    updateInfo = Booking.objects.get(id=id)
    
    if request.method == 'POST':
        updateInfo.name = request.POST.get('name')
        updateInfo.email = request.POST.get('email')
        updateInfo.date = request.POST.get('date')
        updateInfo.time = request.POST.get('time')
        updateInfo.person = request.POST.get('person')
        
        updateInfo.save()
        
        return redirect('showdb')
    
    
    context = {
        'updateInfo': updateInfo
    }
    
    return render(request,'correction.html', context)

def delete_contact(request,id):
    
    booking=get_object_or_404(Booking, id=id)
    
    if  request.method=='POST':
        booking.delete()
        return redirect('showdb')
    
    context={
        'booking': booking
    }
    return render(request,'delete_confirmation.html', context)