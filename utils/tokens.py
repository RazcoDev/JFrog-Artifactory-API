from copy import copy
from interfaces.jfrog_api import JfrogAPI


def set_token_to_client(client: JfrogAPI, token: str) -> JfrogAPI:
    tokenized_client = copy(client)
    tokenized_client.token = token
    return tokenized_client
