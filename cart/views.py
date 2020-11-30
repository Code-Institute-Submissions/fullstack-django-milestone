import os
import random, string
import stripe
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import ShoppingCart, Order
from products.models import Ebook

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

# Create your views here.

def get_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    random_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return random_str

@login_required
def addToCart(request, ebook_id):
    ebook = Ebook.objects.get(id=ebook_id)
    shopping_cart = ShoppingCart.objects.filter(customer=request.user)
    if shopping_cart.exists():
        shopping_cart[0].items.add(ebook)
    else:
        new_shopping_cart = ShoppingCart.objects.create(customer=request.user)
        new_shopping_cart.items.add(ebook)
        new_shopping_cart.save()
    messages.success(request, 'Your Shopping Cart has been updated')
    return redirect('home')

def deleteItem(request, ebook_id):
    shopping_cart = ShoppingCart.objects.get(customer=request.user)
    ebook = Ebook.objects.get(id=ebook_id)
    shopping_cart.items.remove(ebook)
    messages.success(request, 'Your Shopping Cart has been updated')
    return redirect('home')

def deleteItemCheckout(request, ebook_id):
    shopping_cart = ShoppingCart.objects.get(customer=request.user)
    ebook = Ebook.objects.get(id=ebook_id)
    shopping_cart.items.remove(ebook)
    return redirect('checkout')

def checkout(request):
    shopping_cart = ShoppingCart.objects.get(customer=request.user)
    shopping_cart_items = shopping_cart.items.all()
    grand_total = sum(item.price for item in shopping_cart_items)
    grand_total_pennies = int(grand_total*100)

    if request.method == 'POST':
        print('Data:', request.POST)

        customer = stripe.Customer.create(
            email = request.user.email,
            name = request.user.username,
            source = request.POST['stripeToken']
            )
        charge = stripe.Charge.create(
            customer = customer,
            amount = grand_total_pennies,
            currency = 'eur',
            description = 'Ebook purchase'
            )
        order = Order()
        order.ref = get_random_string(10)
        order.customer = request.user
        order.amount_paid = grand_total
        order.save()
        for item in shopping_cart_items:
            order.items.add(item)
        order.save()
        shopping_cart.delete()
        return redirect(reverse('success'))
    else:
        return render(request, 'cart/checkout.html', {'cart_items':shopping_cart_items,'grand_total':grand_total})

def successMsg(request):
    customer_orders = Order.objects.filter(customer=request.user)
    most_recent_order = customer_orders.last()
    items_list = most_recent_order.items.all()
    return render(request, 'cart/success.html', {'order':most_recent_order,'items_list':items_list})
