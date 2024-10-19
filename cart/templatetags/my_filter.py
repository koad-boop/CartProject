from django import template
from cart_admin.models import Product,Cart
from cart.models import Customer
register=template.Library()


@register.filter
def Currency(value):
    return "₹"+str(int(value))

@register.filter
def mg(value):
    cust = Customer.objects.get(id=value)
    return cust.image.url

def fetch_instance(product,cust_id):
    pro_instance = Product.objects.get(id=product.id)
    cust_instance = Customer.objects.get(id=cust_id) 
    return [pro_instance,cust_instance]

@register.filter
def cart_status(product,cust_id): 
    pro_i,cust_i = fetch_instance(product,cust_id)
    cart_instance = Cart.objects.filter(pro_id=pro_i,cust_id=cust_i)
    if cart_instance:
        return True
    return False


@register.filter
def cart_quantity(product,cust_id):
    pro_i,cust_i = fetch_instance(product,cust_id)
    cart_instance = Cart.objects.get(pro_id=pro_i,cust_id=cust_i)
    return cart_instance.quantity

@register.filter
def total_price(product,cart):
    return product.price*cart_quantity(product,cart)    

@register.filter
def grand_total(prods,cart):
    s=0
    for p in prods:
        s=s+total_price(p,cart)
    return s  

@register.filter
def c_qty(product_id,quantities_dict):
    for q in quantities_dict.keys():
        if product_id==q:
            return quantities_dict[q]
