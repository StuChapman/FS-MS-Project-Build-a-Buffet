from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from basket.contexts import basket_context
from products.models import Product, Category
from basket.models import Basket

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

    """ check for a basket cookie """
    context_items = basket_context(request)
    cookie = context_items['cookie']

    option = 1
    menu = Category.objects.all().order_by('id_no')

    if request.POST:
        bartholemew_event_type = request.POST['bartholemew_eventType']
        bartholemew_min_guests = int(request.POST['bartholemew_minGuests'])
        bartholemew_max_guests = int(request.POST['bartholemew_maxGuests'])
        bartholemew_vegan_guests = int(request.POST['bartholemew_veganGuests'])
        bartholemew_veggie_guests = int(request.POST['bartholemew_veggieGuests'])
        bartholemew_pesc_guests = int(request.POST['bartholemew_pescGuests'])
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

        # Credit: https://stackoverflow.com/questions/32389519/django-get-10-random-instances-from-a-queryset-and-order-them-into-a-new-querys

        """ Generate 3 random main courses for unspecified guests """
        products_main = [i.id for i in Product.objects.filter(category__course="main")]
        random.shuffle(products_main)
        products_main_shuffled = [Product.objects.get(id=i) for i in products_main]
        products_main_unspecified = products_main_shuffled[0:bartholemew_unspecified * 3]

        """ Generate 3 random main courses for vegan guests """
        products_main_vegan = [i.id for i in Product.objects.filter(category__course="main",
                                                                    allergies__startswith="1")]
        random.shuffle(products_main_vegan)
        products_main_vegan_shuffled = [Product.objects.get(id=i) for i in products_main_vegan]
        products_main_vegan = products_main_vegan_shuffled[0:bartholemew_vegan_guests * 3]

        """ Generate 3 random main courses for hot food """
        products_hot_food = [i.id for i in Product.objects.filter(category__course="main",
                                                                    allergies__endswith="1")]
        random.shuffle(products_hot_food)
        products_hot_food_shuffled = [Product.objects.get(id=i) for i in products_hot_food]
        products_hot_food = products_hot_food_shuffled[0:bartholemew_hotNumber * 3]

        """ Generate 2 random side courses for unspecified guests """
        products_side = [i.id for i in Product.objects.filter(category__course="side")]
        random.shuffle(products_side)
        products_side_shuffled = [Product.objects.get(id=i) for i in products_side]
        products_side_unspecified = products_side_shuffled[0:bartholemew_unspecified * 2]

        """ Generate 2 random side courses for vegan guests """
        products_side_vegan = [i.id for i in Product.objects.filter(category__course="side",
                                                                    allergies__startswith="1")]
        random.shuffle(products_side_vegan)
        products_side_vegan_shuffled = [Product.objects.get(id=i) for i in products_side_vegan]
        products_side_vegan = products_side_vegan_shuffled[0:bartholemew_vegan_guests * 2]

        """ Generate 1 random dessert course for unspecified guests """
        products_dessert = [i.id for i in Product.objects.filter(category__course="dessert")]
        random.shuffle(products_dessert)
        products_dessert_shuffled = [Product.objects.get(id=i) for i in products_dessert]
        products_dessert_unspecified = products_dessert_shuffled[0:bartholemew_unspecified * 1]

        """ Generate 1 random dessert courses for vegan guests """
        products_dessert_vegan = [i.id for i in Product.objects.filter(category__course="dessert",
                                                                    allergies__startswith="1")]
        random.shuffle(products_dessert_vegan)
        products_dessert_vegan_shuffled = [Product.objects.get(id=i) for i in products_dessert_vegan]
        products_dessert_vegan = products_dessert_vegan_shuffled[0:bartholemew_vegan_guests * 2]

        products_list_unspecified = (products_main_unspecified +
                                     products_side_unspecified +
                                     products_dessert_unspecified)
        products_list_vegan = (products_main_vegan +
                               products_side_vegan +
                               products_dessert_vegan)
        products_list_full = (products_list_unspecified +
                              products_list_vegan +
                              products_hot_food)

        for product in products_list_full:
            category = product.category
            name = product.name
            price = product.price
            servings = 1

            """ Randomise the available option """
            rnd = random.randint(1, 3)
            if rnd == 1:
                option = "selected-one"
            elif rnd == 2:
                option = "selected-two"
            elif rnd == 3:
                option = "selected-three"

            """ check for existing basket(s) with the current cookie value """
            try:
                existing_basket = Basket.objects.get(cookie=cookie,
                                                     category=category,
                                                     name=product,
                                                     option=option)
                existing_servings = existing_basket.servings

                """ add the new servings variable to the existing """
                updated_servings = existing_servings + int(servings)

                total_price = float(price) * float(updated_servings)

                """ save the updated basket and delete the existing """
                updated_basket = Basket(cookie=cookie,
                                        category=category,
                                        name=name,
                                        servings=updated_servings,
                                        option=option,
                                        total_price=total_price)
                updated_basket.save()
                existing_basket.delete()
            except ObjectDoesNotExist:

                """ if there is no existing basket, create a new one """
            total_price = float(price) * float(servings)

            basket = Basket(cookie=cookie,
                            category=category,
                            name=name,
                            servings=servings,
                            option=option,
                            total_price=total_price)
            basket.save()

    context = {
            'bartholemew_event_type': bartholemew_event_type,
            'products_list_full': products_list_full,
            'menu': menu,
        }

    return render(request, 'bartholemew/bartholemew_output.html', context)
