from django.shortcuts import  render, redirect
from rest_framework import serializers
from .models import Form
from .serializers import formSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from MySQLdb import IntegrityError
from rest_framework.authtoken.models import Token
# Create your views here.


# class UserRegistrationView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user.set_password(request.data.get('password'))
#             user.save()
            
#             # Generate an authentication token
#             token, created = Token.objects.get_or_create(user=user)
            
#             # Create a response dictionary
#             response_data = {
#                 'message': 'User registered successfully',
#                 'user_id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#                 'token': token.key  # Include the access token
#             }
            
#             return Response(response_data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def postForm(request):
    try:
        form_data = request.data
        
        serializer = formSerializer(data = form_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError:
        return Response({"response": "User with this name already exists"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"response": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def getalldata(request):
    try:
        formdata = Form.objects.all()

        serializer = formSerializer(formdata, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"response": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)