from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
#A Django Model is a Python class that represents a database table.
#the heart of the marketplace.
#Python Class  →  Database Table
class Booking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )                               # Stores who created booking. A customer can have many bookings but a booking can have only one customer. If a customer is deleted, all their bookings will also be deleted.
    provider = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )                               # Stores which provider is assigned to the booking. A provider can have many bookings but a booking can have only one provider. If a provider is deleted, all their bookings will also be deleted.
    date = models.DateField()
    time_slot = models.CharField(
        max_length=50
    )
    address = models.CharField(
        max_length=255
    )
    description = models.TextField() # problem description provided by the customer. 
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer.username} - {self.provider.user.username}"

"""
 current schema:
 Customer
    │
    ▼
Booking
    │
Service Completed
    │
    ▼
Review

 """
class Review(models.Model):

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE
    )                               #onetoone relationship: 1 booking 1 review. If a booking is deleted, the review will also be deleted.
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Review {self.rating}/5"

"""
User
 │
 └── Profile
       │
       └── Category

User(Customer)
       │
       ▼
     Booking
       │
       ▼
     Review
"""
