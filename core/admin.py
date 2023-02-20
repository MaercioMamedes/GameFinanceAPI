from django.contrib import admin
from core.models import Wallet, Paper


class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'b3_code', 'company_name', 'last_value')


admin.site.register(Paper, PaperAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'paper')


admin.site.register(Wallet, WalletAdmin)



