from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Booking
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def admin_orders(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'admin_orders.html', {'bookings': bookings})

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_orders(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'admin_orders.html', {'bookings': bookings})