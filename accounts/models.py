from django.db import models
from django.contrib.auth.models import User
from services.models import Category
#User model of django gives us username password and email fields. We will create a profile model to store additional information about the user.

class Profile(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('provider', 'Provider'),
    ]                               # creates adropdown instead of random values in the role field of the profile model. The first value is stored in the database and the second value is displayed in the dropdown.
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )                               # one-one relationship: 1 user 1 profile
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    phone = models.CharField(max_length=15)
    society = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )                               # this isa relationship between the profile model and the category model. A provider can have one category but a category can have many providers. If a category is deleted, the category field of the provider will be set to null.
                                    #foreign key used to remove duplicates(pumber,Plumber,PLUMBER),Everyone references same category.
    price_per_visit = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    experience_years = models.IntegerField(
        null=True,
        blank=True
    )
    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.user.username
