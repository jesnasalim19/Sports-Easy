from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Admin',views.Admin),
    path('Admin_itemseller_view',views.Admin_itemseller_view),
    path('Admin_itemseller_approve_view',views.Admin_itemseller_approve_view),
    path('itemseller_approve',views.itemseller_approve),
    path('Admin_home',views.Admin_home),
    path('Admin_turf_view',views.Admin_turf_view),
    path('Admin_approved_turf_view',views.Admin_approved_turf_view),
    path('Turf_approve',views.Turf_approve),
    path('Admin_event_view',views.Admin_event_view),
    path('Admin_approved_event_view',views.Admin_approved_event_view),
    path('Event_approve',views.Event_approve),
    path('Admin_approved_academy_view',views.Admin_approved_academy_view),
    path('Academy_approve',views.Academy_approve),
    path('Admin_academy_view',views.Admin_academy_view),

 
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)