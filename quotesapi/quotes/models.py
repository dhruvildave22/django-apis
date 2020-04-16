from django.db import models



class Quote(models.Model):
  author  = models.CharField(max_length=60)
  body = models.TextField()
  context = models.CharField(max_length=240, blank=True)
  source = models.CharField(max_length=120)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.author
  