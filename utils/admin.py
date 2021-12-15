from django.contrib import admin
from .models import Slide,ContactUs,TimeInterval,Images


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','email','subject','message')


admin.site.register(Slide)
admin.site.register(TimeInterval)
admin.site.register(Images)

# Register your models here.
