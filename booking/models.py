from django.db import models

class Booking(models.Model):
    MATERIAL_CHOICES = [
        ('Plastic', 'Plastic'),
        ('Oil', 'Cooking Oil'),
        ('Paper', 'Paper'),
        ('Cardboard', 'Cardboard'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    date = models.DateField()
    materials = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.date}"