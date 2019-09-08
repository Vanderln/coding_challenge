import flask
import logging
import traceback
from app.service.bitbucket_service import BitbucketService
from app.service.response_aggregator import ResponseAggregator
from app.service.github_service import GithubService

from flask import Response, jsonify, request
from json import load

app = flask.Flask("user_profiles_api")
# TODO: make this file path an arg
app.config.update(load(open("app/config/config.json")))
logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)


SERVICES = {
    "github_service": GithubService(),
    "bitbucket_service": BitbucketService(
        app.config.get("bitbucket_user"), app.config.get("bitbucket_password")
    ),
}
RESPONSE_AGGREGATOR = ResponseAggregator(**SERVICES)


@app.errorhandler(Exception)
def http_error_handler(error):
    message = traceback.format_exc()
    response = jsonify({"message": error.args[0]})
    response.status_code = 500
    logger.error(message)
    return response


@app.route("/health-check", methods=["GET"])
def health_check():
    """
    Endpoint to health check API
    """
    app.logger.info("Health Check!")
    return Response("All Good!", status=200)


@app.route("/code-profile", methods=["GET"])
def profile():
    """
    Endpoint to gather github + bitbucket code profile

    :param org_name:  the org/team with which to search
    :return: json profile
    """
    return jsonify(
        RESPONSE_AGGREGATOR.get_profile(
            request.args.get("github_org"), request.args.get("bitbucket_team")
        )
    )
