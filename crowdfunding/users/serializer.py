from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = '__all__'
        extra_kwargs = {'password' : {'write_only':True}} # tell serializer and extra key word argument extra kwargs and write_only infor how it should be serialized

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data) # for password harshing
    
    # if we use custom objects user Django will automaticall harsh the password

class CustomUserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        return instance