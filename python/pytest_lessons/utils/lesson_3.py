from loguru import logger
import requests 
from requests.exceptions import HTTPError
from datetime import datetime

class SomeResourceClient:
    def __init__(self, url: str):
        self.url = url 

    def _user_get_status(self, user_id: int) -> dict:
        current_url = f"{self.url}/web/user/get-status/{user_id}"
        response = requests.get(current_url)
        if response.status_code == 200: 
            return response.json()
        else: 
            raise HTTPError(f'{response.status_code = }')


    def user_get_last_action_time(self, user_id):
        res = self._user_get_status(user_id)
        logger.debug(f'{res = }')
        return datetime.fromtimestamp(res.get("timeDiff")) 