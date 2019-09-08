#!/usr/bin/env python

from unittest import mock

from app.service.bitbucket_service import BitbucketService

"""
@author bvanderlaan
"""


class TestBitbucketService:
    def test_parse_repos(self):
        bbs = BitbucketService("test", "test")
        bbs.get_total = mock.MagicMock()
        bbs.get_total.return_value = 5

        response_json = (
            '{"pagelen": 2, "values": ['
            '{"scm": "git", "website": "http://mandrillapp.com/api/docs/", '
            '"has_wiki": "true", "uuid": "{19f1619f-eb24-4b89-ad87-3912c63b3f3d}", "links": '
            '{"watchers": {"href": "https://bitbucket.org/!api/2.0/repositories/mailchimp/mandrill-api-php/watchers"}, '
            '"forks": {"href": "https://bitbucket.org/!api/2.0/repositories/mailchimp/mandrill-api-php/forks"}, '
            '"downloads": {"href": "https://bitbucket.org/!api/2.0/repositories/mailchimp/mandrill-api-php/downloads"}, '
            '"fork_policy": "allow_forks", "name": "mandrill-api-php", '
            '"language": "php", "full_name": "mailchimp/mandrill-api-php"}}, '
            '{"scm": "git", "links": {"watchers": {"href": '
            '"https://bitbucket.org/!api/2.0/repositories/mailchimp/mandrill-api-python/watchers"}, '
            '"forks": {"href": "https://bitbucket.org/!api/2.0/repositories/mailchimp/mandrill-api-python/forks"}, '
            '"fork_policy": "allow_forks"}, "language": "python", "full_name": "mailchimp/mandrill-api-python"}], "page": 1, "size": 2}'
        )

        expected = {
            "forked": 5,
            "languages": ["python"],
            "original": 2,
            "repo_topics": [None, "mailchimp/mandrill-api-python"],
            "total_watchers": 5,
        }

        assert expected == bbs.parse_repos(response_json)

    def test_get_total(self):
        bbs = BitbucketService("test", "test")
        responses = [
            '{"pagelen":10, "values":[], "size": 1}',
            '{"pagelen":10, "values":[], "size": 2}',
        ]
        assert 3 == bbs.get_total(responses)
