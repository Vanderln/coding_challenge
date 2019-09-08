from unittest import mock

from app.service.response_aggregator import ResponseAggregator
from app.model.profile_response import ProfileResponse

"""
@author bvanderlaan
"""


class TestResponseAggregator:
    def test_get_profile(self):
        github_mock = mock.MagicMock()
        github_mock.get_profile = mock.MagicMock()
        github_mock.get_profile.return_value = ProfileResponse(
            1, 1, 1, ["l1"], ["topic1"]
        )
        bitbucket_mock = mock.MagicMock()
        bitbucket_mock.get_profile = mock.MagicMock()
        bitbucket_mock.get_profile.return_value = ProfileResponse(
            2, 2, 2, ["l2", "l3"], ["topic2", "topic3"]
        )
        ra = ResponseAggregator(
            **{"github_service": github_mock, "bitbucket_service": bitbucket_mock}
        )
        expected = ProfileResponse(
            3, 3, 3, ["l1", "l2", "l3"], ["topic1", "topic2", "topic3"]
        ).json_format()
        actual = ra.get_profile("org1", "team1")
        assert expected == actual
