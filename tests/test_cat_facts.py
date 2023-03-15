from lib.cat_facts import CatFacts
from unittest.mock import Mock

'''

using mock as requester and mock as response
calling #provide returns a cat fact

'''

def test_provide_returns_a_cat_fact():
    # create mock requester and mock response
    mock_requester = Mock()
    mock_response = Mock()

    # set the mock requester to return a mock response
    mock_requester.get.return_value = mock_response

    # set the mock response to return a specific json object
    mock_response.json.return_value = {"fact": "Cats are equally as awesome as dogs - people need to stop getting so hung up on whether they're a cat person or a dog person."}

    # create an instance of the CatFacts class using the mock requester
    cat_facts = CatFacts(mock_requester)

    # set the result variable to the predetermined return value of the provide method
    result = cat_facts.provide()

    # Assert result is equal to the predetermined return value
    assert result == "Cat fact: Cats are equally as awesome as dogs - people need to stop getting so hung up on whether they're a cat person or a dog person."