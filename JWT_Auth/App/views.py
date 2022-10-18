from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializers ,UserLoginSerializers , UserProfileSerializers , UserChangePass
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import JsonResponse

#Function for cretaing token Manually.
def generate_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
# Create your views here.
class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegistrationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        token = generate_token(user)
        return Response({'msg':'Registration Successfull.','Token': token },status=status.HTTP_201_CREATED)
        #return Response({'error':serializers.error},status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    def post(self,request,format=True):
        serializer=UserLoginSerializers (data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token = generate_token(user)
                return Response({'msg': 'Login Successful.' , 'Token' : token } , status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'Invalid email and Password'},status=status.HTTP_400_BAD_REQUEST)    
        else:
               return Response({'error':'Invalid email and Password'},status=status.HTTP_400_BAD_REQUEST)          

                
class UserProfileView(APIView):
      #authentication_classes = [SessionAuthentication, BasicAuthentication]
      permission_classes=[IsAuthenticated]
      def get(self,request,format=None):
          user=UserProfileSerializers(request.user)
          print("******** Working ***********")
          return JsonResponse(user.data)
                                                              
class ChangePassView(APIView):
      permission_classes=[IsAuthenticated] 
      def post(self,request,format=True):
          print("***************")
          print(request.user)
          print("***************")
          user=UserChangePass(data=request.data,context={'user':request.user}) 
          if user.is_valid(raise_exception=True):
              return Response({'msg':'Password Changes Successfully.',status=status.HTTP_200_OK)
          return Response({'Error':user.error},status=status.HTTP_400_BAD_REQUEST)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                              
                                                                
