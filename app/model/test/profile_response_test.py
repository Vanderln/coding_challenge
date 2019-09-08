#!/usr/bin/env python
from app.model.profile_response import ProfileResponse

"""
@author bvanderlaan
"""


class TestProfileResponse:
    def test_count_languages(self):
        pr = ProfileResponse(
            1,
            2,
            3,
            ["Java", "java", "Python", "Ruby"],
            ["Java is coffee", "Ruby is shiny", "Python is slippery"],
        )
        expected = [{"java": 2}, {"python": 1}, {"ruby": 1}]
        assert expected == pr.get_counts(pr.languages)

    def test_count_languages_empty(self):
        pr = ProfileResponse(
            1, 2, 3, [], ["Java is coffee", "Ruby is shiny", "Python is slippery"]
        )
        expected = []
        assert expected == pr.get_counts(pr.languages)

    def test_json_format(self):
        pr = ProfileResponse(
            1,
            2,
            3,
            ["Java", "Python", "Ruby"],
            ["Java is coffee", "Ruby is shiny", "Python is slippery"],
        )
        expected = {
            "languages": [{"java": 1}, {"python": 1}, {"ruby": 1}],
            "repo_topics": [
                {"java is coffee": 1},
                {"ruby is shiny": 1},
                {"python is slippery": 1},
            ],
            "total_repos": {"forked": 3, "original": 1},
            "total_watchers": 2,
        }
        assert expected == pr.json_format()

    def test_json_format_empty(self):
        pr = ProfileResponse(0, 0, 0, [], [])
        expected = {
            "languages": [],
            "repo_topics": [],
            "total_repos": {"forked": 0, "original": 0},
            "total_watchers": 0,
        }
        assert expected == pr.json_format()
