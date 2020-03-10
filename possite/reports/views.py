from datetime import datetime
from time import strftime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from shop.models import Order, Order_Products


# Create your views here.
@login_required
def show(request, reportlist):
    allorder = Order.objects.all().order_by('-date_time')
    today = datetime.today()
    sum = 0
    msg = 'All Order'
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

    if request.method == 'POST':
        if reportlist == 'rep_day':
            search_day = request.POST.get('search_day', '')
            allorder = Order.objects.filter(date_time=search_day).order_by('-date_time')
            msg = search_day[8:] + '/' + search_day[5:7] + '/' + search_day[0:4]
        elif reportlist == 'rep_week':
            search_week = request.POST.get('search_week', '')
            allorder = Order.objects.filter(date_time__week=search_week[6:]).order_by('-date_time')
            msg = search_week
        elif reportlist == 'rep_month' and request.POST.get('search_month', '') != 'Choose...':
            search_month = request.POST.get('search_month', '')
            allorder = Order.objects.filter(date_time__month=search_month).order_by('-date_time')
            msg = month_list[int(search_month)-1]
        elif reportlist == 'rep_year' and request.POST.get('search_year', '') != 'Choose...':
            search_year = request.POST.get('search_year', '')
            allorder = Order.objects.filter(date_time__year=search_year).order_by('-date_time')
            msg = search_year

    for i in allorder:
        sum += i.total_price

    context = {
        'allorder': allorder,
        'month_list': month_list,
        'sum': sum,
        'msg': msg
    }
    return render(request, template_name='report.html', context=context)