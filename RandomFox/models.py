from django.db import models

# Create your models here.


class Fox(models.Model):
    id_from_web = models.IntegerField()
    link_from_web = models.CharField(max_length=200)
    image_form_web = models.ImageField(upload_to='media/foxes/')
    access_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link_from_web
