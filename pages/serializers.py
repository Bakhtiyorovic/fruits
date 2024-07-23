from rest_framework import serializers
from .models import *



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"



class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = "__all__"



class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = "__all__"


class ProducSerializer(serializers.ModelSerializer):
    class Meta:
        models = ProductModel
        fields = "__all__"


