from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # connect core app

    # Static pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('aboutus/', TemplateView.as_view(template_name='aboutus.html'), name='aboutus'),
    path('booking/', TemplateView.as_view(template_name='booking.html'), name='booking'),
    path('rewards/', TemplateView.as_view(template_name='rewards.html'), name='rewards'),
    path('admin_orders/', TemplateView.as_view(template_name='admin_orders.html'), name='admin_orders'),
    path('booking/', include('booking.urls')),
    path("", include("core.urls")),
]