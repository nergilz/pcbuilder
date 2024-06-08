
from django.urls import path
from . import views

app_name = 'shop'   # app name

# pattern for the index page, all products and each product
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.get_all_products, name='get_all_products'),
    path('contacts/', views.get_contacts, name='get_contacts'),

]