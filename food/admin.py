from django.contrib import admin
from food.models import FoodCategory,FoodType,Food,Ingredients,PlateSection,PlateLayout,Plate,Subscribe,RequestToCancel,PlateDrink,PlateDessert,\
                        PlateFood,Take,SectionLayout,PlateDays,Box
from django.db.models import Count
from django.db.models import F,Q
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.urls import path
import json


class TabularInlineDrink(admin.TabularInline):
    model=PlateDrink
    # extra = 1
    fields = ['plate','drink','count','remainder']
    readonly_fields = ['remainder']
    def remainder(self, instance):
        q   = instance.count-instance.drink.take_food.filter(plate=instance.plate).count()
        return q
    remainder.short_description = 'remainder'


class TabularInlineDessert(admin.TabularInline):
    model=PlateDessert
    # extra = 1
    fields = ['plate','dessert','count','remainder']
    readonly_fields = ['remainder']
    def remainder(self, instance):
        q   = instance.count-instance.dessert.take_food.filter(plate=instance.plate).count()
        return q
    remainder.short_description = 'remainder'


class TabularInlineFood(admin.TabularInline):
    model=PlateFood
    # extra = 1
    fields = ['plate','food','section_layout','count','remainder']
    readonly_fields = ['remainder']
    def remainder(self, instance):
        q   = instance.count-instance.food.take_food.filter(plate=instance.plate).count()
        return q
    remainder.short_description = 'remainder'


@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    list_display = ('description','created_at','user','layout','price')
    readonly_fields = ('price',)
    inlines = [TabularInlineDrink,TabularInlineDessert,TabularInlineFood]



@admin.register(RequestToCancel)
class RequestToCancelAdmin(admin.ModelAdmin):
    list_display = ('user','subscribe','description','status')
    list_filter = ('user','subscribe','description','status')
    readonly_fields = ('user','subscribe','description')


admin.site.register(FoodCategory)
admin.site.register(FoodType)
admin.site.register(Food)
admin.site.register(Ingredients)
admin.site.register(PlateSection)
admin.site.register(PlateLayout)
admin.site.register(SectionLayout)
admin.site.register(Subscribe)
admin.site.register(Take)
admin.site.register(PlateDrink)
admin.site.register(PlateDessert)
admin.site.register(PlateFood)
admin.site.register(PlateDays)
admin.site.register(Box)





# Register your models here.
