from rest_framework import serializers

from services.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class SubscriptionSerializers(serializers.ModelSerializer):
    plan = PlanSerializer()
    client_name = serializers.CharField(source="client.company_name")
    email = serializers.CharField(source="client.user.email")
    price = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = (
            'id',
            'client_name',
            'email',
            'plan',
            'price'
        )

    def get_price(self, instance):
        return instance.price

