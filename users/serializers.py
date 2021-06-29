from rest_framework import serializers

from users.models import  CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    """"Serializer for our custom user"""

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name','last_name', 'password', 'profile_pic', 'business_name')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = CustomUser(
            email=validated_data['email'],
            business_name=validated_data['business_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


