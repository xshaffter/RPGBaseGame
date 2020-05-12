from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from cat.models import Accessory, Armor, Weapon, Item, Class, Race
from main.models import Profile, Character, CharacterEquipment, Inventory, ItemInventory

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    inlines = [UserProfileInline]


admin.site.register([Character, Item, Weapon, Armor, Accessory, ItemInventory, Inventory, CharacterEquipment, Race, Class])
