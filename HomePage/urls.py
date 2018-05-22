from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from HomePage.views import index_view, GiftView, FlowerView, BalloonView, detail_view, customer_order_view

app__name = 'HomePage'

urlpatterns = [
                  url(r'^$', index_view, name='index'),
                  url(r'^gift/$', GiftView.as_view(), name='gift'),
                  url(r'^flower/$', FlowerView.as_view(), name='flower'),
                  url(r'^balloon/$', BalloonView.as_view(), name='balloon'),
                  url(r'^(?P<pk>[0-9]+)/$', detail_view, name='detail'),
                  url(r'^(?P<pk>[0-9]+)/order/$', customer_order_view, name='product_form'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
