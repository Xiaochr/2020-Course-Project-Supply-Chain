from django.urls import path

from . import views

urlpatterns = [
    path('info/', views.info, name='index0'),
    path('info/add/', views.info_add, name='index1'),
    path('info/del/', views.info_del, name='index2'),
    path('info/edit/', views.info_edit, name='index3'),
    path('info/search/', views.info_search, name='index4'),
    path('stock/', views.stock, name='index5'),
    path('stock/add/', views.stock_add, name='index5.1'),
    path('stock/search/', views.stock_search, name='index6'),
    path('stock/filter/', views.stock_filter, name='index7'),
    path('stock/count/', views.stock_count, name='index8'),
    path('stock/send/', views.stock_send, name='index9'),
    path('morder/', views.morder, name='index10'),
    path('morder/add/', views.morder_add, name='index10.1'),
    path('morder/detail/', views.morder_detail, name='index10.2'),
    path('morder/detail/add/', views.morder_detail_add, name='index10.3'),
    path('morder/filter/', views.morder_filter, name='index10.4'),
    path('morder/stockin/', views.morder_stockin, name='index11'),
    path('korder/', views.korder, name='index12'),
    path('korder/detail/', views.korder_detail, name='index13'),
    path('material/', views.material, name='index14'),
    path('confirm_order_scm/', views.confirm_order_scm, name='index15'),
    path('confirm_takeout_scm/', views.material, name='index15'),
]