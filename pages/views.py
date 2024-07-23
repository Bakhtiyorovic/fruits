from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.

def Home(request):
    return render(request, 'index.html')

def Product(request):
    return render(request, 'product.html')

def Gallery(request):
    return render(request, 'gallery.html')

def About(request):
    about_object = AboutModel.objects.first()
    return render(request, 'about.html', {'about': about_object})

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')  # message ustunini ham o'qish kerak
        
        if name and phone and email and message:  # Malumotlar to'liq kiritilganligini tekshiramiz
            contact_data = ContactMessage(name=name, phone=phone, email=email, message=message)
            contact_data.save()
            return render(request, 'contact.html', {'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi.'})
        else:
            return render(request, 'contact.html', {'error': 'Iltimos, barcha maydonlarni to\'ldiring.'})
    else:
        return render(request, 'contact.html')




class ContuctApiView(generics.ListAPIView):
     queryset = ContactMessage.objects.all()
     serializer_class = ContactSerializer


class GalleryApiView(generics.ListAPIView):
    queryset = GalleryModel.objects.all()
    serializer_class = GallerySerializer



class AboutApiView(generics.ListAPIView):
    queryset = AboutModel.objects.all()
    serializer_class = AboutSerializer


class ProductApiView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProducSerializer

