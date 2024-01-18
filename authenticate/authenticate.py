# for the authentication in django using the customUser when we use the    [  user.set_password(password) ]      it create the password in hashed format 

# but when we give the data by own side or using the API then we have to convert the password to hash format so that during Authentication we doesn't have a None object user

# for this add 

# this function:
def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(AccountsSerializer, self).create(validated_data)



in serializer.py

from rest_framework import serializers
from account.models import Accounts
from django.contrib.auth.hashers import make_password

class AccountsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Accounts
        fields = "__all__"
        
        
        
    # very important to form the create because the password is serializer after it
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(AccountsSerializer, self).create(validated_data)
        
