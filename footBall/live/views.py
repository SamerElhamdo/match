from django.shortcuts import render, get_object_or_404
from .models import Match, Channel, Lig, Team
import datetime

print(datetime.date)
def match_list(request):
    #date*********************************************************
    yesterday = datetime.date.today() + datetime.timedelta(days=-1)
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)


    #date filter **************************************************
    matchs_yesterday = Match.objects.filter(match_Date=yesterday)
    matchs_today = Match.objects.filter(match_Date=today)
    matchs_tomorrow = Match.objects.filter(match_Date=tomorrow)
    ligs = Lig.objects.all()
    context = {'matchs_yesterday': matchs_yesterday, 'matchs_today': matchs_today, 'matchs_tomorrow': matchs_tomorrow, 'ligs': ligs}
    return render(request, 'live/match/list.html', context)




def match_detail(request, slug):
    match = get_object_or_404(Match, slug=slug)
    return render(request, 'live/match/match-detail.html', {'match': match})

def team_detail(request, slug):
    team = get_object_or_404(Team, slug=slug)
    return render(request, 'live/match/team-detail.html', {'team': team})





# Create your views here.
print(datetime.date)