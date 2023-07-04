from app.config.config import get_settings
from app.models.dao import SellerDAO


def test_config():
    assert 'user' == get_settings().db.DB_USER


async def test_dao():
    result = await SellerDAO.find_all()
    print(result)
