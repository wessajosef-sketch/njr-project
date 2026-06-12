from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactMessage
from booking.models import Booking
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm_password"]

        if password != confirm:
            return render(request, "signup.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})

        User.objects.create_user(username=username, email=email, password=password)
        return redirect("signin")

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "signin.html", {"error": "Invalid username or password"})

    return render(request, "signin.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "contact.html", {"success": "Message sent successfully!"})

    return render(request, "contact.html")


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
@login_required
@csrf_exempt
def mark_done(request, id):
    print("REQUEST METHOD:", request.method)

    if request.method == "POST":
        booking = get_object_or_404(Booking, id=id)
        booking.status = "done"
        booking.save()

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error", "msg": "Only POST allowed"})


@user_passes_test(is_admin)
def admin_orders(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'admin_orders.html', {'bookings': bookings})