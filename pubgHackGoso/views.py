from django.shortcuts import render
from django.http import HttpResponse

from pubg_python import PUBG, Shard
from pubg_python.exceptions import NotFoundError

# Create your views here.
def index(request):
    return HttpResponse("hello, victims! I will goso hack user")

def searchPlayer(request, shard, playerName):
    shardEnum = ""
    for s in Shard:
        if s.value == shard:
            shardEnum = s

    api = PUBG('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0NmEwOGE2MC03MDc2LTAxMzYtOTNmMS0wNDk5NWRmYzQ5Y2EiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTMyMzMwMjAzLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImJhdHRsZXJhZGFyIn0.AE8Q2-3vwrpWrKlLS43ezcucpZN9Eq0rFG654q6PKmw', shardEnum)

    try:
        players = api.players().filter(player_names=[playerName])
        for player in players:
            player_id = player.id
    except NotFoundError:
        response = "Name error"
    else:
        response = ' '.join([playerName, "'s id is", player_id])

    return HttpResponse(response)

