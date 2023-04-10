from django.urls import path
from django.views.decorators.cache import cache_page

from app_store.views import ProductListView, basket_add, basket_del


urlpatterns = [
    # path('', cache_page(60 * 1)(ProductListView.as_view()), name='products'),
    path('', ProductListView.as_view(), name='products'),
    path('category/<int:category_id>', ProductListView.as_view(), name='category'),
    # path('page/<int:page>', ProductListView.as_view(), name='paginator'),
    path('basked-add/<int:product_id>', basket_add, name='basket_add'),
    path('basked-del/<int:id>', basket_del, name='basket_del'),
]
