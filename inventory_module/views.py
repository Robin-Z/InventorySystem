from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from models import goods, borrow_goods_list
from forms import my_info_form
from django.contrib.auth.decorators import login_required
from customized_util.inventory_util import borrow_material_form_util, page_util

"""
User Django's buildin login/logout system, so delete customized login and access filter views here.
Use decorator to filter un-login users.
"""

"""
Redirect to home, about and contact page
"""


@login_required(login_url='/inventory_module/accounts/login/')
def home_page(request):
    return render(request, 'inventory_module/inventory/home.html')


@login_required(login_url='/inventory_module/accounts/login/')
def about_page(request):
    return render(request, 'inventory_module/inventory/about.html')


@login_required(login_url='/inventory_module/accounts/login/')
def contact_page(request):
    return render(request, 'inventory_module/inventory/contact.html')


"""
The view of inventory list. Retrieve all the materials in database and show the data.
"""


@login_required(login_url='/inventory_module/accounts/login/')
def inventory(request):
    # get inventory info from database and show them in inventory_page0.html

    goods_list = goods.objects.all()

    paginator = Paginator(goods_list, 2)
    page = request.GET.get('page')

    # Get data for each page
    goods_per_page = page_util(paginator, page)

    return render(request, 'inventory_module/inventory/details/inventory_page.html',
                  {'goods_list': goods_list, 'goods_per_page': goods_per_page})


"""
The view for user to borrow material.
"""


@login_required(login_url='/inventory_module/accounts/login/')
def borrow_material(request, good_id):
    # Query data from database by good_id
    good = goods.objects.values().get(id=good_id)

    # Transfer data to barrow_material_form
    good_form = borrow_material_form_util(good)

    return render(request, 'inventory_module/inventory/details/borrow_material.html', {'form': good_form})


"""
The information of the material that the user borrowed.
Showing materials that borrowed by users only to the right user.
"""


@login_required(login_url='/inventory_module/accounts/login/')
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

    # Reverse borrow good arr list to put the latest borrow record at the top of the list.
    borrow_good_arr.reverse()
        
    # Show in separate pages
    paginator = Paginator(borrow_good_arr, 5)
    page = request.GET.get('page')

    # Get data for each page
    borrow_good_per_page = page_util(paginator, page)

    return render(request, 'inventory_module/inventory/details/my_borrow_list.html',
                  {'borrow_good_arr': borrow_good_arr, 'borrow_good_per_page': borrow_good_per_page})


"""
The view of showing my_info page.
"""


@login_required(login_url='/inventory_module/accounts/login')
def my_info(request):
    info_form = my_info_form({'user_id': request.user.id,
                              'user_name': request.user.username,
                              'email': request.user.email})
    return render(request, 'inventory_module/inventory/details/my_info.html', {'my_info_form': info_form})


"""
If borrow qty is not bigger than on-hand qty, add a borrow record into database. Otherwise, warn the user.
"""


@login_required(login_url='/inventory_module/accounts/login/')
def add_borrow_record(request):
    add_record_note = ''

    if request.POST.has_key('submit_btn'):

        onhand_qty = int(request.POST['goods_onhand_qty'])
        borrow_qty = int(request.POST['goods_borrow_qty'])
        remain_qty = onhand_qty - borrow_qty

        # Judge if have enough on-hand material to lend
        if (remain_qty < 0) or (remain_qty == onhand_qty):
            print('Borrow qty is invalid! Bigger than on-hand qty or 0!')
            lack_warning = 'Borrow qty is invalid! Bigger than on-hand qty or 0!'
            redirect_url = '/inventory_module/borrow_material/' + request.POST['goods_id'] + '/'
            return redirect(redirect_url)

        # Create borrow record if have enough material on-hand
        elif borrow_goods_list.objects.create(borrower_id=request.user.id,
                                              borrow_goods_id=request.POST['goods_id'],
                                              borrow_goods_qty=request.POST['goods_borrow_qty'],
                                              borrow_date=request.POST['goods_borrow_date'],
                                              borrow_status='Open'):

            # Update on-handQty in database
            good_borrowed = goods.objects.get(id=request.POST['goods_id'])

            good_borrowed.goods_qty = remain_qty
            good_borrowed.save()

            add_record_note = 'Borrow ' + request.POST['goods_borrow_qty'] + ' ' + request.POST['goods_unit'] + ' ' + \
                              request.POST['goods_name'] + ' successfully!'
        else:
            add_record_note = 'Borrow ' + request.POST['goods_borrow_qty'] + ' ' + request.POST['goods_unit'] + ' ' + \
                              request.POST['goods_name'] + ' failed!'

    elif request.POST.has_key('cancel_btn'):
        return render(request, 'inventory_module/inventory/details/inventory_page.html')

    return render(request, 'inventory_module/inventory/details/borrow_result.html', {'borrow_result': add_record_note})


"""
Search material by key word
"""


@login_required(login_url='/inventory_module/accounts/login/')
def query_by_keyword(request):
    query_info = request.POST['query_info']

    if query_info != '':
        try:
            # search data from database per parameters of goods in turn, until retrieve the parameters provided.
            query_good = goods.objects.values().filter(goods_name=query_info)
            if len(query_good) == 0:
                query_good = goods.objects.values().filter(goods_part_num=query_info)
            if len(query_good) == 0:
                query_good = goods.objects.values().filter(goods_spec=query_info)
            if len(query_good) == 0:
                query_good = goods.objects.values().filter(goods_location=query_info)
            if len(query_good) == 0:
                query_good = goods.objects.values().filter(id=int(query_info))
        except Exception as searchError:
            print('queryByKeyWord: searchError: %s' % searchError)
            # return search result if no data found in database
            search_result = 'No ' + query_info + ' found in the inventory!'
            return render(request, 'inventory_module/inventory/home.html', {'search_result': search_result})
    else:
        # warning if user didn't input anything
        search_result = 'You input nothing!'
        return render(request, 'inventory_module/inventory/home.html', {'search_result': search_result})

    goods_list = query_good

    # paginate search result
    paginator = Paginator(goods_list, 3)
    page = request.GET.get('page')
    goods_per_page = page_util(paginator, page)

    # return search result to inventory_page.html
    return render(request, 'inventory_module/inventory/details/inventory_page.html',
                  {'goods_list': goods_list, 'goods_per_page': goods_per_page})
