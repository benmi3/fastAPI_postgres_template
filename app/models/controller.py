from os import environ

from ..auth import create_password_salt_token
from .setup import check_db
from .item import (
    select_all_items,
    select_item_by_text_identifier_cid,
    insert_item,
    update_item_by_id,
    delete_item_by_id
)
from .user import (
    select_username_by_id,
    select_user_by_username,
    insert_user,
    update_username_by_id,
    delete_user_by_id
)

db_user = environ.get('POSTGRES_USER')
db_pass = environ.get('POSTGRES_PASSWORD')
db_host = environ.get('POSTGRES_HOST')
db_name = environ.get('POSTGRES_DB')
db_port = environ.get('POSTGRES_PORT')


class Controller:
    def __init__(self):
        # Maybe make this a try except later, but for now, leave like this.
        # We want it to crash as soon as possible,
        # if it cannot connect to the database.
        # try:
        self.db_url = f"""postgresql://{db_user}:
        {db_pass}@{db_host}:{db_port}/{db_name}"""
        # except TypeError:
        #    self.db_url = ""
        self.check = self.check_db()

    async def check_db(self) -> bool:
        return await check_db(
            db_user, db_pass, db_host, db_port, db_name, self.db_url)


class UserController(Controller):
    # User --------------------------------------------------------------------
    async def select_user(self, user_id: str) -> str:
        return await select_username_by_id(self.db_url, user_id)

    async def select_user_by_name(self, username: str) -> str:
        return await select_user_by_username(self.db_url, username)

    async def create_user(
            self,
            username: str,
            email: str,
            password: str,
            is_admin: bool) -> bool:
        auth_stack = create_password_salt_token(password)
        return await insert_user(self.db_url,
                                 username,
                                 email,
                                 auth_stack.get('password'),
                                 auth_stack.get('pwd_salt'),
                                 auth_stack.get('token_salt'),
                                 is_admin)

    async def update_user(self, user_id: str, new_username: str) -> bool:
        return await update_username_by_id(self.db_url, user_id, new_username)

    async def delete_user(self, user_id: str) -> bool:
        return await delete_user_by_id(self.db_url, user_id)


class AuthController(UserController):
    async def get_user_then verify(self, user_id: str, ) -> tuple[bool]


class ItemController(Controller):
    # Item --------------------------------------------------------------------
    async def select_items(self, identifier: str) -> list:
        return await select_all_items(self.db_url, identifier)

    async def select_item_by_item_identifier_cid(
            self, text: str, identifier: str, cid: str) -> str:
        return await select_item_by_text_identifier_cid(
            self.db_url, text, identifier, cid)

    async def create_item(self, cid: str, item: str, identifier: str) -> bool:
        user_controller = UserController()
        user_id = user_controller.select_user_by_name()
        return await insert_item(self.db_url, cid, item, identifier)

    async def update_item(
            self,
            item_id:
            str,
            cid: str,
            item: str,
            identifier: str) -> bool:
        return await update_item_by_id(
            self.db_url, item_id, cid, item, identifier)

    async def delete_item(
            self, item_id: str, cid: str, identifier: str) -> bool:
        return await delete_item_by_id(self.db_url, item_id, cid, identifier)
