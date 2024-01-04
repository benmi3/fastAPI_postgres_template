from os import environ

from ..auth import create_password_salt_token
from .setup import check_db
from .item import (select_all_items,
                   insert_item,
                   update_item_by_id,
                   delete_item_by_id)
from .user import (select_user_by_id,
                   insert_user,
                   update_username_by_id,
                   delete_user_by_id)

db_user = environ.get('POSTGRES_USER')
db_pass = environ.get('POSTGRES_PASSWORD')
db_host = environ.get('POSTGRES_HOST')
db_name = environ.get('POSTGRES_DB')
db_port = environ.get('POSTGRES_PORT')


class Controller:
    def __init__(self):
        # Maybe make this a try except later, but for now, leave like this.
        # We want it to crash as soon as possible, if it cannot connect to the database.
        # try:
        self.db_url = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        # except TypeError:
        #    self.db_url = ""
        self.check = check_db(db_user, db_pass, db_host, db_port, db_name, self.db_url)

    async def check_db(self) -> bool:
        return await self.check


class UserController(Controller):
    # User ------------------------------------------------------------------------------
    async def select_user(self, user_id: str) -> str:
        return await select_user_by_id(self.db_url, user_id)

    async def create_user(self, username: str, email: str, password: str, is_admin: bool) -> bool:
        auth_stack = create_password_salt_token(password)
        return await insert_user(self.db_url,
                                 username,
                                 email,
                                 auth_stack.get('password'),
                                 auth_stack.get('pwd_salt'),
                                 auth_stack.get('token_salt'),
                                 is_admin)

    async def update_user(self, user_id: str, username: str) -> bool:
        return await update_username_by_id(self.db_url, user_id, username)

    async def delete_user(self, user_id: str) -> bool:
        return await delete_user_by_id(self.db_url, user_id)


class ItemController(Controller):
    # Item ------------------------------------------------------------------------------
    async def select_items(self, identifier: str) -> list:
        return await select_all_items(self.db_url, identifier)

    async def create_item(self, cid: str, item: str, identifier: str) -> bool:
        return await insert_item(self.db_url, cid, item, identifier)

    async def update_item(self, item_id: str, cid: str, item: str, identifier: str) -> bool:
        return await update_item_by_id(self.db_url, item_id, cid, item, identifier)

    async def delete_item(self, item_id: str, cid: str, identifier: str) -> bool:
        return await delete_item_by_id(self.db_url, item_id, cid, identifier)
