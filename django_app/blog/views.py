from django.shortcuts import render

# Create your views here.
def index(request):
    message = 'ola mundo novamente'
    return render(request, 'blog/pages/index.html',{'content':message})