from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.dates import MonthArchiveView, DayArchiveView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Q
from pmnews.models import Post
from taggit.models import Tag
from hitcount.views import HitCountDetailView
# Create your views here.
now = timezone.now()

# def index(request):
#     posts = Post.objects.all().filter(status=1)
#     paginator = Paginator(posts, 7)
#     page_number = request.GET.get('page')
#     post_page = paginator.get_page(page_number)
#     context = {'page_title': "Perahu Media", 'pos_page': post_page}
#     return render(request, "pmnews/home.html", context)


def about(request):
    context = {'page_title': "PM | About", }
    return render(request, "pmnews/about.html", context)


def contact(request):
    context = {'page_title': "PM | Contact", }
    return render(request, "pmnews/contact.html", context)


def pencarian(request):
    if request.method == "POST":
        cari = request.POST.get('cari')
        posts = Post.objects.filter(status=1).filter(created_on__lte=now).filter(
            Q(title__icontains=cari) | Q(content__icontains=cari))
        context = {'cari': cari, 'post': posts, 'page_title': "PM | Cari", }
        return render(request, "pmnews/pencarian.html", context)
    else:
        return render(request, "pmnews/pencarian.html")


def tag_list(request, tag_slug=None):   
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])   
    return render(request,'pmnews/tag_list.html',{'posts':posts, 'tag':tag})

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.filter(status=1).filter(created_on__lte=now)
    date_field = "created_on"
    allow_future = True
    month_format = '%m'


class ArticleDayArchiveView(DayArchiveView):
    queryset = Post.objects.filter(status=1).filter(created_on__lte=now)
    date_field = "created_on"
    allow_future = True
    month_format = '%m'


class DateDetailView(HitCountDetailView, DetailView):
    queryset = Post.objects.filter(status=1).filter(created_on__lte=now)
    date_field = "created_on",
    allow_future = True
    month_format = '%m'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(DateDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.filter(status=1).filter(created_on__lte=now).order_by('-hit_count_generic__hits')[:3],
        })
        return context

class ArticleListView(ListView):
    queryset = Post.objects.filter(status=1).filter(created_on__lte=now)
    paginate_by = 3

    

    # def get(self, request):
    #     posts = Post.objects.all().filter(status=1)
    #     context = {'post': posts}
    #     return render(request, "pmnews/post_list.html", context)
