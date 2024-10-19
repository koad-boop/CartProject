from django.urls import path
from cart import views
urlpatterns = [
    path('',views.index,name='index'),
    path('userlogin/',views.userlogin_view,name='userlogin'),
    path('signup/',views.signup_view,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_view,name='logout'),
    path('cart/',views.cart_view,name='cart'),
    path('fpf',views.fpf,name='fpf'),
    path('password_form/',views.form_otp,name='password_form/'),
    path('newpassword/',views.New_Password,name='newpassword'),
    path('gindex/',views.gindex,name='gindex') 

]