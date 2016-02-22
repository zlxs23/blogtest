from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from blog.uploads import upload_image
from blog.views import ArticleListView

urlpatterns = [
    # Examples:
    # url(r'^$', 'blogtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ArticleListView.as_view(), name='blog_index'),
    url(r'^blog/', include('blog.urls')),
    url('', include('django.contrib.auth.urls')),
    url(r"^uploads/(?P<path>.*)$", \
        "django.views.static.serve", \
        {"document_root": settings.MEDIA_ROOT,}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]
