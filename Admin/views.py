from django.shortcuts import render,redirect
from itemseller . models import Itemseller_reg_tbl
from Turf.models import turf_reg_tbl
from Event . models import Event_manager_tbl
from Academy . models import Academy_reg_tbl

# Create your views here.
def Admin(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        if eml=="admin@gmail.com" and psw=="1234":
            return render(request,"Admin_home.html")
        else:
            return render(request,"Admin_login.html")
    else:
        return render(request,"Admin_login.html")
def Admin_itemseller_view(request):
    obj=Itemseller_reg_tbl.objects.filter(Approve=False)
    if obj:
        return render(request,"Admin_itemseller_view.html",{"view":obj})
    else:
        return render(request,"Admin_itemseller_view.html")
def Admin_itemseller_approve_view(request):
    obj=Itemseller_reg_tbl.objects.filter(Approve=True)
    if obj:
        return render(request,"Admin_approved_itemseller.html",{"view":obj})
    else:
        return render(request,"Admin_approved_itemseller.html")
def itemseller_approve(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        btn=request.POST.get('btn')
        obj=Itemseller_reg_tbl.objects.get(id=sid)
        if obj:
            if btn=="approve":
              obj.Approve=True
              obj.save()
              return redirect("/Admin_itemseller_view")
            elif btn=="disapprove":
              obj.Approve=False
              obj.save()
              return redirect("/Admin_itemseller_approve_view")
        else:
            return redirect("/Admin_itemseller_view")
    else:
        return redirect("/Admin_itemseller_view")
def Admin_home(request):
    return render(request,"Admin_home.html")
def Admin_turf_view(request):
    obj=turf_reg_tbl.objects.filter(Approve=False)
    if obj:
        return render(request,"Admin_turf_view.html",{"view":obj})
    else:
        return render(request,"Admin_turf_view.html")
def Admin_approved_turf_view(request):
    obj=turf_reg_tbl.objects.filter(Approve=True)
    if obj:
        return render(request,"Admin_approved_turf.html",{"view":obj})
    else:
        return render(request,"Admin_approved_turf.html")
def Turf_approve(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        btn=request.POST.get('btn')
        obj=turf_reg_tbl.objects.get(id=sid)
        if obj:
            if btn=="approve":
              obj.Approve=True
              obj.save()
              return redirect("/Admin_turf_view")
            elif btn=="disapprove":
              obj.Approve=False
              obj.save()
              return redirect("/Admin_approved_turf_view")
        else:
            return redirect("/Admin_turf_view")
    else:
        return redirect("/Admin_turf_view")
def Admin_event_view(request):
    obj=Event_manager_tbl.objects.filter(Approve=False)
    if obj:
        return render(request,"Admin_event_view.html",{"view":obj})
    else:
        return render(request,"Admin_event_view.html")
def Admin_approved_event_view(request):
    obj=Event_manager_tbl.objects.filter(Approve=True)
    if obj:
        return render(request,"Admin_approved_event.html",{"view":obj})
    else:
        return render(request,"Admin_approved_event.html")
def Event_approve(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        btn=request.POST.get('btn')
        obj=Event_manager_tbl.objects.get(id=sid)
        if obj:
            if btn=="approve":
              obj.Approve=True
              obj.save()
              return redirect("/Admin_event_view")
            elif btn=="disapprove":
              obj.Approve=False
              obj.save()
              return redirect("/Admin_approved_event_view")
        else:
            return redirect("/Admin_event_view")
    else:
        return redirect("/Admin_event_view")
def Admin_academy_view(request):
    obj=Academy_reg_tbl.objects.filter(Approve=False)
    if obj:
        return render(request,"Admin_academy_view.html",{"view":obj})
    else:
        return render(request,"Admin_academy_view.html")
def Admin_approved_academy_view(request):
    obj=Academy_reg_tbl.objects.filter(Approve=True)
    if obj:
        return render(request,"Admin_approved_academy.html",{"view":obj})
    else:
        return render(request,"Admin_approved_academy.html")
def Academy_approve(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        btn=request.POST.get('btn')
        obj=Academy_reg_tbl.objects.get(id=sid)
        if obj:
            if btn=="approve":
              obj.Approve=True
              obj.save()
              return redirect("/Admin_academy_view")
            elif btn=="disapprove":
              obj.Approve=False
              obj.save()
              return redirect("/Admin_approved_academy_view")
        else:
            return redirect("/Admin_academy_view")
    else:
        return redirect("/Admin_academy_view")








    
         
    
    