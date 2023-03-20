from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Address


@receiver(post_save, sender=Address)
def set_default_address(sender, instance, created, **kwargs):
    if created and instance.default:
        Address.objects.filter(user=instance.user).exclude(id=instance.id).update(
            default=False
        )
