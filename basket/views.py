from django.shortcuts import render

from products.models import Product, Category, Options

# Create your views here.


def basket(request):
    """ A view to show the current basket """

    category = ""
    image = ""
    selected = ""
    options = ""

    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    if request.GET:
        if 'product_options' in request.GET:
            product_options = request.GET['product_options']
            product_options_list = product_options.split(',')
            print(product_options_list)
            category = product_options_list[0]
            product = product_options_list[1]
            selected = product_options_list[2]
            products = products.filter(name=product)
            options = options.filter(name=category)

    context = {
            'products': products,
            'category': category,
            'product': product,
            'selected': selected,
            'options': options,
        }

    return render(request, 'basket/basket.html', context)
