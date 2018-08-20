from django import forms

from pubg_python import Shard

class SearchPlayerForm(forms.Form):
    shard_tuple = tuple([(s.name, s.value) for s in Shard])
    shard = forms.ChoiceField(choices=shard_tuple)
    player_name = forms.CharField()
