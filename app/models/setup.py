from . import check
from .user import setup_user_table
from .item import setup_item_table


async def check_db(
        db_user: str | None,
        db_pass: str | None,
        db_host: str | None,
        db_port: str | None,
        db_name: str | None,
        db_url: str | None
) -> bool:
    # Check if all necessary environ variables has been set
    if None in [db_user, db_pass, db_host, db_port, db_url]:
        return False
    # Check if you can connect to the database
    if not check.check_db_connection(db_url):
        return False
    # If table does not exist, create it
    # User
    if not setup_user_table(db_url):
        return False
    # Comment
    if not setup_item_table(db_url):
        return False

    return True
