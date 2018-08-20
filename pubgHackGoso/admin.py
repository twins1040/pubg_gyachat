from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Player)
admin.site.register(models.Item)
admin.site.register(models.PlayerItem)
admin.site.register(models.MatchChecked)
