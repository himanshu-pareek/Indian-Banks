from rest_framework import serializers
from .models import Bank, Branch

class BankSerializer (serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ('name', )

class BranchSerializer (serializers.ModelSerializer):

    bank = serializers.SerializerMethodField('get_bank_name')

    class Meta:
        model = Branch
        # fields = '__all__'
        exclude = ('bank_id', )

    def get_bank_name (self, obj):
        return obj.bank_id.name
