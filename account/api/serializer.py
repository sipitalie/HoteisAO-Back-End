from account.models import Account
from django.contrib.auth import password_validation
from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext as _
from django.conf import settings


class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields =['id','email', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model=Account
        fields=['email','username', 'password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        account=Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'passwords must match.'})
        account.set_password(password)
        account.save()
        return account

class  AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['pk','email','username']

class  ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)
    confirm_new_password=serializers.CharField(required=True)


#class PasswordResetSerializer(serializers.Serializer):
#    email = serializers.EmailField(required=True)


#class PasswordResetConfirmSerializer(serializers.Serializer):
#    new_password = serializers.CharField(style={'input_type': 'password'},required=True)
#    token = serializers.CharField(required=True)

#    def validate_new_password(self, value):
#        password_validation.validate_password(value)
#        return value




###### IMPORT YOUR USER MODEL ######


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm
    def validate_email(self, value):
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(_('Error'))

        ###### FILTER YOUR USER MODEL ######
        if not Account.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Invalid e-mail address'))
        return value

    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),

            ###### USE YOUR TEXT FILE ######
            'email_template_name': 'example_message.txt',

            'request': request,
        }
        self.reset_form.save(**opts)