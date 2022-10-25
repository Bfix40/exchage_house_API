from dataclasses import fields
from rest_framework import serializers

from .models import Currency, TrackFee, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {
            "password":{"write_only": True}
        }
    
    def create(self, validated_data):

        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        
        instance.save()
        return instance
    

class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        exclude = ('id_currency',)

class TrackFeeSerializer(serializers.Serializer):

    class Meta:
        model = TrackFee
        fields = ["fee_amount", "date_transaction",
                  "base_currency", "quote_currency"]
