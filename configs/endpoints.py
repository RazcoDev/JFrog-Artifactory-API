from interfaces.jfrog_api import RequestMethod

HEALTH_PING = {"url": "api/system/ping", "method": RequestMethod.Get}
SYSTEM_VERSION = {"url": "api/system/version", "method": RequestMethod.Get}
CREATE_USER = {"url": "api/security/users/{}", "method": RequestMethod.Put}
DELETE_USER = {"url": "api/security/users/{}", "method": RequestMethod.Delete}
STORAGE_INFO = {"url": "api/storageinfo", "method": RequestMethod.Get}
