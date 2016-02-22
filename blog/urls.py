from django.conf.urls import url

from blog.views import *

urlpatterns = [
    url(r'^article/(?P<title>\S+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^$', ArticleListView.as_view(), name='blog_index'),
]