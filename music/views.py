from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.utils.translation import ugettext as _

from .models import Album
from .forms import AddAlbumForm, EditAlbumForm

from home.models import HomepageInitialSettings, LinksBar

if len(HomepageInitialSettings.objects.all()) != 0:
    band = HomepageInitialSettings.objects.all()[0]
links = LinksBar.objects.all()

def musicpage(request):
    albums = Album.objects.filter(release_date__lte=timezone.now()).order_by(
        '-release_date')
    paginator = Paginator(albums, 5)
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)
    return render(request, 'home/musicpage.html', {
        'albums': albums, 'band': band, 'links': links})

def viewalbum(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'home/viewalbum.html', {
        'album': album, 'band': band, 'links': links})

@login_required
def add_album(request):
    if request.method == "POST":
        form = AddAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.published_date = timezone.now()
            try:
                album.cover = request.FILES['cover']
            except KeyError:
                pass
            album.save()
            messages.success(request, _("You added new album ") + \
                album.title + _(" successfully!"))
            return redirect('viewalbum', pk=album.pk)
    else:
        form = AddAlbumForm()
    return render(request, 'home/album_add.html', {
        'form': form, 'band': band, 'links': links})

@login_required
def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            album.published_date = timezone.now()
            try:
                album.cover = request.FILES['cover']
            except KeyError:
                pass
            album.save()
            messages.success(request, _("Changes saved!"))
            return redirect('viewalbum', pk=album.pk)
    else:
        form = EditAlbumForm(instance=album)
    return render(request, 'home/album_edit.html', {
        'form': form, 'band': band, 'links': links})

@login_required
def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    messages.success(request, _("Album ")+ album.title + _(" deleted"))
    return redirect('music')
