
from django.urls import path
from science_work import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('', views.nav, name='nav'),
    path('biography', views.biography, name='biography'),
    path('publications', views.publications, name='publications'),
    path('conferences', views.conferences, name='conferences'),
    path('science_progress', views.science_progress, name='science_progress'),
    path('projects', views.projects, name='projects'),
    path('courses', views.courses, name='courses')
]
