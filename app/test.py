import unittest
import pytest

from app.models.controller import Controller, UserController


class ControllerTestCase(unittest.TestCase):
    controller_test = Controller()

    @pytest.mark.asyncio
    async def test_check_db(self):
        result = await self.controller_test.check_db()
        self.assertEqual(result, True)  # add assertion here


class UserControllerTestCase(unittest.TestCase):
    controller_test = UserController()

    @pytest.mark.asyncio
    async def test_create_user(self):
        result = await self.controller_test.create_user('test', 'test@test.com', 'test', False)
        self.assertEqual(result, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
