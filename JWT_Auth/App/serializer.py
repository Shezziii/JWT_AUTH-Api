# import serializer from rest_framework

from rest_framework import serializers
from .models import iUser

class UserRegistrationSerializers(serializers.ModelSerializer):
    password2=serilaizers.CharField(style={'input_type':'password' }, write_only= True )
    class Meta:
        model=iUser
        fields=['email' , 'name' , 'password' , 'password2']
        extra_kwargs={
        'password':{'write_only' : True}
        }
    def validated(self,data):
            password=data.get('password')
            password2=data.get('password2')
            if password!=password2:
                raise serializers.ValidationError("Password's is doesn't match.") 
            return super().validate(data)
            
    def create(self,validated_data):
        return iUser.objects.create_user(**validated_data)        
