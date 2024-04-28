from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from .models import Cart
from django.contrib import auth, messages
from .models import Products
from .models import User
from .utils import get_user_carts


def cart_add(request,product_slug):
    # product_id = request.POST.get("product_id")

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    # return redirect(request.META['HTTP_REFERER'])
    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    # response_data = {
    #     "message": "Товар добавлен в корзину",
    #     "cart_items_html": cart_items_html,
    # }
    messages.success(request, f" Товар добавлен в корзину")
    # return JsonResponse(response_data)
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, cart_id):
    cart_id = Cart.objects.get(id=cart_id)
    quantity = request.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request=request)

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quaantity": updated_quantity,
    }

    return redirect(request.META['HTTP_REFERER'])
    # #
    # return JsonResponse(response_data)
    # cart_id = request.POST.get("cart_id")
    # quantity = request.POST.get("quantity")
    #
    # cart = Cart.objects.get(id=cart_id)
    #
    # cart.quantity = quantity
    # cart.save()
    # updated_quantity = cart.quantity
    #
    # cart = get_user_carts(request)
    # cart_items_html = render_to_string(
    #     "carts/includes/included_cart.html", {"carts": cart}, request=request)
    #
    # response_data = {
    #     "message": "Количество изменено",
    #     "cart_items_html": cart_items_html,
    #     "quaantity": updated_quantity,
    # }
    #
    # return JsonResponse(response_data)


def cart_remove(request, cart_id):

    # cart_id = request.POST.get("cart_id")
    #
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    # quantity = cart.quantity
    # cart.delete()
    #
    # user_cart = get_user_carts(request)
    # cart_items_html = render_to_string(
    #     "carts/includes/included_cart.html", {"carts": user_cart}, request=request)
    #
    # response_data = {
    #     "message": "Товар удален",
    #     "cart_items_html": cart_items_html,
    #     "quantity_deleted": quantity,
    # }
    #
    # return JsonResponse(response_data)
    messages.success(request, f"Товар удален")
    return redirect(request.META['HTTP_REFERER'])