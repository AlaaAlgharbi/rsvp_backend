from django.db import models

# Create your models here.

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,db_index=True)
    firstName = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    joiningUs=models.BooleanField(default=False)
    side=models.TextField(max_length=100)
    def __str__(self):
        return self.firstName + " " + self.lastName
    class Meta:
        ordering = ['-created_at']