from django.contrib import admin
from core.models import Wallet, UserWallet, Paper


class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'b3_code', 'company_name', 'last_value')


admin.site.register(Paper, PaperAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'paper')


admin.site.register(Wallet, WalletAdmin)


class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'initial_value','final_value','profit')


admin.site.register(UserWallet, UserWalletAdmin)
