from django.db import models
from django.contrib.auth import get_user_model # refers to the user model created, using this function is better than user model itself

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(    # tells Django for each project we need an ID/ also link two models together project and pledges
        'Project',
        on_delete=models.CASCADE, # cascade if project gets deleted will dele the pledges
        related_name='pledges' # associates Pledge to a project model
    )
    
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )