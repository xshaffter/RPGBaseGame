from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class CommonModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(CommonModel):
    photo = models.FileField(upload_to='profile_images/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


class Character(CommonModel):
    profile = models.ForeignKey("main.Profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # data
    health_points = models.PositiveIntegerField(default=1)
    max_health = models.PositiveIntegerField(default=1)
    mana_points = models.PositiveIntegerField(default=1)
    max_mana = models.PositiveIntegerField(default=1)
    exp_points = models.PositiveIntegerField(default=1)
    max_exp = models.PositiveIntegerField(default=1)
    level = models.PositiveIntegerField(default=1)

    # stats
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charm = models.IntegerField(default=0)

    # stat points
    sp = models.PositiveIntegerField(default=15)

    character_class = models.ForeignKey("cat.Class", on_delete=models.SET_NULL, null=True, blank=False)
    race = models.ForeignKey("cat.Race", on_delete=models.SET_NULL, null=True, blank=False)
    equipment = models.OneToOneField("main.CharacterEquipment", on_delete=models.CASCADE)


class ItemInventory(CommonModel):
    inventory = models.ForeignKey("main.Inventory", on_delete=models.CASCADE)
    item = models.ForeignKey("cat.Item", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Inventory(CommonModel):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    places = models.PositiveIntegerField(default=1)


class CharacterEquipment(CommonModel):
    left_hand = models.ForeignKey("cat.Weapon", on_delete=models.CASCADE, related_name="eqpmt_left_hand",
                                  null=True, blank=True)
    right_hand = models.ForeignKey("cat.Weapon", on_delete=models.CASCADE, related_name="eqpmt_right_hand",
                                   null=True, blank=True)
    ring = models.ForeignKey("cat.Accessory", on_delete=models.CASCADE, related_name="eqpmt_ring",
                             null=True, blank=True)
    brace = models.ForeignKey("cat.Accessory", on_delete=models.CASCADE, related_name="eqpmt_brace",
                              null=True, blank=True)
    head = models.ForeignKey("cat.Armor", on_delete=models.CASCADE, related_name="eqpmt_head",
                             null=True, blank=True)
    chest = models.ForeignKey("cat.Armor", on_delete=models.CASCADE, related_name="eqpmt_chest",
                              null=True, blank=True)
    bottom = models.ForeignKey("cat.Armor", on_delete=models.CASCADE, related_name="eqpmt_bottom",
                               null=True, blank=True)
    belt = models.ForeignKey("cat.Accessory", on_delete=models.CASCADE, related_name="eqpmt_belt",
                             null=True, blank=True)
    foot = models.ForeignKey("cat.Armor", on_delete=models.CASCADE, related_name="eqpmt_foot",
                             null=True, blank=True)


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()


@receiver(post_save, sender=Character, dispatch_uid='save_new_character')
def save_profile(sender, instance, created, **kwargs):
    character = instance
    if created:
        inventory = Inventory(character=character)
        equipment = CharacterEquipment(character=character)
        equipment.save()
        inventory.save()
