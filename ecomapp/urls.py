from django.urls import path
from django.urls import include
from ecomapp import views

urlpatterns = [
    path('',views.pro_index,name="pro_index"),
    path('<int:id>',views.product_detail, name="product_detail"),
    path('aa/<int:id>',views.brand_detail,name="brand_detail"),
    path('bb/<int:id>/',views.final_detail, name="final_detail"),
    path('cc/<int:cidd>/<int:kid>/',views.conclude_detail, name="conclude_detail"),

]
    
