from django.shortcuts import render

from basket.contexts import basket_context
from products.models import Category, Product

import random

# Create your views here.


def bartholemew(request):
    """ A view to return the bartholemew page """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    menu = Category.objects.all().order_by('id_no')

    context = {
            'cookie_key': cookie_key,
            'basket_total': basket_total,
            'menu': menu,
        }

    return render(request, 'bartholemew/bartholemew.html', context)


def bartholemew_basket(request):
    """ A view to let bartholemew work his magic! """

    if request.POST:
        bartholemew_event_type = request.POST['bartholemew_eventType']
        bartholemew_min_guests = float(request.POST['bartholemew_minGuests'])
        bartholemew_max_guests = float(request.POST['bartholemew_maxGuests'])
        bartholemew_vegan_guests = float(request.POST['bartholemew_veganGuests'])
        bartholemew_veggie_guests = float(request.POST['bartholemew_veggieGuests'])
        bartholemew_pesc_guests = float(request.POST['bartholemew_pescGuests'])
        bartholemew_hotProportion = request.POST['bartholemew_hotProportion']
        bartholemew_allergyProportion = request.POST['bartholemew_allergyProportion']

        """ Calculate the average number of guests """
        bartholemew_ave_guests = int((bartholemew_min_guests +
                                      bartholemew_max_guests) / 2)
        bartholemew_nonspec_guests = int(bartholemew_ave_guests -
                                         bartholemew_vegan_guests -
                                         bartholemew_veggie_guests -
                                         bartholemew_pesc_guests)

        """ Calculate the number of non-allergy meals """
        if bartholemew_allergyProportion == "normal":
            bartholemew_allergyNumber = int(bartholemew_nonspec_guests * 0.2)
        elif bartholemew_allergyProportion == "medium":
            bartholemew_allergyNumber = int(bartholemew_nonspec_guests * 0.3)
        elif bartholemew_allergyProportion == "high":
            bartholemew_allergyNumber = int(bartholemew_nonspec_guests * 0.4)

        """ Calculate the number of hot meals """
        if bartholemew_hotProportion == "No":
            bartholemew_hotNumber = int(bartholemew_nonspec_guests * 0.2)
        elif bartholemew_hotProportion == "Medium amount of":
            bartholemew_hotNumber = int(bartholemew_nonspec_guests * 0.3)
        elif bartholemew_hotProportion == "Lots of":
            bartholemew_hotNumber = int(bartholemew_nonspec_guests * 0.4)

        """ Calculate the total of specified meals """
        bartholemew_specified = int(bartholemew_vegan_guests +
                                    bartholemew_veggie_guests +
                                    bartholemew_pesc_guests +
                                    bartholemew_allergyNumber +
                                    bartholemew_hotNumber)
        bartholemew_unspecified = int(bartholemew_ave_guests -
                                      bartholemew_specified)

        # Choose 10 random records to show
        # Credit: https://stackoverflow.com/questions/32389519/django-get-10-random-instances-from-a-queryset-and-order-them-into-a-new-querys
        
        products_main = Product.objects.get(category__name=categories)

        num_products = Product.objects.all().count()
        print('num_products')
        print(num_products)
        rand_products = random.sample(range(num_products * 6), bartholemew_unspecified * 6)
        print('rand_products')
        print(rand_products)
        unspecified_products = Product.objects.filter(id__in=rand_products)
        print(unspecified_products)
