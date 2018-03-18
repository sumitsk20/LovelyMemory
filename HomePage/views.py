from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.template import Context
from django.template import RequestContext
from .models import Product, CustomerOrderModel
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
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


class CustomerOrderView(generic.FormView):
    model = Product
    template_name = 'HomePage/customerDetail.html'

    def get(self, request, **kwargs):
        form = Customer()
        return render(request, 'HomePage/customerDetail.html', {'form': form})

    def post(self, request, **kwargs):
        form = Customer(request.POST or None)
        if form.is_valid():
            form.save()
            print(request.POST)
        context = {'form': form}
        return render(request, 'HomePage/customerDetail.html', context)
