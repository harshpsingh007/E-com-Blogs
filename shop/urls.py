from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='shop homepage'),
    path("aboutus/",views.aboutus,name='about_us'),
    path("contactus/",views.contactus,name='contact_us'),
    path("products/<int:myid>/",views.productview,name='product_view'),
    path("checkout/",views.checkout,name='check_out'),
    path("search/",views.search,name='search'),
    path("tracker/",views.tracker,name='track_order'),
    path("cart/",views.cart,name='cart'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("allproducts/", views.allproducts, name="all_products"),
]
