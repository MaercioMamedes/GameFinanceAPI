from django.contrib import auth
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class Logout(APIView):

    def get(self, request):
        auth.logout(self.request)
        api_root_url = reverse('api-root', request=self.request)
        return Response(status=302, headers={'Location': api_root_url})
