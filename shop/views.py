from django.shortcuts import render
from  django.http import  HttpResponse
from .models import Product,Contact,Order,track
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from .PayTm import Checksum
MERCHANT_KEY = 'txb0#@zEx6%vNU@6'

def index(request):
    allprod = []
    catprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprod.append([prod, range(1, nslides), nslides])
    params = {'allpro': allprod}
    return render(request, 'shophome.html', params)

def searchmatch(query, item):
    if query in item.product_description.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.sub_category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allprod = []
    catprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchmatch(query, item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprod.append([prod, range(1, nslides), nslides])
    params = {'allpro': allprod, "msg": ""}
    if len(allprod) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'search.html', params)

def aboutus(request):
    return render(request,'aboutus.html')

def allproducts(request):
    allprod = []
    prod=Product.objects.all()
    n = len(prod)
    nslides = ceil(n/4)
    allprod.append([prod, range(1, nslides), nslides])
    params = {'allpro': allprod}
    return render(request, 'allproducts.html', params)


def contactus(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, description=desc)
        contact.save()
    return render(request, 'contactus.html')
def productview(request,myid):
    products=Product.objects.filter(id=myid)
    return render(request,'productview.html',{'prods':products[0]})


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = track.objects.filter(orderid=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.updatedesc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'tracker.html')

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsjson', '')
        amount=request.POST.get('amount','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        adress = request.POST.get('adress1', '') + " " + request.POST.get('adress2', '')
        city = request.POST.get('city', '')
        district=request.POST.get('district','')
        state = request.POST.get('state', '')
        pincode = request.POST.get('pincode', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json,name=name,email=email,adress=adress,city=city,district=district,state=state,pincode=pincode,phone=phone,amount=amount)
        order.save()
        update=track(orderid=order.order_id,updatedesc="order placed")
        update.save()
        thank = True
        id = order.order_id
        # return render(request, 'checkout.html', {'thank':thank, 'id': id})
        param_dict = {

                'MID': 'eQnNxY96458227361378',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'checkout.html')

def cart(request):
    return render(request,'cart.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

