# JFrog Artifactory API

This WSGI performs some demo actions on JFrog Artifactory using its REST API.


## Installation

```
git clone https://github.com/RazcoDev/JFrog-Artifactory-API.git
pip install -r requirements.txt

```


## Usage
First, Set-up the environment needed variables, for example: 
```
export TIMEOUT=3
export ARTIFACTORY_URL=https://razinteg.jfrog.io/artifactory
```
And then, run the web server:
```
uvicorn main:app --reload
```

