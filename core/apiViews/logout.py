from django.contrib import auth
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class Logout(APIView):
    @staticmethod
    def get(request):
        auth.logout(request)
        print(request.user)
        api_root_url = reverse('api-root', request=request)
        return Response(status=302, headers={'Location': api_root_url})
