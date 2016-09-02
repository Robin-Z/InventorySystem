from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import user, goods 

# Create your views here.

def welcome(request):
    return render(request, 'inventory_module/inventory/welcome.html')

def access_filter(request):
    # Receive user name and password from welcome.html page
    userName = request.GET['user_name']
    pwd = request.GET['passwd']
    
    # Judge if user name and password are correct, if correct direct to inventory_page.html, otherwise show user the warning
    if userName != '' and pwd != '':
        try:
            visitUser = user.objects.get(user_name=request.GET['user_name'])
            if pwd == visitUser.user_passwd:
                return render(request, 'inventory_module/inventory/details/inventory_page.html',{'user_name':userName, 'passwd':pwd,})
                #return render(request, 'inventory_module/inventory/main_page.html',{'user_name':userName, 'passwd':pwd,})
            else:
                login_warning = 'user name or pwd is incorrect!'
                return render(request,'inventory_module/inventory/welcome.html',{'login_warning': login_warning})
        except:
            login_warning = 'No this user!'
            return render(request, 'inventory_module/inventory/welcome.html', {'login_warning': login_warning})
    else:
        login_warning = 'user name or password cannot be blank!'
        return render(request, 'inventory_module/inventory/welcome.html',{'login_warning': login_warning})


def inventory(request):
    
    #get inventory info from database and show them in inventory_page.html
    goods_list = goods.objects.all()
    paginator = Paginator(goods_list, 1)
    page = request.GET.get('page')
    try:
        goods_per_page = paginator.page(page)
    except PageNotAnInteger:
        goods_per_page = paginator.page(1)
    except EmptyPage:
        goods_per_page = paginator.page(paginator.num_pages)
        
    return render(request, 'inventory_module/inventory/details/inventory_page.html',{'goods_list': goods_list, 'goods_per_page':goods_per_page})

            

