# import serializer from rest_framework

from rest_framework import serializers
from .models import iUser

class UserRegistrationSerializers(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = iUser
    fields=['email', 'name', 'password', 'password2']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return iUser.objects.create_user(**validate_data)

       

class UserLoginSerializers(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=iUser
        fields=['email' , 'password']
        
class UserProfileSerializers(serializers.ModelSerializer):
    class Meta: 
        model=iUser
        fields=['email' , 'name' , 'id']   
        
             
        

class UserChangePass(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['email','password', 'password2']

   def validate(self, attrs):
    user = self.context.get('user')
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
    user.set_password(password)
    user.save()
    return attr                                      
