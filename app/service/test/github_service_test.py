#!/usr/bin/env python

from app.service.github_service import GithubService

"""
@author bvanderlaan
"""


class TestGithubService:
    def test_parse_response(self):
        gs = GithubService()
        response = (
            '[{"forks_count": 23, "watchers": 11, "language": "python", "name": "repo1"},'
            '{"forks_count": 33, "watchers": 22, "language": "java", "name": "repo2"}]'
        )
        expected = {
            "forked": 56,
            "languages": ["python", "java"],
            "original": 2,
            "repo_topics": ["repo1", "repo2"],
            "total_watchers": 33,
        }
        assert expected == gs.parse_response(response)
