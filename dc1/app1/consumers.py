from channels.routing import ProtocolTypeRouter
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connected')
        self.send({
            'type':'websocket.accept'
        })
        
    def websocket_receive(self,event):
        print('message received from the client',event)
        print(event['text'])
        self.send({
            'type':'websocket.send',
            'text':'message was sent to the client from the application'
            
        })
    
    def websocket_disconnect(self,event):
        print("websocket disconnected",event)
        raise StopConsumer
    
#--------------------------------------------------------------------------------------

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event): # before the handshake
        print("websocket connected")
        await self.send({
            'type':'websocket.accept'
        })


    
    # this handler is called when data is received 
    async def websocket_receive(self,event):
        print('message recieved from client',event)
        print(event['text'])
        await self.send({
            'type':'websocket.send',
            'text':'message was sent to the client from the application'
        })
    #this handler is called when the client or server disconnect
    async def websocket_disconnect(self,event):
         print('websocket disconneted...',event)
         raise StopConsumer
        














