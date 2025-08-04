import factory
from ecommerce.product.models import Brand,Category,Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    # name = "test_category"
    name = factory.sequence(lambda n : "Test_Category_%d" %n)

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    
    name = "test_brand"

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = "test_product"
    description = "test_Product_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)