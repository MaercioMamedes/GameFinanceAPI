from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Wallet
from core.helpers import update_values


class CalculatorView(APIView):

    def post(self, request):
        print(self.request.data)
        if 'period' not in self.request.data.keys():
            raise Exception("deu ruim")

        papers = []
        wallets = Wallet.objects.all()
        for wallet in wallets:
            if wallet.paper not in papers:
                papers.append(wallet.paper)

        for paper in papers:
            update_values(paper, self.request.data['period'])

        return Response(status=200)
