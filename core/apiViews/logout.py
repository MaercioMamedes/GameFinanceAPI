from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Logout(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


    def post(self, request, format=None):
        # Desativar a autenticação básica para a sessão atual
        self.request.session.flush()
        return Response(status=204)
