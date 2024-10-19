from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','fname','lname','father','email','pass1','phone')
admin.site.register(Customer,CustomerAdmin)

