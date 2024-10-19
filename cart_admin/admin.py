from django.contrib import admin
from .models import Admin,Category,Product,Cart

# Register your models here.
class AdminAdmin(admin.ModelAdmin):
    list_display=('name','email','phone')
admin.site.register(Admin,AdminAdmin)    

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','des')
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','category','des','image')
admin.site.register(Product ,ProductAdmin)   

class CartAdmin(admin.ModelAdmin):
    list_display=( 'id','pro_id','cust_id',"quantity")
admin.site.register(Cart,CartAdmin)


