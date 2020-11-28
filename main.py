from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from controllers.artifactory import get_health_ping, get_system_version, user_handling_by_name, get_storage_info
from interfaces.jfrog_api import JfrogAPI
from utils.tokens import set_token_to_client
from configs.envs import ARTIFACTORY_URL

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
client = JfrogAPI(ARTIFACTORY_URL)


@app.get("/")
def read_root():
    return {"Info": "JFrog Artifactory API, feel free to go /docs for more information about the API !"}


@app.get("/artifactory_health")
def artifactory_health(token: str = Depends(oauth2_scheme)):
    tokenized_client = set_token_to_client(client, token)
    return get_health_ping(tokenized_client)


@app.get("/artifactory_version")
def artifactory_version(token: str = Depends(oauth2_scheme)):
    tokenized_client = set_token_to_client(client, token)
    return get_system_version(tokenized_client)


@app.put("/users/{username}")
def create_user(username: str, email: str, password: str, token: str = Depends(oauth2_scheme)):
    tokenized_client = set_token_to_client(client, token)
    return user_handling_by_name(tokenized_client, username, email, password)


@app.delete("/users/{username}")
def delete_user(username: str, email: str, password: str, token: str = Depends(oauth2_scheme)):
    tokenized_client = set_token_to_client(client, token)
    return user_handling_by_name(tokenized_client, username, email, password, is_deletion=True)


@app.get("/storage/info")
def storage_info(token: str = Depends(oauth2_scheme)):
    tokenized_client = set_token_to_client(client, token)
    return get_storage_info(tokenized_client)
