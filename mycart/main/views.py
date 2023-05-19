from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Search_history
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        get_suggestion_product = Search_history.objects.filter(user=request.user)[0:5]
        get_fashion_products = Product.objects.filter(p_cat = "fashion")[:4]
        get_electronics_products = Product.objects.filter(p_cat="electronics")[:4]
        get_access_products = Product.objects.filter(p_cat="accessories")[:4]
        return render(request,'index.html',{'get_suggestion_product':get_suggestion_product,'get_fashion_products':get_fashion_products,'get_electronics_products':get_electronics_products,'get_access_products':get_access_products})
    get_fashion_products = Product.objects.filter(p_cat="fashion")[:4]
    get_electronics_products = Product.objects.filter(p_cat="electronics")[:4]
    get_access_products = Product.objects.filter(p_cat="accessories")[:4]
    return render(request, 'index.html',{'get_fashion_products': get_fashion_products,
                   'get_electronics_products': get_electronics_products, 'get_access_products': get_access_products})

def fashion_section(request):
    get_mens_product = Product.objects.filter(p_sub_cat='mens')[0:4]
    get_womens_product = Product.objects.filter(p_sub_cat='womens')[0:4]
    get_kids_product = Product.objects.filter(p_sub_cat='kids')[0:4]
    return render(request,'fashion_sec.html',{'get_mens_product':get_mens_product,'get_womens_product':get_womens_product,'get_kids_product':get_kids_product})

def electronics_section(request):
    get_mobile_product = Product.objects.filter(p_sub_cat='mobile')[0:4]
    get_laptop_product = Product.objects.filter(p_sub_cat='laptop')[0:4]
    get_ipad_product = Product.objects.filter(p_sub_cat='ipad')[0:4]
    get_power_bank_product = Product.objects.filter(p_sub_cat='power bank')[0:4]
    return render(request, 'electronics_sec.html',{'get_mobile_product': get_mobile_product, 'get_laptop_product': get_laptop_product,'get_ipad_product': get_ipad_product,'get_power_bank_product':get_power_bank_product})

def accessory_section(request):
    get_watch_product = Product.objects.filter(p_sub_cat='watch')[0:4]
    get_sunglass_product = Product.objects.filter(p_sub_cat='sunglass')[0:4]
    get_earphone_product = Product.objects.filter(p_sub_cat='earphone')[0:4]
    get_earring_product = Product.objects.filter(p_sub_cat='earring')[0:4]
    return render(request, 'access.html',{'get_watch_product': get_watch_product, 'get_sunglass_product': get_sunglass_product,'get_earphone_product': get_earphone_product,'get_earring_product':get_earring_product})
def go_home(request):
    return redirect('/')

def search(request):
    searched_product = []
    if request.method == 'POST':
        get_search = request.POST.get('search', '')
        if get_search == '':
            return redirect('/')
        if get_search != '':
            if request.user.is_authenticated:
                user = request.user
                item_obj = Product.objects.filter(p_specification=get_search)
                print(f"The value of get_search is:-{get_search}")
                print(f"The value of item obj is:-{item_obj}")
                get_search = get_search.upper()
                if len(item_obj) != 0:
                    create_search_history = Search_history.objects.create(user=user,item=item_obj[0],data=get_search)
                    create_search_history.save()

            get_all_products = Product.objects.all()
            for product in get_all_products:
                upper = product.p_name.upper()
                if get_search in upper:
                    searched_product.append(product)
            if len(searched_product) == 0:
                messages.error(request,'Oopss... product not found')
    return render(request,'search.html',{'searched_product':searched_product})

def view_products(request,f_id = None,w_id = None,k_id = None,m_id = None,i_id = None,l_id = None,p_id = None,wh_id = None,s_id = None,e_id = None,er_id = None):
    if f_id != None:
        get_mens_product = Product.objects.filter(p_sub_cat='mens')
        return render(request, 'view.html', {'get_mens_product': get_mens_product})

    if w_id != None:
        get_womens_product = Product.objects.filter(p_sub_cat='womens')
        return render(request, 'view.html', {'get_womens_product': get_womens_product})

    if k_id != None:
        get_kids_product = Product.objects.filter(p_sub_cat='kids')
        return render(request, 'view.html', {'get_kids_product': get_kids_product})

    if m_id != None:
        get_mobile_product = Product.objects.filter(p_sub_cat='mobile')
        return render(request, 'view.html', {'get_mobile_product': get_mobile_product})

    if i_id != None:
        get_ipad_product = Product.objects.filter(p_sub_cat='ipad')
        return render(request, 'view.html', {'get_ipad_product': get_ipad_product})

    if l_id != None:
        get_laptop_product = Product.objects.filter(p_sub_cat='laptop')
        return render(request, 'view.html', {'get_laptop_product': get_laptop_product})

    if p_id != None:
        get_power_bank_product = Product.objects.filter(p_sub_cat='power bank')
        return render(request, 'view.html', {'get_power_bank_product': get_power_bank_product})

    if wh_id != None:
        get_watch_product = Product.objects.filter(p_sub_cat='watch')
        return render(request, 'view.html', {'get_watch_product': get_watch_product})

    if s_id != None:
        get_sunglass_product = Product.objects.filter(p_sub_cat='sunglass')
        return render(request, 'view.html', {'get_sunglass_product': get_sunglass_product})

    if e_id != None:
        get_earphone_product = Product.objects.filter(p_sub_cat='earphone')
        return render(request, 'view.html', {'get_earphone_product': get_earphone_product})

    if er_id != None:
        get_earring_product = Product.objects.filter(p_sub_cat='earring')
        return render(request, 'view.html', {'get_earring_product': get_earring_product})

def go_to_mens(request):
    get_mens_product = Product.objects.filter(p_sub_cat = "mens")
    return render(request,'view.html',{'get_mens_product':get_mens_product})

def go_to_womens(request):
    get_womens_product = Product.objects.filter(p_sub_cat = "womens")
    return render(request,'view.html',{'get_womens_product':get_womens_product})

def go_to_kids(request):
    get_kids_product = Product.objects.filter(p_sub_cat = "kids")
    return render(request,'view.html',{'get_kids_product':get_kids_product})

def go_to_mobile(request):
    get_mobile_product = Product.objects.filter(p_sub_cat = "mobile")
    return render(request,'view.html',{'get_mobile_product':get_mobile_product})

def go_to_laptop(request):
    get_laptop_product = Product.objects.filter(p_sub_cat = "laptop")
    return render(request,'view.html',{'get_laptop_product':get_laptop_product})

def go_to_ipad(request):
    get_ipad_product = Product.objects.filter(p_sub_cat = "ipad")
    return render(request,'view.html',{'get_ipad_product':get_ipad_product})

def go_to_power_bank(request):
    get_power_bank_product = Product.objects.filter(p_sub_cat = "power bank")
    return render(request,'view.html',{'get_power_bank_product':get_power_bank_product})
######################################
def go_to_watch(request):
    get_watch_product = Product.objects.filter(p_sub_cat = "watch")
    return render(request,'view.html',{'get_watch_product':get_watch_product})

def go_to_earring(request):
    get_earring_product = Product.objects.filter(p_sub_cat = "earring")
    return render(request,'view.html',{'get_earring_product':get_earring_product})

def go_to_earphone(request):
    get_earphone_product = Product.objects.filter(p_sub_cat = "earphone")
    return render(request,'view.html',{'get_earphone_product':get_earphone_product})

def go_to_sunglass(request):
    get_sunglass_product = Product.objects.filter(p_sub_cat = "sunglass")
    return render(request,'view.html',{'get_sunglass_product':get_sunglass_product})

def show(request,s_id):
    if request.user.is_authenticated:
        user = request.user
        item = Product.objects.filter(id=s_id)
        data = item[0].p_name
        create_search = Search_history.objects.create(user=user,item=item[0],data=data)
        create_search.save()
    sort = []
    get_searched_product = Product.objects.filter(id=s_id)
    get_specification = get_searched_product[0].p_specification
    get_similer_product = Product.objects.filter(p_specification = get_specification)[:4]
    for item in get_similer_product:
        if item != get_searched_product[0]:
            sort.append(item)
    return render(request,'show.html',{'get_searched_product':get_searched_product,'get_similer_product':sort})

def see_all(request,id):
    get_specification = Product.objects.filter(id=id)[0].p_specification
    get_see_all_products = Product.objects.filter(p_specification = get_specification)
    return render(request,'see_all.html',{'get_see_all_products':get_see_all_products})


@login_required(redirect_field_name='/accounts/login')
def cart(request,p_id):
    request.session['id'] = p_id
    user = request.user
    get_product = Product.objects.filter(id=p_id)
    check_cart = Cart.objects.filter(user=user,item=get_product[0])
    #####it check wheteher item present in cart if not it will create item in cart
    if len(check_cart) == 0:
        create_cart_item = Cart.objects.create(user=user,item=get_product[0])
        create_cart_item.save()

    ##for reload
    else:
        show_cart = Cart.objects.filter(user=user)

    get_cart_products = Cart.objects.filter(user=user)

    return render(request, 'cart.html', {'get_cart_products': get_cart_products[::-1]})

def inc_quantity(request,id):
    user = request.user
    get_click_product = Cart.objects.filter(id=id,user=user)
    quantity = get_click_product[0].quantity + 1
    update_quantity = Cart.objects.filter(id=id,user=user).update(quantity=quantity)
    p_id = request.session['id']
    price_per = quantity * get_click_product[0].item.p_price

    return redirect(f'/cart/{p_id}')

def dec_quantity(request,id):
    user = request.user
    get_click_product = Cart.objects.filter(id=id,user=user)
    if get_click_product[0].quantity > 1:
        quantity = get_click_product[0].quantity - 1
        update_quantity = Cart.objects.filter(id=id, user=user).update(quantity=quantity)
    else:
        quantity = get_click_product[0].quantity - 0
        update_quantity = Cart.objects.filter(id=id, user=user).update(quantity=quantity)
    p_id = request.session['id']
    return redirect(f'/cart/{p_id}')

def remove_cart_item(request,id):
    get_product = Cart.objects.filter(id = id)
    get_product.delete()
    p_id = request.session['id']
    return redirect(f"/cart/{p_id}")
