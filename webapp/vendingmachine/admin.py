from django.contrib import admin
from .models import Items, Transaction

@admin.register(Items)
class itemAdim(admin.ModelAdmin) :
    list_display=("item_id","item_name","price","quantity")

@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin) :
    list_display = ("item_name","quantity","money_inserted","total_cost","change","date")



