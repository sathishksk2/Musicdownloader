import datetime

import motor.motor_asyncio


class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    async def users_count(self):
       users = self.col.find({"users": True})
       return users
    
    async def new_user(self, id):
        return dict(id = id, join_date = datetime.date.today().isoformat())

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        return True if user else False

    async def total_users_count(self):
       count = await self.col.count_documents({})
       return count


    
