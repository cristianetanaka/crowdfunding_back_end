from django.db import models
from django.contrib.auth import get_user_model # refers to the user model created, using this function is better than user model itself
from django.db.models import Sum

# Create your models here.
class Project(models.Model):
     
     CATEGORY_CHOICES = {
       ("TEXT", 'Textile'),
       ("ORGANIC", 'Organic composte'),
       ("SOFT", 'Soft plastics'),
       ("HOUSE", 'Households'),
       ("UHT", 'UHT packaging'),
       ("ELECTRICAL", 'Eletronics'),
       ("FURNITURE", 'Furniture'),
       ("PLASTICS", 'all plastics'),
       ("BEDDING", 'BLANKETS AND PILLOW'),
       ("MATTRESS", 'Matresses')
    }
      
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
     
def update_total(self, project_id):
        pledges = Pledge.objects.filter(project_id=project_id)
        self.total = pledges.aggregate(Sum('amount'))['amount__sum']
        self.save()
        
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