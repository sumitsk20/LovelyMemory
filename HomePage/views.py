from django.shortcuts import render, get_object_or_404
from django.views import generic
from HomePage.models import Product
from HomePage.forms import Customer
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def index_view(request):
    product_list = Product.objects.all().order_by('modificationTime')
    paginator = Paginator(product_list, 8)  # Show N contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    product = paginator.get_page(page)

    context = {'product_list': product, 'page_request_var': page_request_var}
    return render(request, 'HomePage/index.html', context)


def detail_view(request, pk):
    instance = get_object_or_404(Product, id=pk)
    session_value = request.session['product'] = instance.id
    print(session_value)
    context = {'instance': instance}
    return render(request, 'HomePage/detail.html', context)


def customer_order_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = Customer(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.customer_product_name = product
        instance.save()
        messages.success(request, "Success \n we will contact you soon")
    context = {'form': form, 'product': product}
    return render(request, 'HomePage/customerDetail.html', context)


class CustomerOrderView(generic.FormView):
    model = Product
    template_name = 'HomePage/customerDetail.html'

    def get(self, request, **kwargs):
        form = Customer()
        context = {'form': form}
        return render(request, 'HomePage/customerDetail.html', context)

    def post(self, request, **kwargs):
        form = Customer(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Success \n we will contact you soon")
        context = {'form': form}
        return render(request, 'HomePage/customerDetail.html', context)
