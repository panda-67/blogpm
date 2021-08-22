from django.urls import path
from django.views.generic.dates import ArchiveIndexView, DateDetailView
from . import views
from pmnews.views import *
from pmnews.models import *

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.pencarian, name='pencarian'),
    path('tag/<slug:tag_slug>/',views.tag_list, name='tag_list'),
    path('', ArticleListView.as_view(), name='home'),
    path('arsip/',
         ArchiveIndexView.as_view(queryset=Post.objects.filter(
             status=1), date_field="created_on"),
         name="article_archive"),
    path('<int:year>/<int:month>/',
         ArticleMonthArchiveView.as_view(),
         name="archive_month_numeric"),
    path('<int:year>/<str:month>/<int:day>/',
         ArticleDayArchiveView.as_view(),
         name="archive_day"),
    path('<int:year>/<str:month>/<int:day>/<slug:slug>/',
         DateDetailView.as_view(),
         name="archive_date_detail"),
]
