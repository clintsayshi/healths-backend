from rest_framework import serializers
from app.models import Profile
from django.contrib.auth.models import User

# proiles serializer
class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model: Profile
        fields: '__all__'

# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model: Profile
        fields: '__all__'


# register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user