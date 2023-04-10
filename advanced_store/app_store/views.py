from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView

from app_store.models import Basket, Product, ProductCategory
from common.views import TitleMixin

# Create your views here.

class IndexView(TitleMixin, TemplateView):
    template_name = 'app_store/index.html'
    title = "Phone Stock"


class ProductListView(TitleMixin, ListView):
    model = Product
    template_name = 'app_store/products.html'
    context_object_name = 'products'
    paginate_by = 2
    title = "Каталог"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        # categories = cache.get('categories')
        # if not categories:
        #     categories = ProductCategory.objects.all()
        #     cache.set('categories', categories, 30)
        #
        # context["categories"] = categories
        categories = ProductCategory.objects.all()
        context["categories"] = categories
        return context

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_del(request, id):
    basket = Basket.objects.get(id=id)

    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        Basket.objects.get(id=id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
