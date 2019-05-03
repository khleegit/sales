from django.urls import path
from . import views


urlpatterns = [
	path('', views.login, name='login'),
	path('home/', views.index, name='index'),
	path('payment/', views.payment, name='payment'),
	path('card_pm/', views.card_pm, name='card_pm'),
	path('card_pm_ol/', views.card_pm_ol, name='card_pm_ol'),
	path('vir_acc/', views.vir_acc, name='vir_acc'),
	path('acc_tran/', views.acc_tran, name='acc_tran'),
	path('ceph_pm/', views.ceph_pm, name='ceph_pm'),
	path('cash_pm/', views.cash_pm, name='cash_pm'),
	path('cash_pm_ol/', views.cash_pm_ol, name='cash_pm_ol'),
	path('card_plm/', views.card_plm, name='card_plm'),
	path('test/', views.test, name='test'),
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]