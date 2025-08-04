import pytest
pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self,category_factory):
        x = category_factory(name= "test_cat1")
        assert x.__str__() == "test_cat1"

class TestBrandModel:
    def test_str_method(self,brand_factory):
        x = brand_factory(name= "test_brand")
        assert x.__str__() == "test_brand"

class TestProductModel:
    def test_str_method(self,product_factory):
        x = product_factory(name= "test_profuct1")
        assert x.__str__() == "test_profuct1"