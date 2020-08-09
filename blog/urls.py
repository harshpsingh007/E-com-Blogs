from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='blog_homepage'),
    path("blogpost/<int:id>/",views.blogpost,name='blog_post'),
    path("blogaboutus/",views.blogaboutus,name='blog_about_us'),
    path("contact_us/",views.contact_us,name='blog_about_us'),
    path("signup/",views.handlesignup,name='handle_signup'),
    path("login/",views.handlelogin,name='handle_login'),
    path("logout/",views.handlelogout,name='handle_logout'),
    path("search/",views.search,name='search')
]
