import datetime
from fnmatch import filter
from logging import log
from traceback import print_exception

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request

from management.models import Product, Type
from shop.models import Order, Order_Products


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

# ------------------------------ #
# ------------------------------ #

@login_required
def home(request):
    # Search
    search_product = request.POST.get('inputSearch', '')
    search_type = request.POST.get('selectSearch', '')
    
    type_list = Type.objects.all().order_by('id')
    product_list = Product.objects.all().order_by('id')
    # -------

    # add to cart
    lastest_order = Order.objects.latest('id')
    pay = 0

    if lastest_order.confirm == False:
        order = lastest_order.id #pk
        makingorder = Order_Products.objects.filter(order_id_id=lastest_order.id).order_by('id')
        lastest_order = Order.objects.latest('id')
        for op in makingorder:
            price = Product.objects.get(pk=op.product_id_id)
            pay += (op.amount*price.price)
        lastest_order.total_price = pay
        lastest_order.save()    

    else:
        norder = Order.objects.create(
                date_time = datetime.date.today(),
                total_price = 0,
                confirm = False
        )
        order = norder.id
        makingorder = Order_Products.objects.filter(order_id_id=lastest_order.id).order_by('id')
        print('new order id:', order)
        pay = 0

    # -------
    if request.method == 'POST':
        if 'formsearch' in request.POST:
            if search_type != 'Choose...' and search_product != '':
                product_list = Product.objects.filter(type=search_type, name__icontains=search_product).order_by('id')
            elif search_type != 'Choose...':
                product_list = Product.objects.filter(type=search_type).order_by('id')
            elif search_product != '':
                product_list = Product.objects.filter(name__icontains=search_product).order_by('id')
                
        elif 'formadd' in request.POST:
            amountproduct = request.POST.get('amountp', '')
            goodid = request.POST.get('pickname', '')

            if amountproduct != '' and amountproduct != '0':
                amountproduct = int(amountproduct)
                good = Product.objects.get(pk=goodid)

                noworder = Order_Products.objects.create(
                    order_id_id = order,
                    product_id_id = good.id,
                    amount = amountproduct
                )

                makingorder = Order_Products.objects.filter(order_id_id=lastest_order.id)
                pay = 0
                makingorder = Order_Products.objects.filter(order_id_id=lastest_order.id)
                for op in makingorder:
                    price = Product.objects.get(pk=op.product_id_id)
                    pay += (op.amount*price.price)

        elif 'formdelete' in request.POST:
            deleteproduct = Order_Products.objects.filter(order_id_id=lastest_order.id, id=request.POST.get('throwout', ''))
            deleteproduct.delete()
            makingorder = Order_Products.objects.filter(order_id_id=lastest_order.id)
            pay = 0
            for op in makingorder:
                price = Product.objects.get(pk=op.product_id_id)
                pay += (op.amount*price.price)

        elif 'formsale' in request.POST:
            print('Sale')
            pay = 0
            makingorder = Order_Products.objects.filter(order_id_id=lastest_order.id)
            for op in makingorder:
                price = Product.objects.get(pk=op.product_id_id)
                pay += (op.amount*price.price)
            if pay != 0:
                lastest_order = Order.objects.latest('id')
                lastest_order.date_time = datetime.date.today()
                lastest_order.total_price = pay
                lastest_order.confirm = True
                lastest_order.save()
                makingorder = ''
                pay = 0


    context = {
        'search_product': search_product,
        'search_type': search_type,
        'type_list': type_list,
        'product_list': product_list,
        'makingorder': makingorder,
        'pay': pay
    }

    return render(request, 'home.html', context=context)