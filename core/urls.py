from django.urls import path
from . import views

urlpatterns = [
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("contact/", views.contact, name="contact"),
    path("admin_orders/", views.admin_orders, name="admin"),
    path('mark-done/<int:id>/', views.mark_done, name='mark_done'),
]