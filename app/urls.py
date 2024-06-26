from django .urls import path
from .views import home_view,about_view,contact_view,blog_view

urlpatterns = [
path('',home_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('blog/',blog_view,name='blog-page'),
    path('contact/',contact_view,name='contact-page'),
   
]
