from django.db import models

# Create your models here.
class Category(models.Model):       #created a db table for the job category
    name = models.CharField(max_length=50) # name of job
    description = models.TextField()  #work description
    class Meta: # only affects admin display(the spelling of the plural name of the model in the admin interface)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name # with this method, when we print the object, it will return the name of the category(cleaner/plumber/tutor...) instead of the default representation(category object 1/2/3...).
