from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.utils.translation import ugettext as _

from .models import Video
from .forms import AddVideoForm, EditVideoForm

from home.models import HomepageInitialSettings, LinksBar

if len(HomepageInitialSettings.objects.all()) != 0:
    band = HomepageInitialSettings.objects.all()[0]
links = LinksBar.objects.all()

def videospage(request):
    videos_list = Video.objects.filter(published_date__lte=timezone.now()).\
        order_by('-published_date')
    videos_by_three = []
    for i in range(len(videos_list)):
        if i % 3 == 0:
            videos_by_three.append([videos_list[i]])
        else:
            videos_by_three[i // 3].append(videos_list[i])
    paginator = Paginator(videos_by_three, 3)
    page = request.GET.get('page')
    try:
        videos_by_three = paginator.page(page)
    except PageNotAnInteger:
        videos_by_three = paginator.page(1)
    except EmptyPage:
        videos_by_three = paginator.page(paginator.num_pages)
    return render(
                request,
                'home/videospage.html',
                {
                    'videos_by_three': videos_by_three,
                    'band': band,
                    'links': links,
                }
                )

def viewvideo(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'home/viewvideo.html', {
        'video': video, 'band': band, 'links': links})

@login_required
def add_video(request):
    if request.method == "POST":
        form = AddVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.published_date = timezone.now()
            video.save()
            messages.success(request, _("You added new video ") + \
                video.title + _(" successfully!"))
            return redirect('viewvideo', pk=video.pk)
    else:
        form = AddVideoForm()
    return render(request, 'home/video_add.html', {
        'form': form, 'band': band, 'links': links})

@login_required
def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = EditVideoForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save()
            video.published_date = timezone.now()
            video.save()
            messages.success(request, _("Changes saved!"))
            return redirect('viewvideo', pk=video.pk)
    else:
        form = EditVideoForm(instance=video)
    return render(request, 'home/video_edit.html', {
        'form': form, 'band': band, 'links': links})

@login_required
def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.delete()
    messages.success(request, _("Video ")+ video.title + _(" deleted"))
    return redirect('videos')
