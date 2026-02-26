import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class WSConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        count = 0
        for i in range(1000):
            count += 1
            await self.send(json.dumps({
                'message': count,
            }))
            await asyncio.sleep(1)