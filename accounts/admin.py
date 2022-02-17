from pyexpat import model
from django.contrib  import admin
from accounts.models import Accounts
from django.contrib.auth.models import User
from django.contrib.auth.admin  import UserAdmin

class AccountInline(admin.StackedInline):
    model               =  Accounts
    can_delete          =  False
    verbose_name_plural = 'Custom fields'

class CustomUserAdmin (UserAdmin): 
    inlines = (AccountInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# admin.site.register(Accounts) # we don't want custom fields maintained in isolation
