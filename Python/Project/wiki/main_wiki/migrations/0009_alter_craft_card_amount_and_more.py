# Generated by Django 5.1.5 on 2025-05-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_wiki', '0008_craft_card_station_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craft_card',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='craft_card',
            name='ingredients_item_image_path',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='craft_card',
            name='station',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='craft_card',
            name='station_image_path',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='wiki_page',
            name='notes',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
