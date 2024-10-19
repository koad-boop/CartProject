from django.urls import path
from cart_admin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminn',views.index),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('addproduct/',views.addproduct_view,name='addproduct'),
    path('viewproduct/',views.viewproduct_view,name='viewproduct'),
    path('addcategory/',views.addcategory_view,name='addcategory'),
    path('deleteproduct/<id>',views.deleteproduct_view,name='deleteproduct'),
    path('editproduct/<id>',views.edit_view,name='editproduct'),
    path('mail',views.email,name='mail'),
    path('send_email',views.send_email,name='send_email'),
    path('formfor_otp',views.formforotp,name='formfor_otp'),
    path('otp',views.otp,name='otp'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )