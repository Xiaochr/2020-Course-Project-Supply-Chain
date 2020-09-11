from django.shortcuts import render
from django.http.response import *
from .models import *
import requests
import datetime
import xmltodict, json
import os
from django.forms.models import model_to_dict
import copy

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
        if res:
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
    data_list = eval(str(request.body,encoding = 'utf-8'))
    moID = int(data_list[0]['moID'])
    oDate = datetime.datetime.now()

    aDate = oDate ## 待修改！！！！
    aDate = datetime.datetime.now()

    moState = 0

    to_insert = MaterialOrder(moID,oDate,aDate,moState)
    to_insert.save()
    for item in data_list:
        mID = int(item['mID'])
        amount = int(item['amount'])
        unit = item['unit']
        price = float(item['price'])
        material_table = MaterialInfo.objects.get(mID = mID)
        material_order_table = MaterialOrder.objects.get(moID = moID)
        to_insert_ = MaterialOrderDetail(moID = material_order_table, mID = material_table, amount = amount, unit = unit, price = price)
        to_insert_.save()
    rep = HttpResponse("Successfully added the new data. ")
    return rep

def morder_detail(request):
    data_dict = request.POST
    moID = data_dict.get('moID')
    all_data = list(MaterialOrderDetail.objects.filter(moID_id=moID).values())
    repackeged_data = []
    for item in all_data:
        mID = item['mID_id']
        target_obj = MaterialInfo.objects.get(mID = mID)
        mName = target_obj.mName
        item['mName'] = mName
        repackeged_data.append(copy.deepcopy(item))
    rep = JsonResponse(repackeged_data, safe = False)
    return rep          

def morder_detail_add(request):
    data_dict = request.POST
    mName= data_dict.get('mName')
    moID = data_dict.get('moID')
    amount = data_dict.get('amount')
    target_object = MaterialInfo.objects.get(mName = mName)
    unit = target_object.unit
    price = target_object.price1
    mID = target_object.mID
    
    to_return = {
        'unit':unit,
        'price':price,
        'moID':moID,
        'mID':mID,
        'mName':mName,
        'amount':amount
    }
    rep = JsonResponse(to_return, safe = False)
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
    all_data = list(MaterialOrderDetail.objects.filter(moID = moID).values())
    repackage_data_list = []
    for item in all_data:
        mID = item['mID_id']
        moID = item['moID_id']
        amount = item['amount']
        mState = 0
        print(mID,moID,mState)
        target = MaterialStock(mID = mID,moID = moID, mState = mState, arrival= datetime.datetime.now(), stock = amount)
        target.save()
        new_data = {
            'mID':mID,
            'moID':moID,
            'amount':amount,
            'unit':item['unit'],
            'price':item['price'],
            'mName':MaterialInfo.objects.get(pk = mID).mName
        }
        repackage_data_list.append(new_data)
    # url = None
    # res = requests.post(url, data = repackage_data_list)
    rep = HttpResponse("Successfully modify the new data. ")
    return rep
    
def korder(request):
    all_data = list(KitchenOrder.objects.all().values())
    rep = JsonResponse(all_data, safe = False)
    return rep

def korder_detail(request):
    order_id = request.GET.get('order_id')
    all_data = KitchenOrderDetails.objects.filter(order_id = order_id).values()
    rep = JsonResponse(all_data, safe = False)
    return rep    

def material(request):
    all_material = MaterialInfo.objects.all().values()
    id2name = {}
    id2unit = {}
    for item in all_material:
        _id = item['mID']
        name = item['mName']
        unit = item['unit']
        id2name[_id] = name
        id2unit[_id] = unit
    name2id = {k:v for v,k in id2name.items()}
    name2num = {}
    for _id, name in id2name.items():
        name2num[name] = 0
        filtered_stock = MaterialStock.objects.filter(mID = _id)
        total_num = 0
        for item in filtered_stock:
            state = item['mState']
            stock_num = item['stock']
            if state == 0:
                total_num += stock_num
        name2num[name] = total_num
    to_return = []
    for _id, name in id2name.items():
        data_dict = {}
        unit = id2unit[_id]
        data_dict['ingredient_name'] = name + '（' + unit + '）'
        data_dict['ingredient_number'] = str(name2num[name])
        to_return.append(data_dict)
    
    url = None
    res = requests.post(url, data = to_return)
    return HttpResponse("successfully send the result! ")

def xml_to_dict(request):
    jsonstr = xmltodict.parse(request)
    jsonstr = json.dumps(jsonstr)
    return json.loads(jsonstr)['root']

def confirm_order_scm(request):
    data_dict = xml_to_dict(request.body)
    order_id = data_dict['order_id']
    order_type = data_dict['order_type']
    material_item_list = data_dict['raw_material']
    if order_type == 0:
        error = False
        to_return = {}
        to_return['order_id'] = order_id
        to_return['order_type'] = order_type
        to_return['raw_material'] = []
        for item in material_item_list:
            ingredient_name = ' '.join(item['ingredient_name'].split('（')[:-1])
            ingredient_number = item['ingredient_number']
            ordered_stock_set = MaterialStock.objects.filter(mName = ingredient_name).order_by('arrival').values()
            flag = True

            material_info_obj = MaterialInfo.objects.get(mName = ingredient_name)
            ##传给杨泽远
            data_dict = {}
            data_dict['mID'] = mID
            data_dict['mName'] = ingredient_name
            data_dict['amount'] = ingredient_number
            data_dict['unit'] = material_info_obj.unit
            data_dict['price'] = material_info_obj.price
            to_return['raw_material'].append(data_dict)


            for i in range(len(ordered_stock_set)):
                stock_item = ordered_stock_set[i]
                state = stock_item['mState']
                stock = stock_item['stock']
                moID = stock_item['moID']
                mID = stock_item['mID']
                _id = stock_item['id']


                
                if state != 0:
                    if i == len(ordered_stock_set) - 1:
                        flag = False
                    continue

                target_object = MaterialStock.objects.get(moID = moID, mID = mID, mState = mState)

                if ingredient_number <= stock:
                    target_object.stock -= ingredient_number
                    if target_object.stock == 0:
                        target_object.mState = 1
                    break
                else:
                    if i == len(ordered_stock_set) - 1:
                        flag = False
                    target_object.stock = 0
                    ingredient_number -= stock
                    target_object.mState = 1

            if not flag:
                error = True
                break
        if error:
            return HttpResponse("Fail! Not enough ingredients!")
        else:
            url = None
            res = requests.post(url, data = to_return)
            return HttpResponse("success !  ")


    else:
        error = False
        all_record = []
        for item in material_item_list:
            ingredient_name = ' '.join(item['ingredient_name'].split('（')[:-1])
            ingredient_number = item['ingredient_number']
            ordered_stock_set = MaterialStock.objects.filter(mName = ingredient_name).order_by('arrival').values()
            flag = True

            for i in range(len(ordered_stock_set)):
                record_data = {}
                stock_item = ordered_stock_set[i]
                state = stock_item['mState']
                stock = stock_item['stock']
                moID = stock_item['moID']
                mID = stock_item['mID']
                _id = stock_item['id']
                if state != 0:
                    if i == len(ordered_stock_set) - 1:
                        flag = False
                    continue
                if ingredient_number <= stock:
                    target_object = MaterialStock.objects.get(moID = moID, mID = mID, mState = mState)
                    target_object.stock -= ingredient_number
                    
                    record_data['id'] = _id
                    record_data['decrease_num'] = ingredient_number
                    
                    if target_object.stock == 0:
                        target_object.mState = 1
                    break
                else:
                    if i == len(ordered_stock_set) - 1:
                        flag = False
                    target_object.stock = 0
                    ingredient_number -= stock
                    target_object.mState = 1

                    record_data['id'] = _id
                    record_data['decrease_num'] = stock

                all_record.append(record_data)

            if not flag:
                error = True
                break
        if error:
            return HttpResponse("Fail! Not enough ingredients!")
        if not os.path.exists('rollback_dir/'):
            os.path.mkdir('rollback_dir/')
        f = open('rollback_dir/rollback_log.txt','a',encoding = 'utf-8')
        log_data = {
                        'order_id':order_id,
                        'material_data':all_record
                    }
        print(all_record, file = f)
        f.close()
        return HttpResponse("success !  ")
        
def confirm_takeout_scm(request):
    data_dict = xml_to_dict(request.body)
    order_id = data_dict['order_id']
    order_type = data_dict['action']
    material_item_list = data_dict['raw_material']
    if order_type == 0:
        to_return = {}
        to_return['order_id'] = order_id
        to_return['order_type'] = order_type
        to_return['raw_material'] = []
        for item in material_item_list:
            ingredient_name = ' '.join(item['ingredient_name'].split('（')[:-1])
            ingredient_number = item['ingredient_number']
            ordered_stock_set = MaterialStock.objects.filter(mName = ingredient_name).order_by('arrival').values()
            flag = True

            material_info_obj = MaterialInfo.objects.get(mName = ingredient_name)
            ##传给杨泽远
            data_dict = {}
            data_dict['mID'] = mID
            data_dict['mName'] = ingredient_name
            data_dict['amount'] = ingredient_number
            data_dict['unit'] = material_info_obj.unit
            data_dict['price'] = material_info_obj.price
            to_return['raw_material'].append(data_dict)
        url = None
        res = requests.post(url, data = to_return)
        return HttpResponse("success! ")
    new_record_list = []
    with open('rollback_dir/rollback_log.txt','r',encoding = 'utf-8') as f:
        for line in f:
            item = eval(line.strip())
            stored_id = item['order_id']
            if stored_id != order_id:
                new_record_list.append(item)
                continue
            all_data = item['material_data']
            for data in all_data:
                prim_id = data['id']
                increase_num = data['decrease_num']
                obj = MaterialStock.objects.get(id = prim_id)
                obj.mState = 0
                obj.stock += increase_num
            
    with open('rollback_dir/rollback_log.txt','w',encoding = 'utf-8') as f:
        print(new_record_list,file = f)
    return HttpResponse("success! ")
