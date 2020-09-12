from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='index0'),
    path('db/', views.info_global, name='index1'),
    path('db/search/', views.info_global_search, name='index2'),
    path('db/priv/', views.global_priv, name='index2_1'),
    path('user/', views.info_user, name='index3'),
    path('user/search/', views.info_user_search, name='index4'),
    path('user/lock/', views.alter_lock, name='index5'),
    path('user/create/', views.create_user, name='index6'),
    path('user/pswd/', views.pswd_change, name='index7'),
    path('table/', views.info_table, name='index8'),
    path('table/search/', views.search_part_priv, name='index9'),
    path('table/priv/', views.local_priv, name='index10'),
]