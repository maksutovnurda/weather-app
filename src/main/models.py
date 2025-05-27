from django.db import models

class Search(models.Model):
    visitor_id = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    count = models.IntegerField(default=1)
    last_search = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city