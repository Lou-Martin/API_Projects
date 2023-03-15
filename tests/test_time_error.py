from lib.time_error import TimeError
from unittest.mock import Mock

'''

unit test using mock as requester and mock as response
calling #error displays the difference in seconds between the time on an external server and the local time

'''

def test_error_returns_difference_in_seconds_between_server_time_and_local_time():
    # create mock requester and mock response
    mock_requester = Mock()
    mock_response = Mock()
    
    # set the mock requester to return a mock response
    mock_requester.get.return_value = mock_response

    # set the mock response to return a specific json object
    mock_response.json.return_value = {"unixtime": 1616700000}

    # create an instance of the TimeError class using the mock requester
    time_error = TimeError(mock_requester)

    # set the time variable to a predetermined value rather than using the time module
    time_error.time = 1615700000

    # set the result variable to the predetermined return value of the error method
    result = time_error.error()

    # Assert result is equal to the predetermined return value
    assert result == 1616700000 - time_error.time