from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app__name = 'HomePage'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
