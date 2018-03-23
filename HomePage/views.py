from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Product
from .forms import Customer


class BalloonView(generic.ListView):
    template_name = 'HomePage/balloons.html'

    def get_queryset(self):
        return Product.objects.all().filter(type_product__exact='BL')


class GiftView(generic.ListView):
    template_name = 'HomePage/gifts.html'

    def get_queryset(self):
        return Product.objects.all().filter(type_product__exact='GF')


class FlowerView(generic.ListView):
    template_name = 'HomePage/flowers.html'

    def get_queryset(self):
        return Product.objects.all().filter(type_product__exact='FW')


class IndexView(generic.ListView):
    template_name = 'HomePage/index.html'
    productList = Product.objects.all()

    def get_queryset(self):
        return self.productList.order_by('modificationTime')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['dataProduct'] = self.dataProduct
        return context


class DetailView(generic.DetailView):
    model = Product
    template_name = 'HomePage/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        # context['pk'] = self.kwargs['name']
        return context


class CustomerOrderView(generic.FormView):
    model = Product
    template_name = 'HomePage/customerDetail.html'

    def get(self, request, **kwargs):
        form = Customer()
        id = self.kwargs.get(id)
        product = Product
        context = {'form': form, 'id': id, 'product': product}
        return render(request, 'HomePage/customerDetail.html', context)

    def post(self, request, **kwargs):
        form = Customer(request.POST or None)
        if form.is_valid():
            form.save()
            print(request.POST)
        context = {'form': form}
        return render(request, 'HomePage/customerDetail.html', context)
