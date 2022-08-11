import json
from time import sleep
from channels.generic.websocket import WebsocketConsumer
from .models import Notification
from asgiref.sync import async_to_sync



class NotificationConsumer(WebsocketConsumer):
    
    def connect(self):
        self.group_name = 'previewer'

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()
        self.send_last_notification()

    def disconnect(self, close_code):

        self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    def send_last_notification(self):

            last_notification = Notification.objects.last()

            message = {
                'notification_id': last_notification.id,
                'text': last_notification.text,
            }

            self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type': 'send_message',
                        'text': message
                    }
                )
            #Mandar la primera vez que se abre la conexion
            self.send(text_data=json.dumps(
                message
            ))

    def send_message(self, event):
            message = event['text']

            # Send message to WebSocket
            self.send(text_data=json.dumps(
                message
            ))