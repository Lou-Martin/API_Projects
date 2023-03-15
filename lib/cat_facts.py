#File lib/cat_facts.py



class CatFacts:
    def __init__(self, requester):
        self.requester = requester

    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self.requester.get("https://catfact.ninja/fact")
        return response.json()


# Usage
import requests
cat_facts = CatFacts(requests)
print(cat_facts.provide())
print(cat_facts.provide())