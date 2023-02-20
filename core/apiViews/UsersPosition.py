from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Wallet
from django.contrib.auth.models import User


class UsersPositionView(APIView):

    @staticmethod
    def get(request):
        users_position = []
        users = User.objects.all()
        wallets = Wallet.objects.all()

        for user in users:
            user_wallet = wallets.filter(user=user)
            wallet = {
                'user': user.first_name,
                'first_value': 0,
                'last_value': 0,
                'profit':0,
            }
            for element in user_wallet:
                wallet['first_value'] += element.paper.first_value
                wallet['last_value'] += element.paper.last_value

            profit = (wallet['last_value'] - wallet['first_value'])/wallet['first_value']

            wallet['profit'] = round(profit, 5)
            users_position.append(wallet)

        return Response(users_position)
