from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'text':'how are you?','number':2000}
    return render(request, 'basic_app/index.html',context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')
