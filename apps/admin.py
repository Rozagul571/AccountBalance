from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Wallet, Category

admin.site.site_header = "Account Balance Admin"
admin.site.site_title = "Account Balance Admin Portal"
admin.site.index_title = "Welcome to Account Balance Researcher Portal"


# admin.site.unregister(User)
# admin.site.unregister(Group)

@admin.register(Wallet)
class WalletAdmin(ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass
