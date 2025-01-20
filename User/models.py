from django.db import models
from itemseller . models import product_upload_tbl
from itemseller . models import Itemseller_reg_tbl
from datetime import datetime, timedelta
from Event.models import Event_manager_tbl,Event_reg_tbl
from Academy.models import Academy_reg_tbl
from Turf . models import turf_reg_tbl


# Create your models here.

class User_regtbl(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    mob = models.IntegerField()
    ag = models.IntegerField()
    ad = models.TextField()
    gn = models.CharField(max_length=10)
    eml = models.EmailField(unique=True)
    ps1 = models.CharField(max_length=25)
    ps2 = models.CharField(max_length=25)
class add_to_cart_table(models.Model):
      product = models.ForeignKey(product_upload_tbl, on_delete=models.CASCADE)
      userid = models.IntegerField()
      proid=models.IntegerField()

class Booking(models.Model):
    user=models.ForeignKey(User_regtbl,on_delete=models.SET_DEFAULT,default="this user account is deleted")
    product = models.ForeignKey(product_upload_tbl, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    Amount=models.IntegerField()
    order_date = models.DateTimeField(default=datetime.today())
    arrival_date = models.DateTimeField(default=datetime.today()+timedelta(7))
    status=models.CharField(max_length=15)
    Alt_phone=models.IntegerField()
    shipping_Address=models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.arrival_date:
            order=datetime.today()
            self.arrival_date = order+ timedelta(days=7)
        super(Booking, self).save(*args, **kwargs)
    class Meta:
        ordering = ['order_date']   
class complaint_reg_tbl(models.Model):
     book=models.ForeignKey(Booking,on_delete=models.SET_DEFAULT,default="this booking is deleted")
     seller= models.ForeignKey(Itemseller_reg_tbl, on_delete=models.CASCADE)
     complaint=models.TextField()
     cdate=models.DateTimeField(auto_now=True)
     cimage=models.FileField(upload_to="pictures")
     status=models.CharField(max_length=100)
class book_event_tbl(models.Model):
    event=models.ForeignKey(Event_reg_tbl, on_delete=models.CASCADE)
    audient=models.ForeignKey(User_regtbl,on_delete=models.SET_DEFAULT,default="this user account is deleted")
    ticketno=models.IntegerField()
    amount=models.IntegerField()
    bookingdate=models.DateTimeField(default=datetime.today())
    status=models.CharField(max_length=15,default="notpaid")
class Academy_admission_tbl(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    mob = models.IntegerField()
    ag = models.IntegerField()
    ad = models.TextField()
    gn = models.CharField(max_length=10)
    eml = models.EmailField()
    date=models.DateTimeField(default=datetime.today())
    academy=models.ForeignKey(Academy_reg_tbl,on_delete=models.CASCADE)
    user=models.ForeignKey(User_regtbl,on_delete=models.CASCADE)
class posts_tbl(models.Model):
    pimg=models.FileField(upload_to="pictures")
    Pcaption=models.TextField(default="nocaption")
    user=models.ForeignKey(User_regtbl,on_delete=models.CASCADE)
class comments_tbl(models.Model):
    user=models.ForeignKey(User_regtbl,on_delete=models.CASCADE)
    post=models.ForeignKey(posts_tbl,on_delete=models.CASCADE)
    comment=models.TextField(default="nocomments")
class turf_booking_tbl(models.Model):
    sid=models.IntegerField()
    user=models.ForeignKey(User_regtbl,on_delete=models.SET_DEFAULT,default="this user account is deleted")
    turf=models.ForeignKey(turf_reg_tbl,on_delete=models.CASCADE)
    tdate=models.DateTimeField(default=datetime.today())
    bdate=models.DateField()
    stime=models.TimeField()
    etime=models.TimeField()
    amount=models.IntegerField()
    status=models.CharField(max_length=25,default="unpaid")








    
    