from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from basket.contexts import basket_context
from products.models import Product, Category, Options
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
        bartholemew_min_guests = int(float(
                                     request.POST['bartholemew_minGuests']))
        bartholemew_max_guests = int(float(
                                     request.POST['bartholemew_maxGuests']))
        bartholemew_vegan_guests = int(float(
                                       request.POST['bartholemew_veganGuests']))
        bartholemew_veggie_guests = int(float(
                                        request.POST['bartholemew_veggieGuests']))
        bartholemew_pesc_guests = int(float(
                                      request.POST['bartholemew_pescGuests']))
        bartholemew_hotProportion = request.POST['bartholemew_hotProportion']
        bartholemew_allergyProportion = request.POST['bartholemew_allergyProportion']

        """ Calculate the average number of guests """
        if bartholemew_max_guests == "":
            bartholemew_ave_guests = bartholemew_min_guests
        else:
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

        # Credit: https://stackoverflow.com/questions/32389519/
        # django-get-10-random-instances-from-a-queryset-and-
        # order-them-into-a-new-querys

        """ MAIN COURSES """

        """ Generate 3 random main courses for each unspecified guest """
        products_main = [i.id for i in Product.objects.filter(
                                        category__course="main")]
        products_main_unspecified = []
        for i in range(bartholemew_unspecified):
            random.shuffle(products_main)
            products_main_shuffled = ([Product.objects.get(id=i)
                                       for i in products_main])
            products_main_unspecified = (products_main_unspecified +
                                         products_main_shuffled[0: 3])

        """ Generate 3 random main courses for each vegan guest """
        products_main = ([i.id for i in
                          Product.objects.filter(category__course="main",
                                                 allergies__contains="v")])
        products_main_vegan = []
        for i in range(bartholemew_vegan_guests):
            random.shuffle(products_main)
            products_main_shuffled = ([Product.objects.get(id=i)
                                      for i in products_main])
            products_main_vegan = (products_main_vegan +
                                   products_main_shuffled[0: 3])

        """ Generate 3 random main courses for each vegetarian guest """
        products_main = ([i.id for i in
                          Product.objects.filter(category__course="main",
                                                 allergies__contains="g")])
        products_main_veggie = []
        for i in range(bartholemew_veggie_guests):
            random.shuffle(products_main)
            products_main_shuffled = ([Product.objects.get(id=i)
                                       for i in products_main])
            products_main_veggie = (products_main_veggie +
                                    products_main_shuffled[0: 3])

        """ Generate 3 random main courses for each pescatarian guest """
        products_main = ([i.id for i in
                          Product.objects.filter(category__course="main",
                                                 allergies__contains="p")])
        products_main_pesc = []
        for i in range(bartholemew_pesc_guests):
            random.shuffle(products_main)
            products_main_shuffled = ([Product.objects.get(id=i)
                                       for i in products_main])
            products_main_pesc = (products_main_pesc +
                                  products_main_shuffled[0: 3])

        """ Generate 3 random main courses for hot food proportion """
        products_main = ([i.id for i in
                          Product.objects.filter(category__course="main",
                                                 allergies__contains="h")])
        products_hot_food = []
        for i in range(bartholemew_hotNumber):
            random.shuffle(products_main)
            products_main_shuffled = ([Product.objects.get(id=i)
                                       for i in products_main])
            products_hot_food = (products_hot_food +
                                 products_main_shuffled[0: 3])

        """ SIDE COURSES """

        """ Generate 2 random side courses for each unspecified guest """
        products_side = ([i.id for i in
                          Product.objects.filter(category__course="side")])
        products_side_unspecified = []
        for i in range(bartholemew_unspecified):
            random.shuffle(products_side)
            products_side_shuffled = ([Product.objects.get(id=i)
                                       for i in products_side])
            products_side_unspecified = (products_side_unspecified +
                                         products_side_shuffled[0: 2])

        """ Generate 2 random side courses for each vegan guest """
        products_side = ([i.id for i in
                          Product.objects.filter(category__course="side",
                                                 allergies__contains="v")])
        products_side_vegan = []
        for i in range(bartholemew_vegan_guests):
            random.shuffle(products_side)
            products_side_shuffled = ([Product.objects.get(id=i)
                                       for i in products_side])
            products_side_vegan = (products_side_vegan +
                                   products_side_shuffled[0: 2])

        """ Generate 2 random side courses for each vegetarian guest """
        products_side = ([i.id for i in
                          Product.objects.filter(category__course="side",
                                                 allergies__contains="g")])
        products_side_veggie = []
        for i in range(bartholemew_veggie_guests):
            random.shuffle(products_side)
            products_side_shuffled = ([Product.objects.get(id=i)
                                       for i in products_side])
            products_side_veggie = (products_side_veggie +
                                    products_side_shuffled[0: 2])

        """ Generate 2 random side courses for each pescatarian guest """
        products_side = ([i.id for i in
                          Product.objects.filter(category__course="side",
                                                 allergies__contains="p")])
        products_side_pesc = []
        for i in range(bartholemew_pesc_guests):
            random.shuffle(products_side)
            products_side_shuffled = ([Product.objects.get(id=i)
                                       for i in products_side])
            products_side_pesc = (products_side_pesc +
                                  products_side_shuffled[0: 2])

        """ DESSERT COURSES """

        """ Generate 1 random dessert courses for each unspecified guest """
        products_dessert = ([i.id for i in
                             Product.objects.filter(category__course="dessert")])
        products_dessert_unspecified = []
        for i in range(bartholemew_unspecified):
            random.shuffle(products_dessert)
            products_dessert_shuffled = ([Product.objects.get(id=i)
                                          for i in products_dessert])
            products_dessert_unspecified = (products_dessert_unspecified +
                                            products_dessert_shuffled[0: 1])

        """ Generate 1 random dessert courses for each vegan guest """
        products_dessert = ([i.id for i in
                             Product.objects.filter(category__course="dessert",
                                                    allergies__contains="v")])
        products_dessert_vegan = []
        for i in range(bartholemew_vegan_guests):
            random.shuffle(products_dessert)
            products_dessert_shuffled = ([Product.objects.get(id=i)
                                          for i in products_dessert])
            products_dessert_vegan = (products_dessert_vegan +
                                      products_dessert_shuffled[0: 1])

        """ Generate 1 random dessert courses for each vegetarian guest """
        products_dessert = ([i.id for i in
                             Product.objects.filter(category__course="dessert",
                                                    allergies__contains="g")])
        products_dessert_veggie = []
        for i in range(bartholemew_veggie_guests):
            random.shuffle(products_dessert)
            products_dessert_shuffled = ([Product.objects.get(id=i)
                                          for i in products_dessert])
            products_dessert_veggie = (products_dessert_veggie +
                                       products_dessert_shuffled[0: 1])

        """ Generate 1 random dessert courses for each pescatarian guest """
        products_dessert = ([i.id for i in
                             Product.objects.filter(category__course="dessert",
                                                    allergies__contains="p")])
        products_dessert_pesc = []
        for i in range(bartholemew_pesc_guests):
            random.shuffle(products_dessert)
            products_dessert_shuffled = ([Product.objects.get(id=i)
                                          for i in products_dessert])
            products_dessert_pesc = (products_dessert_pesc +
                                     products_dessert_shuffled[0: 1])

        products_list_main = (products_main_unspecified +
                              products_main_vegan +
                              products_main_veggie +
                              products_main_pesc +
                              products_hot_food)
        products_list_side = (products_side_unspecified +
                              products_side_vegan +
                              products_side_veggie +
                              products_side_pesc)
        products_list_dessert = (products_dessert_unspecified +
                                 products_dessert_vegan +
                                 products_dessert_veggie +
                                 products_dessert_pesc)

        for product in products_list_dessert:
            category = product.category
            name = product.name
            price = product.price
            servings = 1

            """ Randomise the available option """
            try:
                category_option = Options.objects.get(category=category)
                rnd = random.randint(1, 3)
                if rnd == 1:
                    option = "selected-one"
                elif rnd == 2:
                    option = "selected-two"
                elif rnd == 3:
                    option = "selected-three"
            except ObjectDoesNotExist:
                option = "none"

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

        for product in products_list_side:
            category = product.category
            name = product.name
            price = product.price
            servings = 1

            """ Randomise the available option """
            try:
                category_option = Options.objects.get(category=category)
                rnd = random.randint(1, 3)
                if rnd == 1:
                    option = "selected-one"
                elif rnd == 2:
                    option = "selected-two"
                elif rnd == 3:
                    option = "selected-three"
            except ObjectDoesNotExist:
                option = "none"

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

        for product in products_list_main:
            category = product.category
            name = product.name
            price = product.price
            servings = 1

            """ Randomise the available option """
            try:
                category_option = Options.objects.get(category=category)
                rnd = random.randint(1, 3)
                if rnd == 1:
                    option = "selected-one"
                elif rnd == 2:
                    option = "selected-two"
                elif rnd == 3:
                    option = "selected-three"
            except ObjectDoesNotExist:
                option = "none"

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
            'products_list_main': products_list_main,
            'products_list_side': products_list_side,
            'products_list_dessert': products_list_dessert,
            'menu': menu,
        }

    return render(request, 'bartholemew/bartholemew_output.html', context)
