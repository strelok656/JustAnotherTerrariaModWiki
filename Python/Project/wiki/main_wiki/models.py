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

# class Article(models.Model):
#     # id = models.IntegerField(unique=True)
#     url_title = models.CharField(max_length=100)
#     def __str__(self):
#         return self.url_title

class Wiki_page(models.Model):
    # id = models.ForeignKey(Article, on_delete=models.CASCADE)
    url_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    item_image_path = models.CharField(max_length=100)
    placed_or_not = models.CharField(max_length=3)
    notes = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.url_title

class Craft_card(models.Model):
    url_title = models.ForeignKey(Wiki_page, on_delete=models.CASCADE, related_name='craft_cards')
    ingredients_name = models.CharField(max_length=100)
    ingredients_item_image_path = models.CharField(max_length=100, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    station = models.CharField(max_length=30, blank=True)
    station_image_path = models.CharField(max_length=50, blank=True)