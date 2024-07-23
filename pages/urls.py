from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name= 'home'),
    path('contact/', Contact, name= 'contact'), 
    path('gallery/', Gallery, name= 'gallery'),
    path('about/', About, name= 'about'), 
    path('product/', Product, name= 'product'),
    path('api1/', ContuctApiView.as_view(), name = 'contact_api'),
    path('api2/', GalleryApiView.as_view(), name = 'gallery_api'),
    path('api3/', AboutApiView.as_view(), name = 'about_api'),
    path('api/', ProductApiView.as_view(), name = 'product_api'),
]

