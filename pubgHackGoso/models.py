from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Players(models.Model):
    player_id = models.CharField(max_length=200, primary_key=True)
    player_name = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return self.player_name

class PlayerItem(models.Model):
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    item_id  = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_id

class MatchChecked(models.Model):
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    match_id = models.CharField(max_length=200)

    def __str__(self):
        return self.match_id



