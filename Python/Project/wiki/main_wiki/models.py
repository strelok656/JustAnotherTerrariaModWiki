from django.db import models

# class Wiki_pages(models.Model):
#     title = models.CharField(max_length=100)
#     # description = models.CharField(max_length=200)
#     def __str__(self):
#         return self.title

# class Info_card(models.Model):
#     item_image_path = models.CharField(max_length=100)
#     
#     def __str__(self):
#         return self.item_image_path

# class Craft_card(models.Model):
#     craft_text = models.CharField(max_length=200)
#     def __str__(self):
#         return self.craft_text

class Wiki_page(models.Model):
    url_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    item_image_path = models.CharField(max_length=100)
    placed_or_not = models.CharField(max_length=3)
    notes = models.CharField(max_length=500)
    def __str__(self):
        return self.url_title

class Craft_card(models.Model):
    url_title = models.ForeignKey(Wiki_page, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=200)
    amount = models.IntegerField()
    station = models.CharField(max_length=30)