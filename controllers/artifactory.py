from interfaces.jfrog_api import JfrogAPI
from configs import endpoints
import json


def get_health_ping(client: JfrogAPI) -> dict:
    try:
        endpoint = endpoints.HEALTH_PING
        res = client.request(endpoint['method'].value, endpoint['url'])
        if res['success']:
            if res['ok']:
                return {"jfrog_alive": True}
            else:
                return {"jfrog_alive": False, "error": res['response'].status_code, "message": res['message']}
        else:
            return {"jfrog_alive": False, "error": res['error']}

    except Exception as e:
        return {"jfrog_alive": False, "error": "unknown exception"}


def get_system_version(client: JfrogAPI) -> dict:
    try:
        endpoint = endpoints.SYSTEM_VERSION
        res = client.request(endpoint['method'].value, endpoint['url'])
        if res['success']:
            if res['ok']:
                response_json = json.loads(res['response'].content)
                if "version" in response_json.keys():
                    return {"version": response_json['version']}
                else:
                    return {"error": "no version"}
            else:
                return {"error": res['response'].status_code, "message": res['message']}
        else:
            return {"error": res['error']}

    except Exception as e:
        return {"error": "unknown exception"}


def user_handling_by_name(client: JfrogAPI, username: str, email: str, password: str,
                          is_deletion: bool = False) -> dict:
    try:
        if is_deletion:
            endpoint = endpoints.DELETE_USER
        else:
            endpoint = endpoints.CREATE_USER
        data = {"email": email, "password": password}
        res = client.request(endpoint['method'].value, endpoint['url'].format(username), data)
        if res['success']:
            if res['ok']:
                return {"succeed": True}
            else:
                return {"error": res['response'].status_code, "message": res['message']}
        else:
            return {"error": res['error']}

    except Exception as e:
        return {"error": "unknown exception"}


def get_storage_info(client: JfrogAPI) -> dict:
    try:
        endpoint = endpoints.STORAGE_INFO
        res = client.request(endpoint['method'].value, endpoint['url'])
        if res['success']:
            if res['ok']:
                return {"succeed": True, "data": json.loads(res['response'].content)}
            else:
                return {"error": res['response'].status_code, "message": res['message']}
        else:
            return {"error": res['error']}

    except Exception as e:
        return {"error": "unknown exception"}
