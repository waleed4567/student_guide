from channels.generic.websocket import AsyncJsonWebsocketConsumer

class BoardConsumer(AsyncJsonWebsocketConsumer):
    groups = ['students', ]




