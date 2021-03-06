from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'smallapp/index.html')

def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Form is Valid')
            print('Name:'+ form.cleaned_data['name'])
            print('Mail:'+ form.cleaned_data['email'])
            print('Text:'+ form.cleaned_data['text'])

    return render(request,'smallapp/forms.html',{'form':form})
