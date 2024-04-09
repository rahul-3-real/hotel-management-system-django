from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account, Admin, Staff, Guest


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.type == "admin":
            Admin.objects.create(user=instance)
        elif instance.type == "staff":
            Staff.objects.create(user=instance)
        elif instance.type == "guest":
            Guest.objects.create(user=instance)
