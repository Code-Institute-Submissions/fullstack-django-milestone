from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from products.models import Ebook
from cart.models import ShoppingCart
from .forms import PlainUserForm

def home(request):
    ebooks = Ebook.objects.all()
    if request.user.is_authenticated:
        shopping_cart = ShoppingCart.objects.filter(customer=request.user)
        if shopping_cart.exists():
            shopping_cart_items =shopping_cart[0].items.all()
            item_ids_list = []
            for item in shopping_cart_items:
                item_ids_list.append(item.id)
            grand_total = sum(item.price for item in shopping_cart_items)
            return render(request, 'accounts/home.html', {'ebooks':ebooks,'cart_items':shopping_cart_items,'items_ids':item_ids_list,'grand_total':grand_total})
        else:
            return render(request, 'accounts/home.html', {'ebooks':ebooks})
    else:
        return render(request, 'accounts/home.html', {'ebooks':ebooks})

def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
        messages.success(request, 'Registration successful')
        return redirect('login')
    else:
        form = PlainUserForm()
        return render(request, 'accounts/register.html', {'form':form})

def beforeLogout(request):
    shopping_cart = ShoppingCart.objects.filter(customer=request.user)
    if shopping_cart.exists():
        shopping_cart[0].delete()
    messages.info(request, 'Youve been logged out')
    return redirect ('logout')
