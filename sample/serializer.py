from rest_framework import serializers
from sample.models import InvoiceTest


class InvoiceTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceTest
        fields = '__all__'
