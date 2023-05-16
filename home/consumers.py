
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from home.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        username = str(self.scope["user"])
        self.room_name =a=self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        
        user_id = self.scope['user'].id
        user_qs = await sync_to_async(User.objects.filter)(id=user_id)
        await sync_to_async(user_qs.update)(online=True)
        username = str(self.scope["user"])
        
        user_s = await sync_to_async(User.objects.filter)(id=user_id)
        user = await sync_to_async(user_s.first)()
        online = user.online if user else False

        
       
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

          

        await self.accept()


        await self.channel_layer.group_send(
            self.room_group_name,
        {
            'type': 'chat_join',
            'username': 'username',
            'online':online 
        }
    )


    async def disconnect(self, close_code):
        user_id = self.scope['user'].id
        user_qs = await sync_to_async(User.objects.filter)(id=user_id)
        await sync_to_async(user_qs.update)(online=False)
        username = str(self.scope["user"])
        
        user_s = await sync_to_async(User.objects.filter)(id=user_id)
        user = await sync_to_async(user_s.first)()
        online = user.online if user else False

        await self.channel_layer.group_send(
            self.room_group_name,
        {
            'type': 'chat_leave',
            'username': 'username',
            'online':online 
        }
    )

    
        
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
            
        )


        

    async def receive(self, text_data):
       
          text_data_json = json.loads(text_data)
          message = text_data_json['message']
          username = str(self.scope["user"])

          await self.channel_layer.group_send(
             self.room_group_name,
             {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )
          


    async def chat_message(self, event):
        message = event['message']
        username = event["username"]
        
        css_class = 'current-user' if username == self.scope["user"].username else 'other-user'

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'css_class':css_class,

            

     }))
        
    async def chat_leave(self, event):
    
        username = event["username"]
        online = event['online']
        

        await self.send(text_data=json.dumps({

            'username': username,
            'is_online': online,

            

     })) 

    async def chat_join(self, event):
    
        username = event["username"]
        online = event['online']
        

        await self.send(text_data=json.dumps({

            'username': username,
            'is_online': online,

            

     }))        

   

# class OnlineConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         username = str(self.scope["user"])
#         self.room_name =a=self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = "chat_%s" % self.room_name
        
#         user_id = self.scope['user'].id
#         user_qs = await sync_to_async(User.objects.filter)(id=user_id)
#         await sync_to_async(user_qs.update)(online=True)
#         username = str(self.scope["user"])
        
#         user_s = await sync_to_async(User.objects.filter)(id=user_id)
#         user = await sync_to_async(user_s.first)()
#         online = user.online if user else False

        
       
#         await self.channel_layer.group_add(
#             self.room_group_name, self.channel_name
#         )

          

#         await self.accept()


#         await self.channel_layer.group_send(
#             self.room_group_name,
#         {
#             'type': 'chat_join',
#             'username': 'username',
#             'online':online 
#         }
#     )


#     async def disconnect(self, close_code):
#         user_id = self.scope['user'].id
#         user_qs = await sync_to_async(User.objects.filter)(id=user_id)
#         await sync_to_async(user_qs.update)(online=False)
#         username = str(self.scope["user"])
        
#         user_s = await sync_to_async(User.objects.filter)(id=user_id)
#         user = await sync_to_async(user_s.first)()
#         online = user.online if user else False

#         await self.channel_layer.group_send(
#             self.room_group_name,
#         {
#             'type': 'chat_leave',
#             'username': 'username',
#             'online':online 
#         }
#     )

    
        
#         await self.channel_layer.group_discard(
#             self.room_group_name, self.channel_name
            
#         )

    
#     async def chat_leave(self, event):
    
#         username = event["username"]
#         online = event['online']
        

#         await self.send(text_data=json.dumps({

#             'username': username,
#             'is_online': online,

            

#      })) 

    # async def chat_join(self, event):
    
    #     username = event["username"]
    #     online = event['online']
        

    #     await self.send(text_data=json.dumps({

    #         'username': username,
    #         'is_online': online,

            

    #  }))        