#!/usr/bin/env python

from app.util import combine_objects

"""
Class to aggregate responses from services

@author bvanderlaan
"""


class ResponseAggregator:
    def __init__(self, **kwargs):
        self.github_service = kwargs.get("github_service")
        self.bitbucket_service = kwargs.get("bitbucket_service")

    def get_profile(self, org, team):
        """
        Calls each service and combines each ProfileResponse objects into one

        :param org: the github org
        :param team: the bitbucket team/org
        :return: a combined ProfileResponse object
        """
        github_response = self.github_service.get_profile(org)
        bitbucket_response = self.bitbucket_service.get_profile(team)
        return combine_objects(github_response, bitbucket_response).json_format()
