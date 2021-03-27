from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .models import Product, Category, Options
from basket.contexts import basket_context
from .forms import ProductAdminForm, OptionsAdminForm, CategoryAdminForm

# Create your views here.


def products(request):
    """ A view to show and filter products """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    category = ""
    range = ""
    image = ""

    categories = Category.objects.all()
    products = Product.objects.all()

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            range = "standard"
            image = categories.filter(name=category)
        if 'category_range' in request.GET:
            category_range = request.GET['category_range']
            category_range_list = category_range.split(',')
            category = category_range_list[0]
            range = category_range_list[1]
            image = categories.filter(name=category)

    context = {
            'products': products,
            'category': category,
            'range': range,
            'image': image,
            'cookie_key': cookie_key,
            'basket_total': basket_total
        }

    return render(request, 'products/products.html', context)


def product_detail(request):
    """ A view to show product options """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    category = ""
    products = ""
    selected = ""
    image = ""
    options = ""
    item_number = ""

    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    if request.GET:
        if 'category_product' in request.GET:
            category_product = request.GET['category_product']
            category_product_list = category_product.split(',')
            category = category_product_list[0]
            product = category_product_list[1]
            selected = category_product_list[2]
            products = products.filter(name=product)
            image = categories.filter(name=category)
            options = options.filter(category__in=categories)
            context = {
                    'products': products,
                    'category': category,
                    'product': product,
                    'selected': selected,
                    'image': image,
                    'options': options,
                    'cookie_key': cookie_key,
                    'basket_total': basket_total,
                }

            return render(request, 'products/product_detail.html', context)

        if 'product_edit' in request.GET:
            product_edit = request.GET['product_edit']
            product_edit_list = product_edit.split(',')
            category = product_edit_list[0]
            product = product_edit_list[1]
            selected = product_edit_list[2]
            item_number = product_edit_list[3]
            servings = product_edit_list[4]
            total_price = product_edit_list[5]
            servings_plusten = float(servings) + 10
            products = products.filter(name=product)
            image = categories.filter(name=category)
            options = options.filter(category__in=categories)

            context = {
                    'products': products,
                    'category': category,
                    'product': product,
                    'selected': selected,
                    'image': image,
                    'options': options,
                    'servings': servings,
                    'total_price': total_price,
                    'item_number': item_number,
                    'servings_plusten': servings_plusten,
                    'cookie_key': cookie_key,
                    'basket_total': basket_total,
                }

            return render(request, 'products/edit_product.html', context)
    return render(request, 'products/product_detail.html', context)


@login_required
def product_admin(request):
    """ A view to manage products, categories and options """

    """ reset all variables to handle errors """
    form = ""
    dataset = ""
    query = ""
    return_query_length = ""
    return_query_number = 1

    """ get information from form and/or request """
    if request.GET:
        """ get information from request """
        if 'dataset' in request.GET:
            dataset = request.GET['dataset']
            """ determine dataset to return """
            if dataset == 'products':
                return_query = Product.objects.all().first()
                return_query_length = Product.objects.all().count()
                form = ProductAdminForm(instance=return_query)
            elif dataset == 'options':
                return_query = Options.objects.all().first()
                return_query_length = Options.objects.all().count()
                form = OptionsAdminForm(instance=return_query)
            elif dataset == 'categories':
                return_query = Category.objects.all().first()
                return_query_length = Category.objects.all().count()
                form = CategoryAdminForm(instance=return_query)

        """ get information from search form """
        if 'product_search_admin' in request.GET:
            query = request.GET['product_search_admin']
            if not query:
                """ default to products in case of blank query """
                return_query = Product.objects.all().first()
                dataset = 'products'
                form = ProductAdminForm(instance=return_query)
                context = {
                        'form': form,
                        'dataset': dataset,
                        'return_query_number': return_query_number,
                        'return_query_length': return_query_length
                    }
                return render(request, 'products/product_admin.html', context)

            """ get information from request """
            if 'dataset' in request.GET:
                dataset = request.GET['dataset']
                return_query_number = 1

                """ determine dataset to return """
                if dataset == 'products':
                    queries = Q(name__icontains=query) | Q(description__icontains=query)
                    products = Product.objects.all()
                    return_query = products.filter(queries).first()
                    return_query_length = products.filter(queries).count()
                    form = ProductAdminForm(instance=return_query)
                elif dataset == 'options':
                    queries = Q(category__name__icontains=query) | Q(option2__icontains=query) | Q(option3__icontains=query)
                    options = Options.objects.all()
                    return_query = options.filter(queries).first()
                    return_query_length = options.filter(queries).count()
                    form = OptionsAdminForm(instance=return_query)
                elif dataset == 'categories':
                    queries = Q(name__icontains=query) | Q(friendly_name__icontains=query)
                    categories = Category.objects.all()
                    return_query = categories.filter(queries).first()
                    return_query_length = categories.filter(queries).count()
                    form = CategoryAdminForm(instance=return_query)

    else:
        """ default to products in case of error """
        return_query = Product.objects.all().first()
        form = ProductAdminForm(instance=return_query)

    context = {
            'form': form,
            'dataset': dataset,
            'query': query,
            'return_query_length': return_query_length,
            'return_query_number': return_query_number,
        }

    return render(request, 'products/product_admin.html', context)


@login_required
def update_product(request, form_id):
    """ update a product on the menu """
    if not request.user.is_superuser:
        messages.success(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = ""
    option = ""
    category = ""

    if request.method == 'POST':
        if form_id[0:3] == 'pro':
            product = get_object_or_404(Product, id_no=form_id)
            form = ProductAdminForm(request.POST, request.FILES, instance=product)
            item = 'product'
        if form_id[0:3] == 'opt':
            option = get_object_or_404(Options, id_no=form_id)
            form = OptionsAdminForm(request.POST, request.FILES, instance=option)
            item = 'option'
        if form_id[0:3] == 'cat':
            category = get_object_or_404(Category, id_no=form_id)
            form = CategoryAdminForm(request.POST, request.FILES, instance=category)
            item = 'category'
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {item}')
            return redirect(reverse('refresh_product_admin', args=[form_id]))
        else:
            messages.success(request, 'Failed to update product. Please ensure the form is valid.')
            return redirect(reverse('refresh_product_admin', args=[form_id]))
    else:
        form = ProductAdminForm(instance=product)
        messages.success(request, f'You are editing {product.name}')

    context = {
        'form': form,

    }

    return render(request, 'home/index.html', context)


@login_required
def add_product(request):
    """ update a product on the menu """
    if not request.user.is_superuser:
        messages.success(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    categories = Category.objects.all()

    dataset = ""

    if request.method == 'GET':
        """ get the dataset to decide to add: product, option or category """
        if 'dataset' in request.GET:
            dataset = request.GET['dataset']

    if request.method == 'POST':
        dataset = request.POST['dataset']

        if dataset == 'products':
            """ get the last product.id_no and incriment by 1 """
            last_product = Product.objects.all().last()
            last_product_id = int(float(last_product.id_no[3:6]))
            next_product_id = last_product_id + 1
            if next_product_id < 10:
                next_product_id = "pro" + "00" + str(next_product_id)
            elif next_product_id < 100:
                next_product_id = "pro" + "0" + str(next_product_id)
            else:
                next_product_id = "pro" + str(next_product_id)

            category = Category.objects.get(name=request.POST['new_category'])
            name = request.POST['new_name']
            description = request.POST['new_description']
            price = request.POST['new_price']
            range = request.POST['new_range']
            new_product = Product(category=category,
                                  id_no=next_product_id,
                                  name=name,
                                  description=description,
                                  price=price,
                                  range=range)
            new_product.save()
            messages.success(request, f'Succesfully added {new_product.name}')
            return redirect(reverse('refresh_product_admin', args=[next_product_id]))

        if dataset == 'categories':
            """ get the last product.id_no and incriment by 1 """
            last_category = Category.objects.all().last()
            last_category_id = int(float(last_category.id_no[3:6]))
            next_category_id = last_category_id + 1
            if next_category_id < 10:
                next_category_id = "cat" + "00" + str(next_category_id)
            elif next_category_id < 100:
                next_category_id = "cat" + "0" + str(next_category_id)
            else:
                next_category_id = "cat" + str(next_category_id)

            name = request.POST['new_category_name']
            friendly_name = request.POST['new_friendly_name']
            new_category = Category(name=name,
                                    id_no=next_category_id,
                                    friendly_name=friendly_name)
            new_category.save()
            messages.success(request, f'Succesfully added {new_category.name}')
            return redirect(reverse('refresh_product_admin', args=[next_category_id]))

        if dataset == 'options':
            """ get the last option.id_no and incriment by 1 """
            last_option = Options.objects.all().last()
            last_option_id = int(float(last_option.id_no[3:6]))
            next_option_id = last_option_id + 1
            if next_option_id < 10:
                next_option_id = "opt" + "00" + str(next_option_id)
            elif next_option_id < 100:
                next_option_id = "opt" + "0" + str(next_option_id)
            else:
                next_option_id = "opt" + str(next_option_id)

            category = Category.objects.get(name=request.POST['new_option_category'])
            option1 = request.POST['new_option_one']
            option2 = request.POST['new_option_two']
            option3 = request.POST['new_option_three']
            new_option = Options(category=category,
                                 id_no=next_option_id,
                                 option1=option1,
                                 option2=option2,
                                 option3=option3)
            new_option.save()
            messages.success(request, f'Succesfully added {new_option.name}')
            return redirect(reverse('refresh_product_admin', args=[next_option_id]))

    context = {
        'categories': categories,
        'dataset': dataset,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def delete_product(request, form_id):
    """ update a product on the menu """
    if not request.user.is_superuser:
        messages.success(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    form = ""
    dataset = ""
    return_query_length = ""
    return_query_number = ""

    if form_id[0:3] == 'pro':
        product = Product.objects.get(id_no=form_id)
        product.delete()
        return_query = Product.objects.all().last()
        return_query_length = Product.objects.all().count()
        return_query_number = return_query_length
        form = ProductAdminForm(instance=return_query)
        dataset = "products"
        messages.success(request, f'You have deleted {product}')
    if form_id[0:3] == 'opt':
        option = Options.objects.get(id_no=form_id)
        option.delete()
        return_query = Options.objects.all().last()
        return_query_length = Options.objects.all().count()
        return_query_number = return_query_length
        form = OptionsAdminForm(instance=return_query)
        dataset = "options"
        messages.success(request, f'You have deleted {option}')
    if form_id[0:3] == 'cat':
        category = Category.objects.get(id_no=form_id)
        category.delete()
        return_query = Category.objects.all().last()
        return_query_length = Category.objects.all().count()
        return_query_number = return_query_length
        form = CategoryAdminForm(instance=return_query)
        dataset = "categories"
        messages.success(request, f'You have deleted {category}')

    context = {
            'form': form,
            'dataset': dataset,
            'return_query_length': return_query_length,
            'return_query_number': return_query_number,
        }

    return render(request, 'products/product_admin.html', context)


@login_required
def refresh_product_admin(request, form_id):

    """ reset all variables to handle errors """
    form = ""
    dataset = ""
    return_query_length = 1
    return_query_number = 1

    """ determine dataset to return """
    if form_id[0:3] == "pro":
        query = get_object_or_404(Product, id_no=form_id)
        return_query_length = Product.objects.all().count()
        # Credit: https://www.c-sharpcorner.com/article/how-to-get-the-last-n-characters-of-a-string-in-python/
        return_query_number = int(form_id[-3::] * 1)
        form = ProductAdminForm(instance=query)
        dataset = 'products'
    elif form_id[0:3] == "opt":
        query = get_object_or_404(Options, id_no=form_id)
        return_query_length = Options.objects.all().count()
        return_query_number = int(form_id[-3::] * 1)
        form = OptionsAdminForm(instance=query)
        dataset = 'options'
    elif form_id[0:3] == "cat":
        query = get_object_or_404(Category, id_no=form_id)
        return_query_length = Category.objects.all().count()
        return_query_number = int(form_id[-3::] * 1)
        form = CategoryAdminForm(instance=query)
        dataset = 'categories'

    else:
        """ default to home in case of error """
        return render(request, 'home/index.html')

    context = {
            'form': form,
            'form_id': form_id,
            'dataset': dataset,
            'return_query_length': return_query_length,
            'return_query_number': return_query_number,
        }

    return render(request, 'products/product_admin.html', context)


@login_required
def next_product(request):

    """ reset all variables to handle errors """
    form = ""
    query = ""

    """ get information from request """
    if request.GET:
        if 'this_product' in request.GET:
            this_product = request.GET['this_product']
            this_product_list = this_product.split(',')
            dataset = this_product_list[0]
            return_query_number = int(this_product_list[1]) + 1
            return_query_length = int(this_product_list[2])
            query = this_product_list[3]
            """ determine dataset to return """
            if dataset == 'products':
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = Product.objects.all()
                return_query = products.filter(queries)[return_query_number - 1]
                form = ProductAdminForm(instance=return_query)
            elif dataset == 'options':
                queries = Q(category__name__icontains=query) | Q(option2__icontains=query) | Q(option3__icontains=query)
                products = Options.objects.all()
                return_query = products.filter(queries)[return_query_number - 1]
                form = OptionsAdminForm(instance=return_query)
            elif dataset == 'categories':
                queries = Q(name__icontains=query) | Q(friendly_name__icontains=query)
                products = Category.objects.all()
                return_query = products.filter(queries)[return_query_number - 1]
                form = CategoryAdminForm(instance=return_query)

    else:
        """ default to home in case of error """
        return render(request, 'home/index.html')

    context = {
            'form': form,
            'dataset': dataset,
            'query': query,
            'return_query': return_query,
            'return_query_number': return_query_number,
            'return_query_length': return_query_length,
        }

    return render(request, 'products/product_admin.html', context)


@login_required
def prev_product(request):

    """ reset all variables to handle errors """
    form = ""
    query = ""

    """ get information from request """
    if request.GET:
        if 'this_product' in request.GET:
            this_product = request.GET['this_product']
            this_product_list = this_product.split(',')
            dataset = this_product_list[0]
            return_query_number = int(this_product_list[1]) - 1
            return_query_length = this_product_list[2]
            query = this_product_list[3]
            """ determine dataset to return """
            if dataset == 'products':
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = Product.objects.all()
                return_query = products.filter(queries)[return_query_number - 1]
                form = ProductAdminForm(instance=return_query)
            elif dataset == 'options':
                queries = Q(category__name__icontains=query) | Q(option2__icontains=query) | Q(option3__icontains=query)
                products = Options.objects.all()
                return_query = products.filter(queries)[return_query_number - 1]
                form = OptionsAdminForm(instance=return_query)
            elif dataset == 'categories':
                queries = Q(name__icontains=query) | Q(friendly_name__icontains=query)
                products = Category.objects.all()
                return_query = products.filter(queries)[return_query_number - 1]
                form = CategoryAdminForm(instance=return_query)

    else:
        """ default to home in case of error """
        return render(request, 'home/index.html')

    context = {
            'form': form,
            'dataset': dataset,
            'query': query,
            'return_query_number': return_query_number,
            'return_query_length': return_query_length,
        }

    return render(request, 'products/product_admin.html', context)


def search_products(request):
    """ A view to search all products """

    """ reset all variables to handle errors """
    query = ""

    """ get information from form and/or request """
    if request.GET:

        """ get information from search form """
        if 'product_search' in request.GET:
            query = request.GET['product_search']
            if not query:
                """ default to all products in case of blank query """
                product_results = Product.objects.all()

                context = {
                        'product_results': product_results,
                    }
                return render(request, 'products/search_products.html', context)

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
            products = Product.objects.all()
            product_results = products.filter(queries)

    else:
        """ default to products in case of error """
        product_results = products.filter(queries).first()

    context = {
            'product_results': product_results,
        }

    return render(request, 'products/search_products.html', context)
