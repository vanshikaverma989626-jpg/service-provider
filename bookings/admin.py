from django.contrib import admin
from .models import Booking, Review


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'customer',
        'provider',
        'status',
        'date'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'customer__username',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'booking',
        'rating',
        'created_at'
    )

    search_fields = (
        'comment',
    )