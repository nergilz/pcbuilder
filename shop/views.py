from django import shortcuts # render, get_object_or_404, get_list_or_404
from .models import Product

# Create your views here.
def index(request):
    return shortcuts.render(request, 'index.html')

def get_all_products(request):
    products = shortcuts.get_list_or_404(Product)
    # в product помещаем все данные о текущем товаре. в дальнейшем в шаблоне будем вызывать так: product.title
    # где title - название одного из полей товара из созданной нами модели в models.py
    context = {
        'products' : products,
    }
    return shortcuts.render(request, 'catalog.html', context)

def get_contacts(request):
    return shortcuts.render(request, 'contacts.html')

def product_detail(request, id):
    product = shortcuts.get_object_or_404(Product, pk=id)
    # в product помещаем все данные о текущем товаре. в дальнейшем в шаблоне будем вызывать так: product.title
    # где title - название одного из полей товара из созданной нами модели в models.py
    context = {
        'product' : product,
    }
    return shortcuts.render(request, 'single-product.html', context)
