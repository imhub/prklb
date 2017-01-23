from django.shortcuts import render


def videospage(request):
    return render(request, 'home/homepage.html', {})
