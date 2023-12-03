from django.db import models

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class targetEvent(models.Model):
    target = models.CharField(max_length=200)
    subtitle = models.TextField()

    def __str__(self):
        return self.target