#!/usr/bin/env python
from collections import Counter

"""
@author bvanderlaan
"""


class ProfileResponse:
    def __init__(self, original, total_watchers, forked, languages, repo_topics):
        self.original = original
        self.total_watchers = total_watchers
        self.forked = forked
        self.languages = languages
        self.repo_topics = repo_topics

    def json_format(self):
        return {
            "total_repos": {"forked": self.forked, "original": self.original},
            "total_watchers": self.total_watchers,
            "languages": self.get_counts(self.languages),
            "repo_topics": self.get_counts(self.repo_topics),
        }

    def get_counts(self, items):
        """
        Counts the items and returns as list of dicts
        :param items: list of items
        :return: list of dicts with each dict {item: val}
        """
        return [
            {count: val}
            for count, val in dict(
                Counter([item.lower() for item in items if item])
            ).items()
        ]
