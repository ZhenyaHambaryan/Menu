from django.contrib import admin
from food.models import FoodCategory,FoodType,Food,Ingredients,PlateSection,PlateLayout,Plate,Subscribe,RequestToCancel


admin.site.register(FoodCategory)
admin.site.register(FoodType)
admin.site.register(Food)
admin.site.register(Ingredients)
admin.site.register(PlateSection)
admin.site.register(PlateLayout)
admin.site.register(Plate)
admin.site.register(Subscribe)
@admin.register(RequestToCancel)
class RequestToCancelAdmin(admin.ModelAdmin):
    list_display = ('user','subscribe','description','status')
    list_filter = ('user','subscribe','description','status')
    readonly_fields = ('user','subscribe','description')


# Register your models here.
