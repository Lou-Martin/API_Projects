#File: lib/api_exercise.py

class ActivitySuggester:
    def __init__(self, requester):
        self.requester = requester

    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not go {response['activity']}?"
    
    #This method calls an API on the internet to get a random activity.
    #An API is a way of allowing programs to request data from other programs.
    def _make_request_to_api(self):
        response = self.requester.get("http://www.boredapi.com/api/activity/")
        return response.json()
    

# Usage
import requests
activity_suggester = ActivitySuggester(requests)
#activity_suggester.suggest() will return a different value every time it is called. eg. "Why not go try skydiving?"

print(activity_suggester.suggest())
# Why not go skydiving?

print(activity_suggester.suggest())
# Why not go go-karting?