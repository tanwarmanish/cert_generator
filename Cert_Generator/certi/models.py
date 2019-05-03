from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class ProjectData(models.Model):
    user = models.CharField(max_length=50,default='root')
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=40)
    template = models.FileField(upload_to='template_data/')
    data = models.FileField(upload_to='record_data/')
    current = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    link = models.CharField(max_length=200,default="Processing")
    def __str__(self):
        return str( 1169924 + self.project_id)
    def getProjectId(self):
        return str(project_id)

class ProjectStatus(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(ProjectData,on_delete=models.PROTECT)
    link = models.CharField(max_length=200)
