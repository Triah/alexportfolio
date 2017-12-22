from django.db import models


class Image(models.Model):
    image_id = models.CharField(max_length=20)

    def __str__(self):
        return self.image_id
