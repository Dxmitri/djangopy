from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="vendingmachine"),
    path('buy/',views.buy, name= 'buy'),
    path('success/<int:item_id>/<int:quantity>/<str:total>/<str:change>/',views.success, name='success')
]