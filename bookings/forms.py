from django import forms
from .models import Booking, Review
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'date',
            'time_slot',
            'address',
            'description'
        ]
    def clean_date(self):
        booking_date = self.cleaned_data['date']
        if booking_date < date.today():
            raise forms.ValidationError(
                "Past dates are not allowed."
            )
        return booking_date

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[
            (1, '⭐'),
            (2, '⭐⭐'),
            (3, '⭐⭐⭐'),
            (4, '⭐⭐⭐⭐'),
            (5, '⭐⭐⭐⭐⭐')
        ]

    )
    class Meta:
        model = Review
        fields = [
            'rating',
            'comment'
        ]