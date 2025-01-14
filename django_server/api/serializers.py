from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from . import models

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id',  'first_name', 'last_name', 'email', 'password', 'date_joined', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        if not validated_data.get('is_google_user', False):
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)

        instance.save()
        return(instance)
    
class LogoutUserSerializer(serializers.Serializer):
    refresh_token=serializers.CharField()
    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs.get('refresh_token')
        return attrs

    def save(self, **kwargs):
        try:
            token=RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            return self.fail('bad_token')
    

# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'
        

# booking serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'
        

# review serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
        

# service serializer
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'
        
# newsletter mail serializer
class Newsletter_MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newsletter_Mail
        fields = '__all__'