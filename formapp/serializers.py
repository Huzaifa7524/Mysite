from .models import Form
from rest_framework import serializers

class formSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'name', 'email', 'phone','message']
         
     
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password') 
#         extra_kwargs = {'password': {'write_only': True}}
