from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import DataSet
from core.tasks import get


@receiver(post_save, sender=DataSet)
def process_data_set(sender, instance, created, **kwargs):
    if created:
        get.delay(instance)
