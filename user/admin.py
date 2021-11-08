from django.contrib import admin
from user.models import UserDetail,ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','email','subject','message')

admin.site.register(UserDetail)
# admin.site.register(Organization)
# Register your models here.
