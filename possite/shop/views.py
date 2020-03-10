from fnmatch import filter
from logging import log
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request

from management.models import Product, Type
from shop.models import Order_Products, Order


# Create your views here.
def mylogin(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
            # return render(request, template_name='home.html')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'something wrong, please try again :\')'
    
    return render(request, template_name='login.html', context=context)

def mylogout(request):
    logout(request)
    print('logout')
    return redirect('mylogin')

# ------------------------------

@login_required
def home(request, do_what):
    search_product = request.POST.get('inputSearch', '')
    search_type = request.POST.get('selectSearch', '')
    
    type_list = Type.objects.all().order_by('id')
    product_list = Product.objects.all().order_by('id')

    order_list = ''
    order = Order()
    
    if request.method == 'POST':
        if do_what == 'search':
            if search_type != 'Choose...' and search_product != '':
                product_list = Product.objects.filter(type=search_type, name__icontains=search_product).order_by('id')
            elif search_type != 'Choose...':
                product_list = Product.objects.filter(type=search_type).order_by('id')
            elif search_product != '':
                product_list = Product.objects.filter(name__icontains=search_product).order_by('id')
        # ------------------------
        if do_what.isdigit():
            if request.POST.get('amountp', '') != '' and request.POST.get('amountp', '') != '0':
                product = Product.objects.get(pk=do_what)
                # order_list = Order_Products.objects.create(
                #     order_id = order.objects.get(pk),
                #     product_id_id = product.id,
                #     amount = request.POST.get('amountp', '')
                # )
                print(order.total_price)
                print(product.name, product.id)
                print('add:(' + do_what + ')' + product.name + ' x ' + request.POST.get('amountp', ''))
            else:
                order_list = Order_Products.objects.none()

    context = {
        'search_product': search_product,
        'search_type': search_type,
        'type_list': type_list,
        'product_list': product_list,
        'order_list': order_list
    }

    return render(request, 'home.html', context=context)