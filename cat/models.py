from django.db import models

# Create your models here.
from main.models import CommonModel


class Class(CommonModel):
    name = models.CharField(max_length=50)
    initiative = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)


class Race(CommonModel):
    name = models.CharField(max_length=50)
    initiative = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)


class Weapon(CommonModel):
    item = models.ForeignKey("cat.Item", on_delete=models.CASCADE)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)


class Armor(CommonModel):
    item = models.ForeignKey("cat.Item", on_delete=models.CASCADE)
    defense = models.IntegerField(default=0)


class Accessory(CommonModel):
    item = models.ForeignKey("cat.Item", on_delete=models.CASCADE)
    attack = models.IntegerField(default=1)


class Item(CommonModel):
    image = models.FileField(upload_to='items/')
    name = models.CharField(max_length=20)
    max_quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)
