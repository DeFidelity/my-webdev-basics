from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Game, School

# Create your views here.
def index(request):
    gamers_list = Game.objects.order_by('scores')
    gamers_dict = {'gamers': gamers_list}
    return render(request, 'first_app/index.html',context=gamers_dict)
