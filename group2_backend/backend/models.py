from django.db import models

# Create your models here.
class MaterialInfo(models.Model):
    mID = models.CharField(max_length=10, primary_key=True)
    mName = models.CharField(max_length=10)
    mType = models.CharField(max_length=10)
    price1 = models.FloatField()
    price2 = models.FloatField()
    price3 = models.FloatField()
    unit = models.CharField(max_length=10)
    safetyType = models.IntegerField()
    outType = models.IntegerField()
    shelfLife = models.IntegerField()

class MaterialStock(models.Model):
    moID = models.CharField(max_length=10)
    mID = models.CharField(max_length=10)
    mName = models.CharField(max_length=10)
    arrival = models.DateField(auto_now= True)
    stock = models.IntegerField()
    mState = models.IntegerField()
    class Meta:
        unique_together = ("moID", "mID", "mState")

class MaterialOrder(models.Model):
    moID = models.CharField(max_length=10, primary_key=True)
    oDate = models.DateField(auto_now= True)
    aDate = models.DateField(auto_now= True)
    moState = models.IntegerField()

class MaterialOrderDetail(models.Model):
    moID = models.ForeignKey('MaterialOrder', on_delete=models.CASCADE)
    mID = models.ForeignKey('MaterialInfo', on_delete=models.CASCADE)
    amount = models.IntegerField()
    unit = models.CharField(max_length=10)
    price = models.FloatField()

class KitchenOrder(models.Model):
    order_id = models.CharField(max_length=10, primary_key=True)
    order_type = models.CharField(max_length=10)
    koState = models.IntegerField()

class KitchenOrderDetail(models.Model):
    order_id = models.ForeignKey('KitchenOrder', on_delete=models.CASCADE)
    mID = models.ForeignKey('MaterialInfo', on_delete=models.CASCADE)
    mName = models.CharField(max_length=10)
    amount = models.FloatField()


