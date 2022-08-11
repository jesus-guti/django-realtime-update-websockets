import json
from channels.generic.websocket import WebsocketConsumer

from .models import Notifications
from django.forms.models import model_to_dict
from time import sleep



class NotificationsConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope)
        self.accept()
        while True:
            self.send(json.dumps({
                "type":"send_message",
                "text": model_to_dict(Notifications.objects.last())
            })) 
            sleep(1)