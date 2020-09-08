from django.shortcuts import HttpResponse, render, redirect
from .models import *
from django.http import JsonResponse
import pymysql
conn = pymysql.connect(
        host='localhost',
        user ='root', password ='12345',
        database ='mysql',
        charset ='utf8')


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


def terminal(request):
    return render(request, "terminal.html")


def wholedb(request):

    alldata = list(User.objects.all().values())

    arr = []
    for item in alldata:
        content = {'用户': item["user"], 'Select权限': item["select_priv"],'Update权限': item["update_priv"],
                   'Delete权限': item["delete_priv"], 'Create权限': item["create_priv"],'Drop权限': item["drop_priv"],
                    'Trigger权限': item["trigger_priv"],
                   }
        arr.append(content)
    return JsonResponse(arr, safe=False)

def account(request):
    alldata = list(User.objects.all().values())
    arr = []
    for item in alldata:
        content = {'用户': item["user"], '账户情况': item["account_locked"]}
        arr.append(content)
    return JsonResponse(arr, safe=False)


def table(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    sql = 'select * from tables_priv'
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    arr = []
    for i in data:
        content = {'用户': i[2], '数据库': i[1], '表名': i[3], '权限': i[6],}
        arr.append(content)
    return JsonResponse(arr,safe = False)

def priviledge_grant_totable(request):

    cursor = conn.cursor()
    method = 'grant {} on {} to {};'
    sql = method.format('insert','mysql.Persons','testoutsider')
    cursor.execute(sql)
    cursor.close()
    conn.close()

def priviledge_grant_toall(request):
    user = 'testn2'
    priv = "delete"
    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = 'grant {} on *.* to {};'
    sql = method.format(priv,user)
    print(sql)
    cursor.execute(sql)
    cursor.close()
    conn.close()


def priviledge_del(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = 'revoke {} on {} from {};'
    sql = method.format('insert', 'mysql.Persons', 'testoutsider')
    cursor.execute(sql)
    cursor.close()
    conn.close()

def priviledge_revoke_toall(request):
    user = 'testn2'
    priv = "delete"
    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = 'revoke {} on *.* from {};'
    sql = method.format(priv,user)
    print(sql)
    cursor.execute(sql)
    cursor.close()
    conn.close()

def create_user(request):
    username = 'testn2'
    pwd = '123456'

    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = "CREATE USER  '{}' @'%'  IDENTIFIED BY '{}';"
    sql = method.format(username, pwd)
    cursor.execute(sql)
    cursor.close()
    conn.close()

def lock_user(request):
    username = 'testn2'

    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = "alter user {} account lock;"
    sql = method.format(username)
    cursor.execute(sql)
    cursor.close()
    conn.close()

def unlock_user(request):
    username = 'testn2'

    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = "alter user {} account unlock;"
    sql = method.format(username)
    cursor.execute(sql)
    cursor.close()
    conn.close()

def passwd_change(request):
    username = 'testn2'
    newpwd = '123456'

    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = "alter user '{}'@'%' identified by '{}';"
    sql = method.format(username,newpwd)
    cursor.execute(sql)
    cursor.close()
    conn.close()

def info_search(request):
    user = 'testoutsider'
    table = 'persons'

    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    method = "select * from tables_priv where user='{}' and table_name = '{}';"
    sql = method.format(user, table)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    arr = []
    for i in data:
        content = {'用户': i[2], '数据库': i[1], '表名': i[3], '权限': i[6], }
        arr.append(content)
    return JsonResponse(arr, safe=False)

def show_table(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    sql = "show tables;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    silence_list = [
        'auth_group','auth_group_permissions','auth_permission','auth_user',
        'auth_user_groups','auth_user_user_permissions','columns_priv','component',
        'db','default_roles','django_admin_log','django_content_type',
        'django_migrations','engine_cost','func','general_log',
        'global_grants','gtid_executed','help_category','help_keyword',
        'help_relation','help_topic','innodb_index_stats','innodb_table_stats',
        'password_history','plugin','procs_priv','proxies_priv','role_edges',
        'server_cost','servers','slave_master_info','slave_relay_log_info','slave_worker_info',
        'slow_log','tables_priv','time_zone','time_zone_leap_second','time_zone_name','time_zone_transition',
        'time_zone_transition_type','user'
    ]
    arr = []
    for i in data:
        if i[0] not in silence_list:
            content = {'表名': i[0],}
            arr.append(content)
    return JsonResponse(arr, safe=False)

def show_user(request):
    conn = pymysql.connect(
        host='localhost',
        user='root', password='12345',
        database='mysql',
        charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT User, Host FROM mysql.user;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    arr = []
    for i in data:
        content = {'用户名': i[0], 'Host':i[1] }
        arr.append(content)
    return JsonResponse(arr, safe=False)


