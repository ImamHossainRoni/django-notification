import json

from django.http import HttpResponse
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your views here.


def index(request):
    return render(request, 'index.html', {'room_name': 'broadcast'})


def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification 3")
        }
    )
    return HttpResponse("Done")

def new():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification 3")
        }
    )
    return HttpResponse("Done")