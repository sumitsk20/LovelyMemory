from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app__name = 'HomePage'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^gift/$', views.GiftView.as_view(), name='gift'),
    url(r'^flower/$', views.FlowerView.as_view(), name='flower'),
    url(r'^balloon/$', views.BalloonView.as_view(), name='balloon'),
    url(r'^(?P<pk>[0-9]+)/order$', views.CustomerOrder.as_view(), name='customerOrder'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
