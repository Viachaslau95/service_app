from celery import shared_task
from celery_singleton import Singleton
from django.db.models import F

"""
Singleton - creating a class in one instance.
Use in order not to send permanent tasks with the same arguments
"""


@shared_task(base=Singleton)
def set_price(subscription_id):
    from services.models import Subscription

    subscription = Subscription.objects.filter(id=subscription_id).annotate(
        annotated_price=F('service__full_price') - F('service__full_price') * F('plan__discount_percent') / 100.00
    ).first()

    subscription.price = subscription.annotated_price
    subscription.save()


