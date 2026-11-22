from django.db import models

# Create your models here.


# Activity 2

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["completed", "created_at"]
        
    def __str__(self):
        return self.title