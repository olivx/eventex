from django.shortcuts import render

# Create your views here.

def home(request):
    speackers = [
        {'name': 'Grace Hopper', 'link': 'http://hbn.link/hopper-pic'},
        {'name': 'Allan Turing', 'link': 'http://hbn.link/turing-pic'}
    ]
    return render(request, 'index.html', {'speackers': speackers})
