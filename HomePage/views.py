from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Product
from django.views import View
from django.views.generic import TemplateView

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


class CustomerOrder(generic.FormView):
    model = Product
    template_name = 'HomePage/customerDetail.html'

    def get(self, request, **kwargs):
        form = Customer()
        return render(request, 'HomePage/customerDetail.html', {'form': form})

    def post(self, request, **kwargs):
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
            customer_name = form.cleaned_data['customer_name']
            customer_location = form.cleaned_data['customer_location']
        context = {'form': form, 'customer_name': customer_name, 'customer_location': customer_location}
        return render(request, 'HomePage/customerDetail.html', context)

# def customer_detail(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = Customer(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             print(form.cleaned_data)
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             # return HttpResponseRedirect('HomePage/index.html')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = Customer()
