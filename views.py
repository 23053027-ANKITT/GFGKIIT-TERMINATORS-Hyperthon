from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def index(request):
    return render(request, 'registration.html')

def payment(request):
    return render(request, 'payment.html')

def add_person(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_method = request.POST.get('paymentMethod')
        
        Person.objects.create(roll=roll, name=name, email=email, phone_number=phone, payment_method=payment_method)

        return HttpResponse(f"Payment completed successfully for {name} using {payment_method}.")
    
    else:
        return HttpResponse("Invalid request.", status=400)
