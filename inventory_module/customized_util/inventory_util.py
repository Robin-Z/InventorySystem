
from inventory_module.forms import borrow_material_form
from django.core.paginator import EmptyPage, PageNotAnInteger
import datetime


# Transfer good data to fit borrow_material_form
def borrow_material_form_util(good):
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

    return good_form


def page_util(paginator, page):

    try:
        goods_per_page = paginator.page(page)
    except PageNotAnInteger:
        goods_per_page = paginator.page(1)
    except EmptyPage:
        goods_per_page = paginator.page(paginator.num_pages)

    return goods_per_page

