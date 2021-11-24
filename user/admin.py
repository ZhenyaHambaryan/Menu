from django.contrib import admin
from user.models import UserDetail,ContactUs,Team,UserTeam,RequestTeam,ConfirmCode,RecoverEmail


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','email','subject','message')

admin.site.register(UserDetail)
admin.site.register(Team)
admin.site.register(UserTeam)
admin.site.register(RequestTeam)
admin.site.register(ConfirmCode)
admin.site.register(RecoverEmail)


# Register your models here.
