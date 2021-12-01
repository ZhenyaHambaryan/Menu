from django.contrib import admin
from .models import Slide,ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','email','subject','message')


admin.site.register(Slide)

# Register your models here.
