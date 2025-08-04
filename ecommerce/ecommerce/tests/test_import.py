import importlib
import pkgutil
import ecommerce.product as product

def test_import_all_modules():
    """Import all modules in product app so coverage sees them."""
    package = product
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        importlib.import_module(module_name)
