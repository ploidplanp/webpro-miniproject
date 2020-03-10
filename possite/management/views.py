from builtins import object

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.context_processors import request

from management.models import Product, Type

# Create your views here.

@login_required
def manage(request):

    search_product = request.POST.get('inputSearch', '')
    search_type = request.POST.get('selectSearch', '')

    type_list = Type.objects.all().order_by('id')
    product_list = Product.objects.all().order_by('id')

    if request.method == 'POST':
        if search_type != 'Choose...' and search_product != '':
            product_list = Product.objects.filter(type=search_type, name__icontains=search_product)
        elif search_type != 'Choose...':
            product_list = Product.objects.filter(type=search_type)
        elif search_product != '':
            product_list = Product.objects.filter(name__icontains=search_product)

    context = {
        'type_list': type_list,
        'product_list': product_list
    }

    return render(request, template_name='manage.html', context=context)

# ---------ABOUT PRODUCT MANAGEMENT---------

@login_required
def add_product(request):
    
    type_list = Type.objects.all().order_by('id')
    msg = ''

    if request.method == 'POST':
        if request.POST.get('productname') != '' and request.POST.get('producttype') != 'Choose...':
            # type = Type.object.get
            product = Product.objects.create(
                name = request.POST.get('productname'),
                type_id = request.POST.get('producttype'),
                description = request.POST.get('productdes'),
                price = request.POST.get('productprice')
            )
            msg = 'Add Product Successful'
    else:
        product = Product.objects.none()
        

    context = {
        'type_list': type_list,
        'msg': msg
    }
    return render(request, template_name='product_m/add_product.html', context=context)

@login_required
def edit_product(request, product_id):
    print(product_id)
    print(request.method)
    type_list = Type.objects.all().order_by('id')

    msg = ''

    try:
        product = Product.objects.get(pk=product_id)
        msg = ''
    except Product.DoesNotExist:
        return redirect('manage')

    if(request.method == 'POST') and request.POST.get('choose_type') != 'Choose...':
        product.name = request.POST.get('productname')
        product.type_id = request.POST.get('choose_type')
        product.description = request.POST.get('productdes')
        product.price = request.POST.get('productprice')
        product.save()

    msg = 'Update Product Successful'

    context = {
        'product': product,
        'type_list': type_list,
        'msg': msg
    }

    return render(request, template_name='product_m/edit_product.html', context=context)

@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

    return redirect(to='manage')

# ------------------

# ---------ABOUT TYPE MANAGEMENT---------

@login_required
def add_type(request):
    msg = ''
    if request.method == 'POST':
        if request.POST.get('typename') != '':
            type = Type.objects.create(
                name = request.POST.get('typename'),
                description = request.POST.get('typedes')
            )
            msg = 'Add Type Successful'
    else:
        type = Type.objects.none()

    context = {
        'msg': msg
    }

    return render(request, template_name='type_m/add_type.html', context=context)

@login_required
def edit_type(request, type_id):
    print(request.method)
    msg = ''

    try:
        type = Type.objects.get(pk=type_id)
        msg = ''
    except Type.DoesNotExist:
        return redirect('alltype')

    if(request.method == 'POST'):
        type.name = request.POST.get('typename')
        type.description = request.POST.get('typedes')
        type.save()


    msg = 'Update Type Successful'

    context = {
        'type': type,
        'msg': msg
    }

    return render(request, template_name='type_m/edit_type.html', context=context)

@login_required
def delete_type(request, type_id):
    type = Type.objects.get(id=type_id)
    type.delete()
    return redirect('alltype')


@login_required
def alltype(request):
    type_list = Type.objects.all().order_by('id')
    context = {
        'type_list': type_list
    }
    return render(request, template_name='type_m/type_detail.html', context=context)

# ------------------
