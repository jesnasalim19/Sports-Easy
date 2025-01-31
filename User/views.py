from django.shortcuts import render,redirect
from . models import User_regtbl,complaint_reg_tbl
from itemseller . models import product_upload_tbl
from . models import add_to_cart_table,Academy_admission_tbl,posts_tbl
from .models import Booking
from django . contrib import messages
from datetime import datetime, timedelta,date,time
from django.utils import timezone
from itemseller . models import Itemseller_reg_tbl
from Event . models import Event_reg_tbl,Event_manager_tbl
from .models import book_event_tbl,comments_tbl,turf_booking_tbl
from Academy.models import Academy_reg_tbl
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"index.html")
def User_reg(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('Lname')
        mobile=request.POST.get('mob')
        eml=request.POST.get('email')
        Age=request.POST.get('Age')
        Gen=request.POST.get('Gender')
        Address=request.POST.get('Address')
        pas=request.POST.get('password')
        cpass=request.POST.get('c_password')
        if User_regtbl.objects.filter(eml=eml).exists():
            messages.success(request, 'Another Account Has Similar Email Id')
            return render(request,"user_reg.html")
        else:
          obj=User_regtbl.objects.create( fname=fname,lname=lname,mob=mobile,ag=Age,ad=Address,gn=Gen,eml=eml,ps1=pas,ps2=cpass)
          obj.save()
          if obj:
            return render(request,"User_login.html")
          else:
            return render(request,"user_reg.html")
    else:
        return render(request,"user_reg.html")
def User_login(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        obj=User_regtbl.objects.filter(eml=eml,ps1=psw)
        if obj:
            for l in obj:
                uid=l.id
                request.session['uid']=uid
            return render(request,"User_home.html")
        else:
            return render(request,"User_login.html")
    else:
        return render(request,"User_login.html")
def sports_items(request):
     mypro=product_upload_tbl.objects.filter(seller__Approve=True)
     return render(request,"User_sports_items.html",{"view":mypro}) 
def  add_to_cart(request):
    uid=request.session['uid']
    proid=request.GET.get('idn')
    mypro=product_upload_tbl.objects.get(id=proid)
    obj1=add_to_cart_table.objects.filter(proid=proid,userid=uid)
    if obj1:
        messages.success(request, 'product already in cart')
        return redirect("/sports_items")
    else:
        obj=add_to_cart_table.objects.create(product=mypro,userid=uid,proid=proid)
        obj.save()
        if obj:
         messages.success(request, 'Item Added to cart')
         return redirect("/sports_items")
        else:
         messages.success(request, 'Added to cart')
         return redirect("/sports_items")
def cart_view(request):
    uid=request.session['uid']
    mycart=add_to_cart_table.objects.filter(userid=uid)
    return render(request,"Carted_items.html",{"cart":mycart})
def remove_from_cart(request):
    cid=request.GET.get('idn')
    obj=add_to_cart_table.objects.filter(id=cid)
    obj.delete()
    return redirect("/cart_view")
def booking(request):
    pid=request.GET.get('idn')
    uid=request.session['uid']
    status=request.GET.get('status')
    if status!="out of stock" :
       obj=product_upload_tbl.objects.filter(id=pid)
       obj1=User_regtbl.objects.filter(id=uid)
       return render(request,"User_booking.html",{"pro":obj,"use":obj1})
    else:
        messages.success(request, 'product is out of stock')
        return redirect("/sports_items")

def Save_booking(request):
    uid=request.session['uid']
    if request.method=="POST":
        Altnumber=request.POST.get('altphone')
        Qty=request.POST.get('quantity')
        Amount=request.POST.get('amount')
        pid=request.POST.get('proid')
        Saddress=request.POST.get('shipaddress')
        mypro=product_upload_tbl.objects.get(id=pid)
        use=User_regtbl.objects.get(id=uid)
        obj=Booking.objects.create(Alt_phone=Altnumber,quantity=Qty,Amount=Amount,shipping_Address=Saddress,status="notsuccess",user=use,product=mypro)
        obj.save()
    
        if obj:
            return render(request,"payment.html",{"book":obj})
        else:
            redirect("/booking")
    else:
        redirect("/booking")
def payment(request):
    bid=request.GET.get('idn')
    obj=Booking.objects.get(id=bid)
    obj.status="booking success"
    obj.save()
    messages.success(request, 'Booking Successfull')
    return redirect("/sports_items")
def my_order(request):
    uid=request.session['uid']
    use=User_regtbl.objects.get(id=uid)
    obj=Booking.objects.filter(user=use).exclude(status="notsuccess")
    if obj:
        return render(request,"User_myorder.html",{"view":obj})
    else:
        return redirect("/sports_items")
def cancel_booking_sports_item(request):
    bid=request.GET.get('idn')
    obj=Booking.objects.get(id=bid)
    if(obj.arrival_date <= timezone.make_aware(datetime.now()) and obj.status=="delivered"):
             messages.success(request, 'Not Possible To Cancel')
             return redirect("/my_order")
    else:
        obj.delete()
        messages.success(request, 'Booking Cancelled')
        return redirect("/my_order")
def complaint_reg_view(request):
    bid=request.GET.get('idn')
    obj=Booking.objects.filter(id=bid)
    if obj:
        return render(request,"Complaint_reg.html",{"view":obj})
    else:
        return redirect("/my_order")

def save_complaint(request):
    if request.method=="POST":
        complain=request.POST.get('complaint')
        ccimage=request.FILES.get('cimage')
        bid=request.POST.get('idn')
        obj=Booking.objects.get(id=bid)
        obj1=Itemseller_reg_tbl.objects.get(id=obj.product.sellerid)
        mycom=complaint_reg_tbl.objects.create(complaint=complain,cimage=ccimage,book=obj,seller=obj1,status="notsolved")
        mycom.save()
        if mycom:
             messages.success(request, 'complaint registered please wait for our reply')
             return redirect("/my_order")
        else:
            return render("/cart_view")
    else:
        return redirect("/my_order")
def complaint_view(request):
    uid=request.session['uid']
    obj=User_regtbl.objects.get(id=uid)
    mycom=complaint_reg_tbl.objects.filter(book__user=obj)
    if mycom:
        return render(request,"User_complaint.html",{"view":mycom})
    else:
        return redirect("/my_order")
def user_home_view(request):
    return render(request,"User_home.html")
def Event_view(request):
    today=datetime.today()
    obj=Event_reg_tbl.objects.filter(edate__gte=today,em__Approve=True)
    if obj:
       return render(request,"User_Event_view.html",{"view":obj})
    else:
        return redirect("/user_home_view")
def event_book(request):
    uid=request.session['uid']
    if request.method=="POST":
        eid=request.POST.get('eid')
        noticket=request.POST.get('ticketno')
        ticketam=request.POST.get('tm')
        amount= int(noticket)*int(ticketam)
        event=Event_reg_tbl.objects.get(id=eid)
        userob=User_regtbl.objects.get(id=uid)
        if (int(noticket)<=event.avl_tickets):
          obj=book_event_tbl.objects.create(event=event,audient=userob,ticketno=noticket,amount=amount)
          obj.save()
          if obj:
            return render(request,"Event_payment.html",{"book":obj})
        else:
            messages.success(request,'no tickets available')
            return redirect("/Event_view")
    else:
        return redirect("/Event_view")
def Event_pay_submit(request):
    if request.method=="POST":
        bid=request.POST.get('idn')
        ticketno=request.POST.get('tn')
        obj=book_event_tbl.objects.get(id=bid)
        even=Event_reg_tbl.objects.get(id=obj.event.id)
        if obj:
            if (int(ticketno)<=even.avl_tickets):
              obj.status="payed"
              obj.save()
              even.avl_tickets=even.avl_tickets-int(ticketno)
              even.save()
              messages.success(request,'Booking success')
              return redirect("/Event_view")
            else:
                messages.success(request,'no tickets available')
                return redirect("/Event_view")

        else:
            messages.success(request,'Something went wrong')
            return redirect("/Event_view")
def event_mybooking_view(request):
    uid=request.session['uid']
    obj=book_event_tbl.objects.filter(audient__id=uid,status="payed")
    if obj:
        return render(request,"User_event_my_booking.html",{"view":obj})
    else:
        messages.success(request,'no bookings')
        return redirect("/Event_view")
def event_search(request):
    today=datetime.today()
    if request.method=="POST":
        dist=request.POST.get('dist')
        obj=Event_reg_tbl.objects.filter(dist=dist,edate__gte=today)
        if obj:
            return render(request,"User_event_search_view.html",{"view":obj})
        else:
             return redirect("/Event_view")
def User_academy_view(request):
    obj=Academy_reg_tbl.objects.filter(Approve=True)
    if obj:
        return render(request,"User_Academy_view.html",{"view":obj})
    else:
        return render(request,"User_home.html")
def Admission_form_view(request):
    aid=request.GET.get('idn')
    status=request.GET.get('status')
    if status=="seat available":
      return render(request,"User_addmission_form.html",{"view":aid})
    else:
        messages.success(request,'seat not available')
        return redirect("/User_academy_view")
def User_academy_admission(request):
    uid=request.session['uid']
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('Lname')
        mobile=request.POST.get('mob')
        eml=request.POST.get('email')
        Age=request.POST.get('Age')
        Gen=request.POST.get('Gender')
        Address=request.POST.get('Address')
        aid=request.POST.get('aid')
        user=User_regtbl.objects.get(id=uid)
        academy=Academy_reg_tbl.objects.get(id=aid)
        obj=Academy_admission_tbl.objects.create(fname=fname,lname=lname,mob=mobile,ag=Age,ad=Address,gn=Gen,eml=eml,academy=academy,user=user)
        if obj:
            messages.success(request,'Addmission Successfull Staff From Academy Contact Soon')
            return redirect("/User_academy_view")
        else:  
            messages.success(request,'Addmission Not Successfull Please try again')
            return redirect("/User_academy_view")
    else:
        return render(request,"User_addmission_form.html",{"view":aid})  
def academy_search(request):
    if request.method=="POST":
        dist=request.POST.get('dist')
        obj=Academy_reg_tbl.objects.filter(dist=dist)
        if obj:
            return render(request,"User_academy_search.html",{"view":obj})
        else:
            return redirect("/User_academy_view")
    else:
        return redirect("/User_academy_view")
def My_addmision_view(request):
    uid=request.session['uid']
    obj=Academy_admission_tbl.objects.filter(user__id=uid)
    if obj:
        return render(request,"User_my_Addmission.html",{"view":obj})
    else:
        messages.success(request,'Addmission Not Successfull Please try again')
        return redirect("/User_academy_view")
def post_view(request):
    obj=posts_tbl.objects.all()
    comment=comments_tbl.objects.all()
    if obj:
        return render(request,"post_view.html",{"view":obj,"cmnt":comment})
    else:
        messages.success(request,'no posts')
        return render(request,"User_home.html")

def make_post(request):
    uid=request.session['uid']
    if request.method=="POST":
        pimgs=request.FILES.get('pimg')
        content=request.POST.get('content')
        user=User_regtbl.objects.get(id=uid)
        obj=posts_tbl.objects.create(pimg=pimgs,Pcaption=content,user=user)
        obj.save()
        if obj:
            return redirect("/post_view")
        else:
            return render(request,"make_post.html")
    else:
        return render(request,"make_post.html")
def comment(request):
    uid=request.session['uid']
    if request.method=="POST":
        pid=request.POST.get('pid')
        comment=request.POST.get('comment')
        post=posts_tbl.objects.get(id=pid)
        user=User_regtbl.objects.get(id=uid)
        obj=comments_tbl.objects.create(user=user,comment=comment,post=post)
        if obj:
            return redirect("/post_view")
        else:
            return redirect("/post_view")
    else:
        return render(request,"User_home.html")
from Turf . models import turf_reg_tbl,slot_tbl
def user_turf_view(request):
    turf=turf_reg_tbl.objects.filter(Approve=True)
    if turf:
        slot=slot_tbl.objects.filter(status="no issue")
        return render(request,"user_turf_view.html",{"view":turf,"slot":slot})
    else:
        messages.success(request,'no turfs')
        return render(request,"User_home.html")
from django.utils import timezone
def turf_book(request):
    uid=request.session['uid']
    if request.method=="POST":
        tid=request.POST.get('tid')
        bdate=request.POST.get('bdate')
        slot=request.POST.get('slot')
        user=User_regtbl.objects.get(id=uid)
        turf=turf_reg_tbl.objects.get(id=tid)
        slotob=slot_tbl.objects.get(id=slot)
        today = datetime.now().date()
        six_days_later = today + timedelta(days=6)
        date = datetime.strptime(bdate, '%Y-%m-%d').date() 
        if date <= six_days_later or (date <= date.today() and slotob.stime<timezone.now().time()):
           if  turf_booking_tbl.objects.filter(turf__id=tid,bdate=bdate,stime__lt=slotob.etime,etime__gt=slotob.stime).exists():
               messages.success(request,'already booked choose another slot')
               return redirect("/user_turf_view")
           else:
            if turf and slotob:
              obj=turf_booking_tbl.objects.create(sid=slotob.id,bdate=bdate,user=user,turf=turf,stime=slotob.stime,etime=slotob.etime,amount=slotob.amount)
              obj.save()
              return render(request,"turf_payment.html",{"book":obj})
            else:
                return redirect("/user_turf_view")

        else:
          messages.success(request,'only allowed to book dates within 6 days')
          return redirect("/user_turf_view")
    else:
        return redirect("/user_turf_view")
def turf_pay(request):
    uid=request.session['uid']
    if request.method=="POST":
        idn=request.POST.get('idn')
        edate=request.POST.get('expiry-date')
        user=User_regtbl.objects.get(id=uid)
        obj=turf_booking_tbl.objects.get(id=idn)
        date = datetime.strptime(edate, '%Y-%m-%d').date() 
        if obj and date>date.today():
            obj.status="paid"
            obj.save()
            subject = 'Turf Booking Confirmation'
            message = f'Dear {user.eml},\n\nYour booking for {obj.turf.tname} has been confirmed.your slot is {obj.stime}-{obj.etime} and book date {obj.bdate} Thank you for choosing our service!\n\nRegards,\nThe Turf Booking Team'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.eml]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            messages.success(request,'booking success')
            return redirect("/user_turf_view")
        else:
            messages.success(request,'card is expired')
            return redirect("/user_turf_view")
    else:
        return redirect("/user_turf_view")
def turf_my_booking(request):
    uid=request.session['uid']
    obj=turf_booking_tbl.objects.filter(user__id=uid,status="paid")
    if obj:
        return render(request,"user_turf_booking_view.html",{"view":obj})
    else:
        return redirect("/user_turf_view")
def turf_cancel_book(request):
    uid=request.session['uid']
    if request.method=="POST":
        bid=request.POST.get('bid')
        obj=turf_booking_tbl.objects.get(user__id=uid,id=bid)
        if obj.bdate>date.today():
          obj.delete()
          messages.success(request,'booking cancelled your 10 percent refund is progressing')
          return redirect("/turf_my_booking")
        else:
            messages.success(request,'not possible to  cancell')
            return redirect("/turf_my_booking")

    else:
        return redirect("/turf_my_booking")
def p_search(request):
    if request.method=="POST":
        search=request.POST.get('pnm')
        products=product_upload_tbl.objects.filter(Q(productname__icontains=search) | Q(productname__istartswith=search))
        if products:
            return render(request,"User_search_product.html",{"view":products}) 
        else:
            messages.success(request,'no product')
            return redirect("/sports_items")
    else:
        return redirect("/sports_items")
def turf_search(request):
    if request.method=="POST":
        dist=request.POST.get('dist')
        turf=turf_reg_tbl.objects.filter(Approve=True,dist=dist)
        if turf:
           slot=slot_tbl.objects.filter(status="no issue")
           return render(request,"user_turf_search.html",{"view":turf,"slot":slot})
        else:
          return redirect("/user_turf_view")
    else:
         return redirect("/user_turf_view")
def my_post_view(request):
    uid=request.session['uid']
    obj=posts_tbl.objects.filter(user__id=uid)
    comment=comments_tbl.objects.all()
    if obj:
        return render(request,"my_post.html",{"view":obj,"cmnt":comment})
    else:
        messages.success(request,'no my posts')
        return redirect("/post_view")

def delete_post(request):
    pid=request.GET.get('idn')
    obj=posts_tbl.objects.get(id=pid)
    if obj:
        obj.delete()
        return redirect("/my_post_view")
    else:
        return redirect("/my_post_view")
def user_profile(request):
    uid=request.session['uid']
    obj=User_regtbl.objects.filter(id=uid)
    if obj:
        return render(request,"User_profile.html",{'view':obj})
    else:
        return render(request,"User_home.html")
         
         



        
    



    


    


    
          




        

    


            




        

          

          
        





        

        





        
    
    


      




    






        
        
  
     
        
        
            
    


    





    
    










    
    





