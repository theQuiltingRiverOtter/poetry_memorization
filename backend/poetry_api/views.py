from rest_framework.views import APIView
from rest_framework.response import Response
import requests  # <== import requests so we can utilize it within our CBV to make API calls
from requests_oauthlib import (
    OAuth1,
)  # <== import OAuth1 which will essentially authenticate our keys when we send a request
import json


class Poems_By_Author(APIView):
    # In our CBV lets create a method to interact with the NounAPI
    def get(self, request, author):
        try:
            endpoint = f"https://poetrydb.org/author/{author}"

            response = requests.get(endpoint)
            responseJSON = response.json()
            return Response(responseJSON)
        except:
            return Response("That author wasn't found")


class Poems_By_Title(APIView):
    # In our CBV lets create a method to interact with the NounAPI
    def get(self, request, title):
        try:
            endpoint = f"https://poetrydb.org/title/{title}"

            response = requests.get(endpoint)
            responseJSON = response.json()
            return Response(responseJSON)
        except:
            return Response("That title wasn't found")
