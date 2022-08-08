from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes,permission_classes



from .models import CustomUser



# because this is an inherited class it will be quite different
class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self,validate_data):
        password = validate_data.pop('password',None)
        instance = self.Meta.model(**validate_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


    def update(self,instance, validate_data):
        for attr, value in validate_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
    
        instance.save()
        return instance
    class Meta:
        model = CustomUser
        extra_kwargs = {'password':{'write_only': True}}
        fields = ['name', 'email', 'password', 'phone', 'gender',
        'is_active','is_staff', 'is_superuser']