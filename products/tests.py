from django.test import TestCase
from .models import Products
from accounts.models import CustomUser

# Testing the model


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_product = Products.objects.create(
            title="test_products",
            description="Testing products",
            image_link="https://unsplash.com/photos/pA2v_MZHHro",
            user=CustomUser.objects.create_user(
                'john', 'lennon@thebeatles.com', 'johnpassword')
        )
        test_product.save()

    def test_products_model(self):
        product = Products.objects.get(id=1)
        actual_title = product.title
        self.assertEqual(actual_title, "test_products")
