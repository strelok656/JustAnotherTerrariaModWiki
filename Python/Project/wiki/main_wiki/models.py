from django.db import models

class Wiki_pages(models.Model):
    title = models.CharField(max_length=100)
    description_path = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Info_card(models.Model):
    item_image_path = models.CharField(max_length=100)
    def __str__(self):
        return self.item_image_path