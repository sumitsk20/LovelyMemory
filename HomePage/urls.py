from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app__name = 'HomePage'

urlpatterns = [
                  url(r'^$', views.index_view, name='index'),
                  url(r'^gift/$', views.GiftView.as_view(), name='gift'),
                  url(r'^flower/$', views.FlowerView.as_view(), name='flower'),
                  url(r'^balloon/$', views.BalloonView.as_view(), name='balloon'),
                  url(r'^(?P<pk>[0-9]+)/$', views.detail_view, name='detail'),
                  url(r'^(?P<pk>[0-9]+)/order/$', views.customer_order_view, name='product_form'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
