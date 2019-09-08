#!/usr/bin/env python

from json import loads

from app.model.profile_response import ProfileResponse
from app.requestor import make_call

HEADERS = {"Content-Type": "application/json"}

"""
Service to handle Github 

@author bvanderlaan
"""


class GithubService:
    def get_profile(self, org):
        return ProfileResponse(
            **self.parse_response(
                make_call(
                    "https://api.github.com/orgs/{}/repos".format(org),
                    HEADERS,
                    "Github",
                ).content
            )
        )

    def parse_response(self, response):
        """
        Extracts original_repo_count, total_watchers, forks, languages, and repo_topics
        :param response: the json response from github
        :return: dict
        """
        original_repo_count = 0
        total_watchers = 0
        forks = 0
        languages = []
        repo_topics = []
        for item in loads(response):
            original_repo_count += 1
            total_watchers += item.get("watchers", 0)
            forks += item.get("forks_count", 0)
            languages.append(item.get("language"))
            repo_topics.append(item.get("name"))
        return {
            "original": original_repo_count,
            "forked": forks,
            "total_watchers": total_watchers,
            "languages": languages,
            "repo_topics": repo_topics,
        }
