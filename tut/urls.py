from django.urls import path
from .views import (
    ArticleList, 
    ArticleDetail, 
    CategoryList, 
    AuthorList,
    ArticlePreview,
    SearchList, 
    tutorials
)

from django.urls import re_path
from . import views

app_name="tut"

urlpatterns = [
     path('', ArticleList.as_view(), name="home"),
     path('page/<int:page>', ArticleList.as_view(), name="home"),
     path('articles/<slug:slug>', ArticleDetail.as_view(), name="details"),
     path('preview/<int:pk>', ArticlePreview.as_view(), name="preview"),
     path('category/<slug:slug>', CategoryList.as_view() , name='category'),
     path('category/<slug:slug>/page/<int:page>', CategoryList.as_view() , name='category'),
     path('author/<slug:username>', AuthorList.as_view() , name='author'),
     path('author/<slug:username>/page/<int:page>', AuthorList.as_view() , name='author'),
     path('search/', SearchList.as_view() , name='search'),
     path('search/page/<int:page>', SearchList.as_view() , name='search'),
     path('tutorials/', tutorials, name="tutorials"),

    ]

# Following's code generate persian urls
# urlpatterns += re_path(r'articles/(?P<slug>[-\W]+)/', views.detail),