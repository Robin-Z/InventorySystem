from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import goods, borrow_goods_list
from forms import borrow_material_form, my_info_form
from django.contrib.auth.decorators import login_required
import datetime

"""
User Django's buildin login/logout system, so delete my own login and access filter views here.
As cannot get request user content with my own views.
"""

"""
The information of the material in inventory
Use decorator to filter unlogin user
"""

@login_required(login_url='/inventory_module/accounts/login')
def home_page(request):
    return render(request, 'inventory_module/inventory/home.html')

@login_required(login_url='/inventory_module/accounts/login')
def inventory(request):
    #get inventory info from database and show them in inventory_page0.html

    goods_list = goods.objects.all()
    paginator = Paginator(goods_list, 2)
    page = request.GET.get('page')
    try:
        goods_per_page = paginator.page(page)
    except PageNotAnInteger:
        goods_per_page = paginator.page(1)
    except EmptyPage:
        goods_per_page = paginator.page(paginator.num_pages)

    return render(request,
                  'inventory_module/inventory/details/inventory_page.html', {'goods_list': goods_list, 'goods_per_page':goods_per_page, 'user_name': request.user})

# The view of borrow material
@login_required(login_url='/inventory_module/accounts/login')
def borrow_material(request, good_id):
    good = goods.objects.values().get(id=good_id)
    good_apply_dict = {'goods_id': good['id'],
                        'goods_name': good['goods_name'],
                        'goods_part_num': good['goods_part_num'],
                        'goods_spec': good['goods_spec'],
                        'goods_revision': good['goods_revision'],
                        'goods_location': good['goods_location'],
                        'goods_unit': good['goods_unit'],
                        'goods_onhand_qty': int(good['goods_qty']),
                        'goods_borrow_qty': 0,
                        'goods_borrow_date': datetime.datetime.now()}

    # Form bind data
    good_form = borrow_material_form(good_apply_dict)

    return render(request, 'inventory_module/inventory/details/borrow_material.html', {'form': good_form})

# The information of the material that the user borrowed
@login_required(login_url='/inventory_module/accounts/login')
def my_borrow(request):
    login_user = request.user
    borrow_goods = []
    borrow_good_arr = []
    borrow_list = borrow_goods_list.objects.values().filter(borrower_id=login_user.id)

    # Get good info with goods_id
    for borrow in borrow_list:
        borrow_goods.append(goods.objects.values().get(id=borrow['borrow_goods_id']))

    # Concatenate borrow_goods_list and goods
    for index_i in range(int(len(borrow_list))):
        borrow_good_dict = dict(borrow_list[index_i], **borrow_goods[index_i])
        borrow_good_arr.append(borrow_good_dict)

    # Show in separate pages
    paginator = Paginator(borrow_good_arr, 5)
    page = request.GET.get('page')
    try:
        borrow_good_per_page = paginator.page(page)
    except PageNotAnInteger:
        borrow_good_per_page = paginator.page(1)
    except EmptyPage:
        borrow_good_per_page = paginator.page(paginator.num_pages)

    return render(request, 'inventory_module/inventory/details/my_borrow_list.html', {'borrow_good_arr': borrow_good_arr, 'borrow_good_per_page': borrow_good_per_page, 'user_name': request.user})

@login_required(login_url='/inventory_module/accounts/login')
def my_info(request):

    info_form = my_info_form({'user_id': request.user.id,
                              'user_name': request.user.username,
                              'email': request.user.email})
    return render(request, 'inventory_module/inventory/details/my_info.html', {'my_info_form': info_form})

@login_required(login_url='/inventory_module/accounts/login')
def add_borrow_record(request):
    add_record_note = ''

    if request.POST.has_key('submit_btn'):
        if borrow_goods_list.objects.create(borrower_id=request.user.id,
                                            borrow_goods_id=request.POST['goods_id'],
                                            borrow_goods_qty=request.POST['goods_borrow_qty'],
                                            borrow_date=request.POST['goods_borrow_date'],
                                            borrow_status='Open'):

            """ Update onhandQty in database """
            good_borrowed = goods.objects.get(id=request.POST['goods_id'])
            good_borrowed.goods_qty = int(request.POST['goods_onhand_qty']) - int(request.POST['goods_borrow_qty'])
            good_borrowed.save()

            add_record_note = 'Borrow ' + request.POST['goods_borrow_qty'] + ' ' + request.POST['goods_unit'] + ' ' + \
                              request.POST['goods_name'] + ' sucessfully!'
        else:
            add_record_note = 'Borrow ' + request.POST['goods_borrow_qty'] + ' ' + request.POST['goods_unit'] + ' ' + \
                              request.POST['goods_name'] + ' failed!'
    elif request.POST.has_key('cancel_btn'):
        return render(request,
                      'inventory_module/inventory/details/inventory_page.html')

    return render(request, 'inventory_module/inventory/details/borrow_result.html', {'borrow_result': add_record_note})

