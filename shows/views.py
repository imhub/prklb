from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext as _

from .models import Poster
from .forms import AddShowForm, EditShowForm

from home.models import HomepageInitialSettings, LinksBar

try:
    band = HomepageInitialSettings.objects.all()[0]
except IndexError:
    band = "Enter Band Name in "
links = LinksBar.objects.all()

def showspage(request):
    shows = Poster.objects.filter(show_date__gte=timezone.now()).order_by\
        ('show_date')
    return render(request, 'home/showspage.html', {
        'shows': shows,'band': band, 'links': links})

def shownfo(request, pk):
    show = get_object_or_404(Poster, pk=pk)
    return render(request, 'home/shownfo.html', {
        'show': show, 'band': band, 'links': links})

@login_required
def add_show(request):
    if request.method == "POST":
        form = AddShowForm(request.POST, request.FILES)
        if form.is_valid():
            show = form.save(commit=False)
            show.published_date = timezone.now()
            try:
                show.affiche = request.FILES['affiche']
            except KeyError:
                pass
            show.save()
            messages.success(request, _("You added new show in ")+ show.venue + \
                _(" successfully!"))
            return redirect('shownfo', pk=show.pk)
    else:
        form = AddShowForm()
    return render(request, 'home/show_add.html', {
        'form': form, 'band': band, 'links': links})

@login_required
def edit_show(request, pk):
    show = get_object_or_404(Poster, pk=pk)
    if request.method == "POST":
        form = EditShowForm(request.POST, instance=show)
        if form.is_valid():
            show = form.save(commit=False)
            show.published_date = timezone.now()
            try:
                show.affiche = request.FILES['affiche']
            except KeyError:
                pass
            show.save()
            messages.success(request, _("Changes saved!"))
            return redirect('shownfo', pk=show.pk)
    else:
        form = EditShowForm(instance=show)
    return render(request, 'home/show_edit.html', {
        'form': form, 'band': band, 'links': links})

@login_required
def delete_show(request, pk):
    show = get_object_or_404(Poster, pk=pk)
    show.delete()
    messages.success(request, _("Show in ")+ show.venue + _(" deleted"))
    return redirect('shows')
