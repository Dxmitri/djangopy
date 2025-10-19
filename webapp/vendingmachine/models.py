from django.db import models

class Items(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    price= models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self) :
        return self.item_name

class Transaction(models.Model) :
    item_name = models.ForeignKey(Items,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    money_inserted = models.IntegerField()
    total_cost = models.IntegerField()
    change = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction #{self.id} -Item ID:{self.item_name}"



