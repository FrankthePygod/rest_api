from rest_framework.views import APIView
from rest_framework.response import Response

## this will be the endpoint where the urls.py file will reference and call to output
## so much potential for this website to show things!

class HelloApiView(APIView):
    """Test the API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Users HTTP methods as function (get, post, patch, put delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
