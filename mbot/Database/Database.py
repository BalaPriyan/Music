import asyncio
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['your_database_name'] 
        self.sg = self.db['your_collection_name'] 




async def add_set(self,id):
          new = {
           "id":id,
           "url": "True",
           "quality": "flac",
           "search": "True",
           "broadcast": "True",
           "http": "True",
           "done": "True",
            }
          await self.sg.insert_one(new)
    async def get_set(self,id):
          users = await self.sg.find_one({'id': int(id)})
          return users     
    async def set_set(self,id,item_id,item_type):
          await self.sg.update_one({'id': int(id)},{'$set': {item_id: item_type}})


