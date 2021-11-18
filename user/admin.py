from django.contrib import admin
from user.models import UserDetail,ContactUs,Team,UserTeam,RequestTeam


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','email','subject','message')

admin.site.register(UserDetail)
admin.site.register(Team)
admin.site.register(UserTeam)
admin.site.register(RequestTeam)

# Register your models here.
