from django.urls import path
from . import views


urlpatterns = [
	path('', views.login, name='login'),
	path('home/', views.index, name='index'),
	path('card_pm/', views.card_pm, name='card_pm'),
	path('cash_pm/', views.cash_pm, name='cash_pm'),
	path('payment/', views.payment, name='payment'),
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]