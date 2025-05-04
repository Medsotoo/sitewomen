from django.urls import path, re_path, register_converter
from .views import index, about, show_post, addpage, contact, login
from . import converters

register_converter(converters.FourDigitConverter, 'year4')


urlpatterns = [
    path('',index, name='home'),
    path('about/',about, name='about'),
    path('addpage/',addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('iogin/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
]