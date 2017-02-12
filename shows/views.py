from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Poster
from .forms import AddShowForm


def showspage(request):
    shows = Poster.objects.filter(show_date__gte=timezone.now()).order_by('-show_date')
    return render(request, 'home/showspage.html', {'shows': shows})

def shownfo(request, pk):
    show = get_object_or_404(Poster, pk=pk)
    return render(request, 'home/shownfo.html', {'show': show})

def add_show(request):
    if request.method == "POST":
        form = AddShowForm(request.POST, request.FILES)
        if form.is_valid():
            show = form.save(commit=False)
            show.published_date = timezone.now()
            show.affiche = request.FILES['affiche']
            show.save()
            return redirect('shownfo', pk=show.pk)
    else:
        form = AddShowForm()
    return render(request, 'home/show_edit.html', {'form': form})

def edit_show(request, pk):
    show = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = AddShowForm(request.POST, instance=show)
        if form.is_valid():
            show = form.save(commit=False)
            show.published_date = timezone.now()
            show.affiche = request.FILES['affiche']
            show.save()
            return redirect('shownfo', pk=show.pk)
    else:
        form = AddShowForm(instance=show)
    return render(request, 'home/news_show.html', {'form': form})
