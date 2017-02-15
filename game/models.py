from django.db import models

class Account(models.Model):
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=30)
    name        = models.CharField(max_length=30)
    username    = models.CharField(max_length=50)
    password    = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Realm(models.Model):
     seed = models.IntegerField()
     name = models.CharField(max_length=30)

     def __str__(self):
        return self.name


class Character(models.Model):
    account     = models.ForeignKey(Account, on_delete=models.CASCADE)
    name        = models.CharField(max_length=30)
    origin_realm= models.ForeignKey(Realm, on_delete=None)

    def __str__(self):
        return self.name


class Mana(models.Model):
    origin_realm = models.ForeignKey(Realm, on_delete=None)

    COLOR_RED       = 'red'
    COLOR_BLUE      = 'blue'
    COLOR_PURPLE    = 'purple'
    COLOR_GREEN     = 'green'
    COLOR_YELLOW    = 'yellow'
    COLOR_CHOICES   = (
        (COLOR_RED, 'Red'),
        (COLOR_BLUE, 'Blue'),
        (COLOR_PURPLE, 'Purple'),
        (COLOR_GREEN, 'Green'),
        (COLOR_YELLOW, 'Yellow'),
    )
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)

    def __str__(self):
        return self.color +' '+ self.origin_realm


class Character_Mana(Mana):
    character   = models.ForeignKey(Character, on_delete=models.CASCADE)

    BOND_TAPPED = 'tapped'
    BOND_BOUND  = 'bound'
    BOND_CHOICES= (
        (BOND_TAPPED, 'Tapped'),
        (BOND_BOUND, 'Bound'),
    )
    bond        = models.CharField(max_length=10, choices=BOND_CHOICES)

class Realm_Mana(Mana):
    realm = models.ForeignKey(Realm, on_delete=models.CASCADE)
    position = models.SmallIntegerField()

