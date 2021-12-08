from django.contrib import admin
from food.models import FoodCategory,FoodType,Food,Ingredients,PlateSection,PlateLayout,Plate,Subscribe,RequestToCancel,PlateDrink,PlateDessert,\
                        PlateFood,Take,TimeInterval,SectionLayout,PlateDays
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

# @admin.register(Subscribe)
# class SubscribeAdmin(admin.ModelAdmin):
#     list_display = ("id", "price", "created_at")
#     ordering = ("-created_at",)
#
#     # Inject chart data on page load in the ChangeList view
#     def changelist_view(self, request, extra_context=None):
#         chart_data = self.chart_data()
#         as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
#         extra_context = extra_context or {"chart_data": as_json}
#         return super().changelist_view(request, extra_context=extra_context)
#
#     def get_urls(self):
#         urls = super().get_urls()
#         extra_urls = [
#             path("chart_data/", self.admin_site.admin_view(self.chart_data_endpoint))
#         ]
#         # NOTE! Our custom urls have to go before the default urls, because they
#         # default ones match anything.
#         return extra_urls + urls
#
#     # JSON endpoint for generating chart data that is used for dynamic loading
#     # via JS.
#     def chart_data_endpoint(self, request):
#         chart_data = self.chart_data()
#         return JsonResponse(list(chart_data), safe=False)
#
#     def chart_data(self):
#         return (
#             Subscribe.objects.annotate(date=TruncDay("created_at"))
#             .values("date")
#             .annotate(y=Count("id"))
#             .order_by("-date")
#         )



admin.site.register(FoodCategory)
admin.site.register(FoodType)
admin.site.register(Food)
admin.site.register(Ingredients)
admin.site.register(PlateSection)
admin.site.register(PlateLayout)
admin.site.register(SectionLayout)
admin.site.register(Subscribe)
admin.site.register(Take)
admin.site.register(TimeInterval)
admin.site.register(PlateDrink)
admin.site.register(PlateDessert)
admin.site.register(PlateFood)
admin.site.register(PlateDays)




# Register your models here.
