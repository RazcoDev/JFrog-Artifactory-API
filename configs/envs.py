from os import environ

TIMEOUT = int(environ.get("TIMEOUT"))

ARTIFACTORY_URL = environ.get("ARTIFACTORY_URL") + '/' if environ.get("ARTIFACTORY_URL")[-1] != '/' else environ.get(
    "ARTIFACTORY_URL")
