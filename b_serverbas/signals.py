from django.db.models.signals import post_save, post_delete,post_migrate
from django.dispatch import receiver
from .models import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@receiver(post_save, sender=Notification)
def send_notification_update(sender, instance, created, **kwargs):

    channel_layer = get_channel_layer()
    data = {
        'action': 'notification_update',
        'id': instance.id,
        'message': instance.Message,
    }
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            'type': 'send_notification_update',
            'data': data
        }
    )

@receiver(post_delete, sender=Notification)
def send_update_on_delete(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    data = {
        'action': 'delete',
        'id': instance.id,
    }
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            'type': 'send_notification_update',
            'data': data
        }
    )