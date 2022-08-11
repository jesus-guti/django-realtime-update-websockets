import json
import channels.layers
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification


def send_message(event):
    '''
    Call back function to send message to the browser
    '''
    message = event['text']
    channel_layer = channels.layers.get_channel_layer()
    # Send message to WebSocket
    async_to_sync(channel_layer.send)(text_data=json.dumps(
        message
    ))

@receiver(post_save, sender=Notification)
def update_notification_status_listeners(sender, instance, **kwargs):
    print("Señales funcionan", instance.text , flush=True)

    group_name = 'previewer'

    message = {
        'notification_id': instance.id,
        'text': instance.text
    }
    
    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_message',
            'text': message
        }
    )