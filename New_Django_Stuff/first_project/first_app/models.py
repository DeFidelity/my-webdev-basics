from django.db import models

# Create your models here.
class Game(models.Model):
    player = models.CharField(max_length=100, unique=True)
    scores = models.IntegerField(unique=False)
    name = models.CharField(max_length=130, unique=True)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.ForeignKey(Game, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=150, unique=True)
    student_dep = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.student_name

'''

create class, run python manage.py migrate, run python manage.py makemigrations,
run python manage.py migrate and the database would be created.
import the model to admin and create new admin with each class using
admin.site.register(class name)
To populate the database with dummy date, do pip instal django-django_seed
add 'django_seed' to INSTALLED_APPS in settings.py
run command python manage.py seed "app_name" --number='number of item you want
to populate'

'''
