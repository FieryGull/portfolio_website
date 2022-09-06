from django.shortcuts import render, redirect
from .models import HomeBlock, BiographyBlock, ConferenceBlock, AchievementBlock, PublicationBlock, \
    ProjectBlock, Publication, CourseBlock, CourseVideo, NavContent


def nav(request):
    datanav = NavContent.objects.all()
    return render(request, 'main/layout.html', {'datanav': datanav})


def index(request):
    data = HomeBlock.objects.order_by('date')
    links = NavContent.objects.all()
    datanav = NavContent.objects.all()
    return render(request, 'main/index.html', {'data': data, 'links': links, 'datanav': datanav})


def biography(request):
    data = BiographyBlock.objects.order_by('date')
    datanav = NavContent.objects.all()
    return render(request, 'main/biography.html', {'data': data, 'datanav': datanav})


def projects(request):
    data = ProjectBlock.objects.order_by('date')
    datanav = NavContent.objects.all()
    return render(request, 'main/projects.html', {'data': data, 'datanav': datanav})


def publications(request):
    data = PublicationBlock.objects.order_by('date')
    publication = Publication.objects.order_by('date')
    datanav = NavContent.objects.all()
    return render(request, 'main/publications.html', {'data': data, 'publication': publication, 'datanav': datanav})


def conferences(request):
    data = ConferenceBlock.objects.order_by('date')
    datanav = NavContent.objects.all()
    return render(request, 'main/conferences.html', {'data': data, 'datanav': datanav})


def science_progress(request):
    data = AchievementBlock.objects.order_by('date')
    datanav = NavContent.objects.all()
    return render(request, 'main/science_progress.html', {'data': data, 'datanav': datanav})


def courses(request):
    data = CourseBlock.objects.order_by('date')
    video = CourseVideo.objects.order_by('date')
    datanav = NavContent.objects.all()
    return render(request, 'main/courses_page.html', {'data': data, 'video': video, 'datanav': datanav})
