from django.db import models

class File(models.Model):

  category = models.CharField(max_length=20)
  ads = models.CharField(max_length=5)
  url1 = models.CharField(max_length=20)
  file1 = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)
