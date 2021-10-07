from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users
from AppTwo.forms import Formdel

# Create your views here.
def home(request):
    return HttpResponse('<h1>Alhamdulilah, i did this</h1>')

def help(request):
    return render(request,'apptwo/index.html')

def users(request):
    user_list = Users.objects.all()
    user_dict= {'our_users': user_list}
    return render(request,'apptwo/users.html',context=user_dict)

def form(request):
    formfields= Formdel()
    if request.method == "POST":

        formfields = Formdel(request.POST)
        if formfields.is_valid():
            formfields = formfields.save()


    return render(request, 'apptwo/forms.html',{'form':formfields})
