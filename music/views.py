from django.shortcuts import render


def musicpage(request):
    return render(request, 'home/homepage.html', {})
