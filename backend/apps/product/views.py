from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from .models import SubCategory, Product, Category
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

# Create your views here.
def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

class IndexPage (TemplateView):
    template_name = 'index.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = "products"
    queryset = Product.objects.filter(is_active=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = "product"
