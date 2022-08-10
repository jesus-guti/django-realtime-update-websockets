from django.shortcuts import render

# Create your views here.

@database_sync_to_async
def create_notification(receiver,typeof="task_created",status="unread"):
    notification_to_create=notifications.objects.create()
    print('I am here to help')
    return (notification_to_create.user_revoker.username,notification_to_create.type_of_notification)