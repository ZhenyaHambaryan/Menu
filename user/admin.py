from django.contrib import admin
from user.models import UserDetail,Organization,ContactUs


admin.site.register(ContactUs)
admin.site.register(UserDetail)
admin.site.register(Organization)
# Register your models here.
