# Coding Challenge App

A skeleton flask app to use for a coding challenge.

## Install:
```
You can use a virtual environment (venv, etc):
virtualenv env
source env/bin/activate
pip install -r requirements.txt

```

## Running the code
```
Add your bitbucket username and passport to the json object in app/config/config.json
```

### Spin up the service

```
# start up local server
python -m run 
```

### Making Requests

```
curl -i "http://127.0.0.1:5000/health-check"

To get your code profile, pass a github_org and a bitbucket_team 
as query params as shown in this example:

curl -i "http://127.0.0.1:5000/code-profile?bitbucket_team=mailchimp&github_org=mailchimp"
```

### To run the tests
```
python -m pytest
```


## What'd I'd like to improve on...
```
1.) Passing the config file path as an arg
2.) Testing the get_profile methods of the service classes
3.) DRYing up the test classes with a setUp method or two
```
