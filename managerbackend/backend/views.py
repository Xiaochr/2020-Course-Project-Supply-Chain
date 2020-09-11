from django.shortcuts import HttpResponse, render, redirect
from .models import *
from django.http import JsonResponse
import pymysql
import json
# conn = pymysql.connect(
#         host='localhost',
#         user ='root', password ='xcr991004',
#         database ='mysql',
#         charset ='utf8')



def correct(dict_obj):
    for k,v in dict_obj.items():
        if isinstance(v, bytes):
            dict_obj[k] = str(v)
    return dict_obj

def correct_list(list_obj):
    new_list = []
    for dict_item in list_obj:
        new_list.append(correct(dict_item))
    return new_list

def login(request):
    data_dict = request.POST
    pswd = data_dict.get('pswd')
    return True if pswd == "test" else False
    '''
    error_msg = ""
    if request.method == "POST":
        pwd = request.POST.get("pswd", None)

        if pwd == 'test':
            return redirect("/terminal/")
        else:
            error_msg = "密钥错误"

    return render(request,"login.html",{"error":error_msg})
    '''

def info_global(request):
    alldata = list(User.objects.all().values())
    alldata_list = correct_list(alldata)
    rep = JsonResponse(alldata_list, safe=False)

    return rep


def info_global_search(request):
    data_dict = request.POST
    username = data_dict.get('searchUser')
    alldata = list(User.objects.filter(user__contains=username).values())
    alldata_list = correct_list(alldata)
    rep = JsonResponse(alldata_list, safe=False)

    return rep


def info_user(request):
    alldata = list(User.objects.all().values())
    alldata_list = correct_list(alldata)
    rep = JsonResponse(alldata_list, safe=False)

    return rep


def info_user_search(request):
    data_dict = request.POST
    username = data_dict.get('searchUser')
    alldata = list(User.objects.filter(user__contains=username).values())
    alldata_list = correct_list(alldata)
    rep = JsonResponse(alldata_list, safe=False)

    return rep


def alter_lock(request):
    data_dict = request.POST
    username = data_dict.get('user')
    conn = pymysql.connect(
            host='localhost',
            user='root', password='YES',
            database='mysql',
            charset='utf8')
    cursor = conn.cursor()
    method = "select account_locked from user where user='{}';"
    sql = method.format(username)
    cursor.execute(sql)
    data = cursor.fetchall()


    lock_method = "alter user {} account lock;"
    unlock_method = "alter user {} account unlock;"
    if data[0][0] == 'N':
        method = lock_method
    else:
        method = unlock_method
    sql = method.format(username)
    cursor.execute(sql)
    cursor.close()
    conn.close()

    rep = HttpResponse("Succeed!")
    return rep


def pswd_change(request):
    data_dict = request.POST
    username = data_dict.get('user')
    newpwd = data_dict.get('pswd')


    conn = pymysql.connect(
        host='localhost',
        user='root', password='YES',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = "alter user '{}'@'%' identified by '{}';"
    sql = method.format(username,newpwd)
    cursor.execute(sql)
    cursor.close()
    conn.close()
    rep = HttpResponse("Succeed!")
    return rep


def create_user(request):
    data_dict = request.POST
    username = data_dict.get('user_name')
    pswd = data_dict.get('pswd')

    conn = pymysql.connect(
        host='localhost',
        user='root', password='YES',
        database='mysql',
        charset='utf8'
        )
    cursor = conn.cursor()
    method = "CREATE USER  '{}' @'%'  IDENTIFIED BY '{}';"
    sql = method.format(username, pswd)
    cursor.execute(sql)
    cursor.close()
    conn.close()
    rep = HttpResponse("Succeed!")
    return rep


def global_priv(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', password='YES',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    data_dict = request.POST
    user = data_dict.get('user_name')
    grant = ""
    revoke = ""
    if data_dict.get('all') == 1:
        method = 'grant all on *.* to {};'
        sql = method.format(user)
        cursor.execute(sql)
        rep = HttpResponse("Succeed!")
        return rep

    param = [data_dict.get('select_priv'),data_dict.get('update_priv'),
             data_dict.get('delete_priv'),data_dict.get('create_priv'),
             data_dict.get('drop_priv'),data_dict.get('trigger_priv')]
    priv = [',select', ',update',',delete',',create',',drop',',trigger']
    for i in range(len(param)):
        if param[i] == 1:
            grant = grant + priv[i]
        else:
            revoke = revoke + priv[i]

    if grant != '':
        method = 'grant {} on *.* to {};'
        sql = method.format(grant[1:],user)
        cursor.execute(sql)

    if revoke != '':
        method = 'revoke {} on *.* from {};'
        sql = method.format(revoke[1:],user)
        cursor.execute(sql)

    cursor.close()
    conn.close()
    rep = HttpResponse("Succeed!")
    return rep




