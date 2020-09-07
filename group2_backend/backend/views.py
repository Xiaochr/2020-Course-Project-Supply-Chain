from django.shortcuts import render
from django.http.response import *
from .models import *
import requests
import datetime
from django.forms.models import model_to_dict
# Create your views here.


def info(request): ##获取MaterialInfo表中的所有数据
    all_data = list(MaterialInfo.objects.all().values())
    rep = JsonResponse(all_data, safe = False)
    return rep

def info_add(request):
    data_dict = request.POST
    mID = data_dict.get('mID')
    mName = data_dict.get('mName')
    mType = data_dict.get('mType')
    price1 = data_dict.get('price1')
    price2 = data_dict.get('price2')
    price3 = data_dict.get('price3')
    unit = data_dict.get('unit')
    safetyType = data_dict.get('safetyType')
    outType = data_dict.get('outType')
    shelfLife = data_dict.get('shelfLife')
    to_insert = MaterialInfo(mID,mName, mType, price1, price2, price3, unit,
        safetyType, outType, shelfLife)
    
    to_insert.save()
    rep = HttpResponse("Successfully added the new data. ")
    return rep

def info_del(request):
    data_dict = request.POST
    mID = data_dict.get('mID')
    target = MaterialInfo.objects.get(pk = mID)
    target.delete()
    rep = HttpResponse("Successfully delete the target data. ")
    return rep

def info_edit(request):
    data_dict = request.POST
    mID = data_dict.get('mID')
    mName = data_dict.get('mName')
    mType = data_dict.get('mType')
    price1 = data_dict.get('price1')
    price2 = data_dict.get('price2')
    price3 = data_dict.get('price3')
    unit = data_dict.get('unit')
    safetyType = data_dict.get('safetyType')
    outType = data_dict.get('outType')
    shelfLife = data_dict.get('shelfLife')
    target = MaterialInfo.objects.get(pk = mID)
    target.mName = mName
    target.mType = mType
    target.price1 = price1
    target.price2 = price2
    target.price3 = price3
    target.unit = unit
    target.safetyType = safetyType
    target.outType = outType
    target.shelfLife = shelfLife
    target.save()
    rep = HttpResponse("Successfully update the target data. ")
    return rep

def info_search(request):
    data_dict = request.POST
    mName = data_dict.get('mName')
    all_data = list(MaterialInfo.objects.filter(mName__contains=mName).values())
    rep = JsonResponse(all_data, safe = False)
    return rep

def stock(request):
    all_data = list(MaterialStock.objects.all().values())
    rep = JsonResponse(all_data, safe = False)
    return rep

def stock_add(request):
    data_dict = request.POST
    mID = data_dict.get('mID')
    mName = data_dict.get('mName')
    moID = data_dict.get('moID')
    # arrival = data_dict.get('arrival')
    stock = data_dict.get('stock')
    mState = data_dict.get('mState')
    # to_insert = MaterialStock(moID,mID,mName, arrival, stock, mState)
    to_insert = MaterialStock(moID = moID,mID = mID,mName = mName, stock = stock, mState = mState)
    
    to_insert.save()
    rep = HttpResponse("Successfully added the new data. ")
    return rep

def stock_search(request):
    data_dict = request.POST
    mName = data_dict.get('mName')
    print(mName)
    all_data = list(MaterialStock.objects.filter(mName__contains=mName).values())
    rep = JsonResponse(all_data, safe = False)
    return rep          

def stock_filter(request):
    data_dict = request.POST
    mState = data_dict.get('state')
    all_data = list(MaterialStock.objects.filter(mState=mState).values())
    rep = JsonResponse(all_data, safe = False)
    return rep      

def stock_count(request):
    
    def check_date(date,expiration_time):
        '''
        date: datetime
        expiration_time: int
        '''
        gap = (datetime.datetime.now() - datetime.datetime.strptime(str(date),'%Y-%m-%d') ).days
        # if gap >= expiration_time:
        if gap >= 0:
            return True
        else:
            return False 
    
    all_data = list(MaterialStock.objects.all())
    filtered_data = []
    for item in all_data[3:]:
        # mID = item.get('mID')
        mID = item.mID
        material_obj = MaterialInfo.objects.get(pk = mID)
        shelfLife = material_obj.shelfLife
        moID = item.moID
        arrival_date = item.arrival
        res = check_date(arrival_date, shelfLife)
        if res and item.mState == 0:
            item.mState = 3
            item.save()
            filtered_data.append(model_to_dict(item))
    return JsonResponse(filtered_data,safe = False)

def stock_send(request):
    ## TODO URL修正
    data_dict = request.POST.dict()
    url = 'http://127.0.0.1:8000/None/'
    res = requests.post(url = url, data = data_dict)
    print(res.text)
    rep = HttpResponse("Successfully send the target data. ")
    return rep

def morder(request):
    all_data = list(MaterialOrder.objects.all().values())
    rep = JsonResponse(all_data, safe = False)
    return rep

def morder_add(request):
    data_dict = request.POST
    moID = data_dict.get('moID')
    oDate = data_dict.get('oDate')
    aDate = data_dict.get('aDate')
    moState = data_dict.get('moState')
    order_data_list = data_dict.get("data")
    to_insert = MaterialOrder(moID,oDate,aDate,moState)
    to_insert.save()
    for item in order_data_list:
        print(type(item))
        print(item)
    rep = HttpResponse("Successfully added the new data. ")
    return rep


def morder_detail(request):
    data_dict = request.POST
    moID = data_dict.get('moID')
    # all_data = list(MaterialOrderDetail.objects.filter(moID__exact=moID).values())
    all_data = list(MaterialOrderDetail.objects.filter(moID=moID).values())

    rep = JsonResponse(all_data, safe = False)
    return rep      

def morder_detail_add(request):
    data_dict = request.POST
    _id = data_dict.get('id')
    moID = data_dict.get('moID')
    mID = data_dict.get('mID')
    amount = data_dict.get('amount')
    unit = data_dict.get('unit')
    price = data_dict.get('price')

    to_insert = MaterialOrderDetail(_id,moID,mID,amount,unit,price)
    to_insert.save()
    rep = HttpResponse("Successfully added the new data. ")
    return rep    

def morder_filter(request):
    data_dict = request.POST
    moState = data_dict.get('state')
    all_data = list(MaterialOrder.objects.filter(moState=moState).values())
    rep = JsonResponse(all_data, safe = False)
    return rep   
    
def morder_stockin(request):
    data_dict = request.POST
    moID = data_dict.get('moID') 
    target = MaterialOrder.objects.get(pk = moID)
    target.moState = 1
    all_data = list(MaterialOrderDetail.objects.filter(moID__exact = moID))
    for item in all_data:
        mID = item.mID
        amount = item.amount
        target = MaterialStock.objects.get(mID = mID)
        orig_stock = target.stock
        new_stock = orig_stock + amount
        target.stock = new_stock
    rep = HttpResponse("Successfully modify the new data. ")
    return rep
    
def korder(request):
    all_data = list(KitchenOrder.objects.all().values())
    rep = JsonResponse(all_data, safe = False)
    return rep

def korder_detail(request):
    order_id = request.GET.get('order_id')
    all_data = KitchenOrderDetails.objects.filter(order_id = order_id)
    rep = JsonResponse(all_data, safe = False)
    return rep    

# def material(request):




