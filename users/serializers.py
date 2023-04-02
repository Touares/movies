from rest_framework import serializers
from .models import CustomUser
# from django.contrib.auth.models import Permission
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    # is_staff = serializers.BooleanField(default=False)
    # is_superuser = serializers.BooleanField(default=False)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password',
         'first_name', 'last_name', "is_superuser", 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        # vendeur_data = validated_data.pop('vendeur')
        # if validated_data['is_staff']:
        #     is_staff=validated_data['is_staff']
        # else: is_staff=False
        # if validated_data['is_superuser']:
        #     is_superuser=validated_data['is_superuser']
        # else: is_superuser=False
        user = CustomUser.objects.create_user(username=validated_data['username'],
          password=validated_data['password']
        #  email=validated_data['email'],
        #  first_name=validated_data['first_name'], last_name=validated_data['last_name'],
        #   is_staff = validated_data['is_staff'], is_superuser= validated_data['is_superuser']
          )
        # user.set_password(validated_data['password'])
        # user.user_permissions.set(validated_data['permissions'])
        user.save()
        return user
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        # instance.username = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.email)
        instance.last_name = validated_data.get('last_name', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)

        # permissions = validated_data['permissions']
        # perm_list = []
        # for perm in permissions:
        #     try:
        #         permission = Permission.objects.get(name=perm)
        #     except Permission.DoesNotExist:
        #         raise serializers.ValidationError({'permission':'permission does not exist'})
        #     perm_list.append(permission)
        # instance.user_permissions.set(perm_list)

        return instance


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)