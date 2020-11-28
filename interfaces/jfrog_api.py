import json
from enum import Enum
import requests
from configs.envs import TIMEOUT


class RequestMethod(Enum):
    Get = "get"
    Post = "post"
    Put = "put"
    Delete = "delete"


class JfrogAPI:
    def __init__(self, api_url, token=None):
        self.api_url = api_url
        self.token = token

    def request(self, method, endpoint_url, data=None):
        try:
            headers = {"Authorization": f"Bearer {self.token}"}

            response = requests.request(method, self.api_url + endpoint_url, timeout=TIMEOUT, json=data,
                                        headers=headers)
            if response.ok:
                return {"success": True, "ok": True, "response": response}
            else:
                message = json.loads(response.content)['errors'][0]["message"]
                return {"success": True, "ok": False, "response": response, "message": message}

        except requests.exceptions.ConnectTimeout:
            return {"success": False, "error": "timeout"}

        except Exception as e:
            return {"success": False, "error": e}
