from django.urls import path
from .views import *

urlpatterns = [
    path('', products, name='products'),
    path('<int:category_id>', products, name='category'),
    path('page/<int:page>', products, name='paginator'),
    path('basked-add/<int:product_id>', basket_add, name='basket_add'),
    path('basked-del/<int:id>', basket_del, name='basket_del'),
]