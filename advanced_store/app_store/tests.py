import os
from http import HTTPStatus

import django
from django.test import TestCase
from django.urls import reverse

os.environ['DJANGO_SETTINGS_MODULE'] = 'advanced_store.settings'

django.setup()
from app_store.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Phone Stock')
        self.assertEqual(response.template_name, ['app_store/index.html'])
        self.assertTemplateUsed(response, 'app_store/base.html')


class ProductsListViewTestCase(TestCase):
    # fixtures = ['category.json', 'product.json']

    def setUp(self):  # общие значения
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products')
        response = self.client.get(path)

        # self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertTemplateUsed(response, 'app_store/products.html')
        # self.assertEqual(response.context_data['title'], 'Каталог')
        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.products[:2]))

    #
    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        # self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertEqual(response.context_data['title'], 'Каталог')
        # self.assertTemplateUsed(response, 'app_store/products.html')
        self._common_tests(response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id)[:2])
        )

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Каталог')
        self.assertTemplateUsed(response, 'app_store/products.html')
