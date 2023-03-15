from lib.api_exercise import ActivitySuggester
from unittest.mock import Mock

'''

when we call the suggest method
an activity is returned

'''

def test_suggest_returns_an_activity():
    # create mock requester and mock response
    mock_requester = Mock()
    mock_response = Mock()

    # set the mock requester to return a mock response
    mock_requester.get.return_value = mock_response

    # set the mock response to return a specific json object
    mock_response.json.return_value = {"activity": "skydiving"}

    # create an instance of the ActivitySuggester class using the mock requester
    activity_suggester = ActivitySuggester(mock_requester)

    # set the result variable to the predetermined return value of the suggest method
    result = activity_suggester.suggest()

    # Assert result is equal to the predetermined return value
    assert result == "Why not go skydiving?"
