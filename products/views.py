from django.shortcuts import render
from products.models import Ebook
from cart.models import ShoppingCart

# Create your views here.

def showEbook(request, ebook_id):
    ebook = Ebook.objects.get(id=ebook_id)

    if request.user.is_authenticated:
        shopping_cart = ShoppingCart.objects.filter(customer=request.user)
        if shopping_cart.exists():
            shopping_cart_items =shopping_cart[0].items.all()
            item_ids_list = []
            for item in shopping_cart_items:
                item_ids_list.append(item.id)
            grand_total = sum(item.price for item in shopping_cart_items)
            return render(request, 'products/ebook.html', {'ebook':ebook,'cart_items':shopping_cart_items,'items_ids':item_ids_list,'grand_total':grand_total})
        else:
            return render(request, 'products/ebook.html', {'ebook':ebook})
    else:
        return render(request, 'products/ebook.html', {'ebook':ebook})
