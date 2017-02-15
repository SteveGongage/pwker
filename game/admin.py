from django.contrib import admin
from game.models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')
    ordering = ['first_name']
admin.site.register(Account, AccountAdmin)

class RealmAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['name']
admin.site.register(Realm, RealmAdmin)

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['name']
admin.site.register(Character, CharacterAdmin)



