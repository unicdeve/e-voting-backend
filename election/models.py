from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here.
class Election(models.Model):
  user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='created_elections')
  title = models.CharField(max_length=50, unique=True)
  image = models.CharField(max_length=150)
  created_at = models.DateTimeField(auto_now_add=True)
  start_time = models.DateTimeField()

  def __str__(self):
    return self.title
