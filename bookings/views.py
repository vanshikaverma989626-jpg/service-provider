from django.shortcuts import render
from bookings.models import Booking, Review, Profile
from .forms import BookingForm, ReviewForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def create_booking(request, provider_id):
    provider = get_object_or_404(
        Profile,
        id=provider_id
    ) 
    if not provider.is_available:
        messages.error(
            request,
            'This provider is currently unavailable for bookings.'
        )
        return redirect(
            f'/providers/{provider.id}/'
        )
    if request.method == 'POST':
        form = BookingForm(
            request.POST
        )
        if form.is_valid():
            booking_date = form.cleaned_data['date']
            time_slot = form.cleaned_data['time_slot']
            existing_booking = Booking.objects.filter(
                provider=provider,
                date=booking_date,
                time_slot=time_slot
            ).exclude(
                status='cancelled'
            ).exists()
            if existing_booking:
                form.add_error(
                    None,
                    "This time slot is already booked."
                )
            else:
                booking = form.save(
                    commit=False
                )
                booking.customer = request.user
                booking.provider = provider
                booking.status = 'pending'
                booking.save()
                messages.success(request,'Booking created successfully.')
                return redirect('/my-bookings/')
    else:
        form = BookingForm()

    return render(
        request,
        'bookings/create_booking.html',
        {
            'form': form,
            'provider': provider
        }
    )

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(customer=request.user)
    return render(
        request,
        'bookings/my_bookings.html',
        {
            'bookings': bookings
        }
    )

@login_required
def provider_dashboard(request):
    profile = request.user.profile
    if profile.role != 'provider':
        return render(
            request,
            'bookings/not_provider.html'
        )
    if not profile.category:
        return redirect(
            '/provider/profile/')
    bookings = Booking.objects.filter(
        provider=profile
    )

    return render(
        request,
        'bookings/provider_dashboard.html',
        {
            'bookings': bookings
        }
    )

@login_required
def accept_booking(request, id):
    booking = get_object_or_404(
        Booking,
        id=id
    )
    booking.status = 'accepted'
    booking.save()
    return redirect('/provider/dashboard/')

@login_required  
def reject_booking(request, id):
    booking = get_object_or_404(
        Booking,
        id=id
    )
    booking.status = 'rejected'
    booking.save()
    return redirect('/provider/dashboard/')

@login_required
def complete_booking(request, id):
    booking = get_object_or_404(Booking,id=id)
    booking.status = 'completed'
    booking.save()
    return redirect('/provider/dashboard/')

@login_required
def add_review(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id
    )
    # Only completed bookings can be reviewed
    if booking.status != 'completed':
        return redirect(
            '/provider/dashboard/'
        )
    # Prevent duplicate reviews
    if Review.objects.filter(
        booking=booking
    ).exists():
        return redirect(
            '/my-bookings/'
        )
    if request.method == 'POST':
        form = ReviewForm(
            request.POST
        )
        if form.is_valid():
            review = form.save(
                commit=False
            )
            review.booking = booking
            review.save()
            return redirect(
                '/provider/dashboard/'
            )
    else:
        form = ReviewForm()
    return render(
        request,
        'bookings/review_form.html',
        {
            'form': form,
            'booking': booking
        }
    )

@login_required
def cancel_booking(request, id):
    booking = get_object_or_404(
        Booking,
        id=id
    )
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
    return redirect(
        '/my-bookings/'
    )