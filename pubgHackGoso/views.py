import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Player, Item, PlayerItem, MatchChecked

from pubg_python import PUBG, Shard
from pubg_python.exceptions import NotFoundError

# Create your views here.
def index(request):
    return HttpResponse("hello! Enter search/pc-kakao/your-nick-name")

def closet(request, player_id):
    return HttpResponse("hello! your id is " + player_id)

def gyachat(request, player_id):
    return HttpResponse("gyachat! your id is " + player_id)

def shoot(request, player_id):
    return HttpResponse("shoot! your id is " + player_id)

def search_player(request, shard, player_name):
    shardEnum = ""
    for s in Shard:
        if s.value == shard:
            shardEnum = s

    with open(os.path.join(os.getcwd(), 'token'), 'r') as f:
            api = PUBG(f.read()[:-1], shardEnum)

    try:
        players = api.players().filter(player_names=[player_name])
        for player in players:
            player_id = player.id
        Player.objects.get(player_id=player_id)
    except NotFoundError:
        response = "Name error"
        return HttpResponse(response)
    except Player.DoesNotExist:
        p = Player(player_id=player_id, player_name=player_name, count=0)
        p.save()
        print('player '+player_name+' is registered')

    return HttpResponseRedirect(reverse('pubg_gyachat:closet',args=(player_id,)))


