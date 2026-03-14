from django.shortcuts import render, redirect
from .models import Appointment

# Create your views here.
def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def appointment(request):
    if request.method == 'POST':
        all = Appointment(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            datetime = request.POST.get('date_and_time_of_appointment'),
            department = request.POST.get('department'),
            doctor = request.POST.get('doctor'),
            message = request.POST.get('message')
        )
        all.save()
        return render(request, 'appointment.html') 

    else:
        return render(request, 'appointment.html')

def show(request):
    allappointments = Appointment.objects.all()
    return render(request, 'show.html', {'allappointments':allappointments}) 

def showpatient(request):
    allpatients = Patient.objects.all()
    return render(request, 'showpatient.html', {'allpatients':allpatients})

def delete(request, id):
    myappointment = Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')