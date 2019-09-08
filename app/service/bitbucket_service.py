#!/usr/bin/env python

from json import loads

from app.model.profile_response import ProfileResponse
from app.requestor import each_delegate, make_call

HEADERS = {"Content-Type": "application/json"}

"""
Service to handle Bitbucket

@author bvanderlaan
"""


class BitbucketService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_profile(self, team):
        return ProfileResponse(
            **self.parse_repos(
                make_call(
                    "https://bitbucket.org/api/2.0/repositories/{}".format(team),
                    HEADERS,
                    "bitbucket",
                    username=self.username,
                    password=self.password,
                ).content
            )
        )

    def parse_repos(self, response):
        """
        Method to extract original repo count, forks count, watcher count,
        languages and repo_topics from the repositories endpoint

        :param response:  The json response from bitbucket
        :return: dict
        """
        values = loads(response).get("values", [])
        forks = []
        watchers = []
        languages = []
        repo_topics = []
        for repo in values:
            watchers.extend(repo["links"]["watchers"].values())
            forks.extend(repo["links"]["forks"].values())
            languages.append(repo.get("language"))
            repo_topics.append(repo.get("full_name"))
        return {
            "original": len(values),
            "forked": self.get_total(
                each_delegate(
                    make_call,
                    forks,
                    HEADERS,
                    "bitbucket",
                    username=self.username,
                    password=self.password,
                )
            ),
            "total_watchers": self.get_total(
                each_delegate(
                    make_call,
                    watchers,
                    HEADERS,
                    "bitbucket",
                    username=self.username,
                    password=self.password,
                )
            ),
            "languages": [l for l in languages if l],
            "repo_topics": repo_topics,
        }

    def get_total(self, responses):
        return sum([loads(response).get("size", 0) for response in responses])
