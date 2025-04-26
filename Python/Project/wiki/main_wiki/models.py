from django.db import models

class Wiki_pages(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Info_card(models.Model):
    item_image_path = models.CharField(max_length=100)
    placed_or_not = models.CharField(max_length=3)
    def __str__(self):
        return self.item_image_path
    
class Craft_card(models.Model):
    craft_text = models.CharField(max_length=200)
    def __str__(self):
        return self.craft_text