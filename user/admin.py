from django.contrib import admin
from user.models import UserDetail,Team,UserTeam,RequestTeam,ConfirmCode,RecoverEmail



admin.site.register(UserDetail)
admin.site.register(Team)
admin.site.register(UserTeam)
admin.site.register(RequestTeam)
admin.site.register(ConfirmCode)
admin.site.register(RecoverEmail)


# Register your models here.
