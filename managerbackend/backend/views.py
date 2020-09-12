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

silence_list = ['mysql.infoschema', 'mysql.session', 'mysql.sys']
silence_list2 = [
        'auth_group', 'auth_group_permissions', 'auth_permission', 'auth_user',
        'auth_user_groups', 'auth_user_user_permissions', 'columns_priv', 'component',
        'db', 'default_roles', 'django_admin_log', 'django_content_type',
        'django_migrations', 'engine_cost', 'func', 'general_log',
        'global_grants', 'gtid_executed', 'help_category', 'help_keyword',
        'help_relation', 'help_topic', 'innodb_index_stats', 'innodb_table_stats',
        'password_history', 'plugin', 'procs_priv', 'proxies_priv', 'role_edges',
        'server_cost', 'servers', 'slave_master_info', 'slave_relay_log_info', 'slave_worker_info',
        'slow_log', 'tables_priv', 'time_zone', 'time_zone_leap_second', 'time_zone_name', 'time_zone_transition',
        'time_zone_transition_type', 'user'
    ]

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



def info_global(request): # ok
    alldata = list(User.objects.all().values())
    alldata_list = correct_list(alldata)
    for item in alldata_list:
        if item['user'] in silence_list:
            alldata_list.remove(item)
    rep = JsonResponse(alldata_list, safe=False)

    return rep


def info_global_search(request): # ok
    data_dict = request.POST
    username = data_dict.get('searchUser')
    alldata = list(User.objects.filter(user__contains=username).values())
    alldata_list = correct_list(alldata)
    for item in alldata_list:
        if item['user'] in silence_list:
            alldata_list.remove(item)
    rep = JsonResponse(alldata_list, safe=False)

    return rep


def global_priv(request): # ok
    conn = pymysql.connect(
        host='localhost',
        user='root', password='123',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    data_dict = request.POST
    user = data_dict.get('user')
    grant = ""
    revoke = ""
    if data_dict.get('all') == 'Y':
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
        if param[i] == 'Y':
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


#################


def info_user(request): # ok
    alldata = list(User.objects.all().values())
    alldata_list = correct_list(alldata)
    for item in alldata_list:
        if item['user'] in silence_list:
            alldata_list.remove(item)
    rep = JsonResponse(alldata_list, safe=False)

    return rep


def info_user_search(request): # ok
    data_dict = request.POST
    username = data_dict.get('searchUser')
    alldata = list(User.objects.filter(user__contains=username).values())
    alldata_list = correct_list(alldata)
    for item in alldata_list:
        if item['user'] in silence_list:
            alldata_list.remove(item)
    rep = JsonResponse(alldata_list, safe=False)

    return rep


def alter_lock(request): # ok
    data_dict = request.POST
    username = data_dict.get('user')
    conn = pymysql.connect(
            host='localhost',
            user='root', password='123',
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


def pswd_change(request): # ok
    data_dict = request.POST
    username = data_dict.get('user')
    newpwd = data_dict.get('pswd')

    conn = pymysql.connect(
        host='localhost',
        user='root', password='123',
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


def create_user(request): # ok
    data_dict = request.POST
    username = data_dict.get('user')
    pswd = data_dict.get('pswd')

    conn = pymysql.connect(
        host='localhost',
        user='root', password='123',
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


##################

def check_global(user):
    alldata = list(User.objects.filter(user=user).values())
    for item in alldata:
        result = [item["select_priv"],item["insert_priv"],item["update_priv"],item["delete_priv"],item["drop_priv"]]
    return result

def check_local(user, table, cursor):
    method = "select * from tables_priv where user='{}' and table_name = '{}';"
    sql = method.format(user, table)
    cursor.execute(sql)
    data = cursor.fetchall()
    result = ['N', 'N', 'N', 'N', 'N']
    if data == ():
        return result
    priv = data[0][6]
    checklist = ['Select', 'insert', 'Update', 'Delete', 'Drop']
    for i in range(len(checklist)):
        if checklist[i] in priv:
            result[i] = 'Y'
    return result



def info_table(request): # ok
    conn = pymysql.connect(
        host='localhost',
        user='root', password='123',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()

    alldata1 = list(User.objects.all().values())
    sql = "show tables;"
    cursor.execute(sql)
    alldata2 = cursor.fetchall()

    arr = []
    for item in alldata1:
        if item["user"] not in silence_list:
            for jtem in alldata2:
                if jtem[0] not in silence_list2:
                    global_info = check_global(item["user"])
                    local_info = check_local(item["user"],jtem[0],cursor)
                    info = ['Y','Y','Y','Y','Y']
                    for i in range(len(global_info)):
                        if global_info[i] == 'N' and local_info[i] == 'N':
                            info[i] = 'N'

                    content = {'user': item["user"],'table': jtem[0],'Select':info[0],
                               'insert':info[1], 'Update':info[2],
                               'Delete':info[3], 'Drop': info[4]
                               }
                    arr.append(content)
    cursor.close()
    conn.close()

    return JsonResponse(arr, safe=False)


def search_part_priv(request):
    data_dict = request.POST
    user = data_dict.get('searchUser')
    table = data_dict.get('searchTable')

    conn = pymysql.connect(
        host='localhost',
        user='root', password='123',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()

    alldata1 = list(User.objects.filter(user__contains=user).values())
    sql = "show tables;"
    cursor.execute(sql)
    alldata2 = cursor.fetchall()
    
    arr = []
    for item in alldata1:
        if item["user"] not in silence_list:
            for jtem in alldata2:
                if jtem[0] not in silence_list2 and table in jtem[0]:
                    global_info = check_global(item["user"])
                    local_info = check_local(item["user"], jtem[0], cursor)
                    info = ['Y','Y','Y','Y','Y']
                    for i in range(len(global_info)):
                        if global_info[i] == 'N' and local_info[i] == 'N':
                            info[i] = 'N'

                    content = {'user': item["user"], 'table': jtem[0], 'Select': info[0],
                               'insert': info[1], 'Update': info[2],
                               'Delete': info[3], 'Drop': info[4]
                               }
                    arr.append(content)
    cursor.close()
    conn.close()

    return JsonResponse(arr, safe=False)


def local_priv(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', password='123',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    data_dict = request.POST
    user = data_dict.get('user')
    table = data_dict.get('table')

    grant = ""
    revoke = ""
    if data_dict.get('all') == 'Y':
        method = 'grant all on *.* to {};'
        sql = method.format(user)
        cursor.execute(sql)
        rep = HttpResponse("Succeed!")
        return rep

    param = [data_dict.get('Select'),data_dict.get('Update'),
             data_dict.get('Delete'),data_dict.get('insert'),
             data_dict.get('Drop')]
    priv = [',select', ',update',',delete',',insert',',drop']
    for i in range(len(param)):
        if param[i] == 'Y':
            grant = grant + priv[i]
        else:
            revoke = revoke + priv[i]

    if grant != '':
        method = 'grant {} on mysql.{} to {};'
        sql = method.format(grant[1:], table, user)
        cursor.execute(sql)

    if revoke != '':
        method = 'revoke {} on mysql.{} from {};'
        sql = method.format(revoke[1:], table, user)
        cursor.execute(sql)

    cursor.close()
    conn.close()
    rep = HttpResponse("Succeed!")
    return rep


def show_table(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', password='123',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    sql = "show tables;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    arr = []
    for i in data:
        if i[0] not in silence_list2:
            arr.append(i[0])
    return JsonResponse(arr, safe=False)


def show_user(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', password='123',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT User FROM mysql.user;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    arr = []
    for i in data:
        if i[0] not in silence_list:
            arr.append(i[0])
    return JsonResponse(arr, safe=False)



