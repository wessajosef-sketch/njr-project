from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
import json

@csrf_exempt
def create_booking(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            booking = Booking.objects.create(
                full_name=data.get("full_name"),
                phone_number=data.get("phone_number"),
                address=data.get("address"),
                date=data.get("date"),  # must be YYYY-MM-DD
                materials=data.get("materials"),
            )
            return JsonResponse({"success": True, "booking_id": booking.id})
        return JsonResponse({"success": False, "error": "Invalid request"})
    except Exception as e:
        # <-- instead of crashing, return JSON error
        return JsonResponse({"success": False, "error": str(e)})
    