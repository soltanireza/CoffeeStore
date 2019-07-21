from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    products = Product.objects.order_by('-created').filter(available=True)[:3]
    product_prices = Product.objects.order_by('price')
    categories = Category.objects.all()
    # paginator = Paginator(products, 6)
    # page = request.GET.get('page')
    # paged_products = paginator.get_page(page)
    context = {
        "products": products,
        "categories": categories,
        "product_prices": product_prices,
    }
    return render(request, 'shop/index.html', context)


def about(request):
    context = {

    }
    return render(request, 'shop/about.html', context)


def search(request):
    products = Product.objects.order_by('-created')
    categories = Category.objects.all()
    product_prices = Product.objects.order_by('price')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        products = products.filter(description__icontains=keywords)

    if 'name' in request.GET:
        name = request.GET['name']
        products = products.filter(name__icontains=name)

    if 'category' in request.GET:
        category = request.GET['category']
        # products = products.filter(category__iexact=category)
        products = products.filter(category__name__iexact=category)

    if 'price' in request.GET:
        price = request.GET['price']
        products = products.filter(price__lte=price)

    context = {
        'products': products,
        'categories': categories,
        'product_prices': product_prices,
        'values': request.GET
    }
    return render(request, 'shop/product/search.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # paginator = Paginator(products, 6)
    # page = request.GET.get('page')
    # paged_products = paginator.get_page(page)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


