from django.views import generic
from .models import Product


class IndexView(generic.ListView):
    template_name = 'HomePage/index.html'

    def get_queryset(self):
        return Product.objects.all()


class DetailView(generic.DetailView):
    model = Product
    template_name = 'HomePage/detail.html'
