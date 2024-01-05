import unittest
import pytest

from app.models.controller import Controller, UserController, ItemController


class ControllerTestCase(unittest.TestCase):
    controller_test = Controller()

    @pytest.mark.asyncio
    async def test_check_db(self):
        result = await self.controller_test.check_db()
        self.assertTrue(result, True)


class UserControllerTestCase(unittest.TestCase):
    controller_test = UserController()

    @pytest.mark.asyncio
    async def test_create_user(self):
        result = await self.controller_test.create_user(
            'test', 'test@test.com', 'test', False
        )
        self.assertTrue(result)

    @pytest.mark.asyncio
    async def test_update_user(self):
        user_id = self.controller_test.select_user_by_name('test')
        result = await self.controller_test.update_user(
            user_id[0],
            'new_test_username',
        )
        self.assertTrue(result)

    @pytest.mark.asyncio
    async def test_delete_user(self):
        user_id = self.controller_test.select_user_by_username('new_test_username')
        result = self.controller_test.delete_user(user_id[0])
        self.assertTrue(result)


class ItemControllerTestCase(unittest.TestCase):
    controller_test = ItemController()

    @pytest.mark.asyncio
    async def test_create_item(self):
        result = await self.controller_test.create_item(
            
        )
        self.assertTrue(result)

    @pytest.mark.asyncio
    async def test_update_item(self):
        user_id = self.controller_test.select_user_by_name('test')
        result = await self.controller_test.update_user(
            user_id,
            'new_test_username',
        )
        self.assertTrue(result)

    @pytest.mark.asyncio
    async def test_delete_item(self):
        user_id = self.controller_test.select_user_by_name('new_test_username')
        result = self.controller_test.delete_user(user_id)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
