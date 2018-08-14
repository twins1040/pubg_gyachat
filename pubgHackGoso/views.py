from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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

    api = PUBG('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0NmEwOGE2MC03MDc2LTAxMzYtOTNmMS0wNDk5NWRmYzQ5Y2EiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTMyMzMwMjAzLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImJhdHRsZXJhZGFyIn0.AE8Q2-3vwrpWrKlLS43ezcucpZN9Eq0rFG654q6PKmw', shardEnum)

    try:
        players = api.players().filter(player_names=[player_name])
        for player in players:
            player_id = player.id
    except NotFoundError:
        response = "Name error"
        return HttpResponse(response)
    else:
        return HttpResponseRedirect(reverse('pubg_gyachat:closet',args=(player_id,)))


