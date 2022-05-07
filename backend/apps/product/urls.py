from django.urls import path
from .views import *
urlpatterns = [
      path('getSubcategory/', get_subcategory, name = 'get_subcategory'),
      path('', IndexPage.as_view(), name='index'),
      path('list/product/', ProductListView.as_view(), name='product_list'),
      path('detail/product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
    ]