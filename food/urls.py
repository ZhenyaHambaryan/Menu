from django.urls import path
from rest_framework import urlpatterns, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodViewSet, FoodTypeViewSet, FoodCategoryViewSet, PlateSectionViewSet, PlateLayoutViewSet, PlateViewSet,\
                                IngredientsViewSet,SubscribeViewSet,SectionLayoutViewSet,BoxViewSet,PlateDrinkViewSet,PlateDessertViewSet,\
                                PlateFoodViewSet,PlateDaysViewSet,TransactionViewSet,RequestToCancelViewSet,TakeViewSet,TimeIntervalViewSet
from food import views



time_interval_list = TimeIntervalViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

time_interval_detail = TimeIntervalViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

take_list = TakeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

take_detail = TakeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


request_to_cancel_list = RequestToCancelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

request_to_cancel_detail = RequestToCancelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


transaction_list = TransactionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

transaction_detail = TransactionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


plate_days_list = PlateDaysViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

plate_days_detail = PlateDaysViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


plate_food_list = PlateFoodViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

plate_food_detail = PlateFoodViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


plate_dessert_list = PlateDessertViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

plate_dessert_detail = PlateDessertViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

plate_drink_list = PlateDrinkViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

plate_drink_detail = PlateDrinkViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



box_list = BoxViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

box_detail = BoxViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



section_layout_list = SectionLayoutViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

section_layout_detail = SectionLayoutViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


subscribe_list = SubscribeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

subscribe_detail = SubscribeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

ingredients_list = IngredientsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

ingredients_detail = IngredientsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

food_list = FoodViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

food_detail = FoodViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

food_type_list = FoodTypeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

food_type_detail = FoodTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

food_category_list = FoodCategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

food_category_detail = FoodCategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

plate_section_list = PlateSectionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

plate_section_detail = PlateSectionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

plate_layout_list = PlateLayoutViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

plate_layout_detail = PlateLayoutViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

plate_list = PlateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

plate_detail = PlateViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [

    # verchacrac yev test arac:
    path('food/api', views.api_root),
    path('foods/', food_list, name='food-list'),
    path('foods/<int:pk>/', food_detail, name='food-detail'),
    path('ingredients/', ingredients_list, name='ingredients-list'),
    path('ingredients/<int:pk>/', ingredients_detail, name='ingredients-detail'),
    path('food_types/', food_type_list, name='food-type-list'),
    path('food_types/<int:pk>/', food_type_detail, name='food-type-detail'),
    path('food_categories/', food_category_list, name='food-category-list'),
    path('food_categories/<int:pk>/', food_category_detail, name='food-category-detail'),
    path('plate_sections/',plate_section_list, name='plate-section-list'),
    path('plates_sections/<int:pk>/', plate_section_detail, name='plate-section-detail'),
    path('plate_layouts/',plate_layout_list, name='plate-layout-list'),
    path('plate_layouts/<int:pk>/', plate_layout_detail, name='plate-layout-detail'),
    path('plates/',plate_list, name='plate-list'),
    path('plates/<int:pk>/', plate_detail, name='plate-detail'),
    path('subscribe/', subscribe_list, name='subscribe-list'),
    path('subscribe/<int:pk>/', subscribe_detail, name='subscribe-detail'),
    path('section_layout/', section_layout_list, name='section-layout-list'),
    path('section_layout/<int:pk>/', section_layout_detail, name='section-layout-detail'),
    path('box/', box_list, name='box-list'),
    path('box/<int:pk>/', box_detail, name='box-detail'),
    path('plate_drink/', plate_drink_list, name='plate-drink-list'),
    path('plate_drink/<int:pk>/', plate_drink_detail, name='plate-drink-detail'),
    path('plate_dessert/', plate_dessert_list, name='plate-dessert-list'),
    path('plate_dessert/<int:pk>/', plate_dessert_detail, name='plate-dessert-detail'),
    path('plate_food/', plate_food_list, name='plate-food-list'),
    path('plate_food/<int:pk>/', plate_food_detail, name='plate-food-detail'),
    path('plate_days/', plate_days_list, name='plate-days-list'),
    path('plate_days/<int:pk>/', plate_days_detail, name='plate-days-detail'),
    path('transaction/', transaction_list, name='transaction-list'),
    path('transaction/<int:pk>/',transaction_detail, name='transaction-detail'),
    path('request_to_cancel/', request_to_cancel_list, name='request-to-cancel-list'),
    path('request_to_cancel/<int:pk>/', request_to_cancel_detail, name='request-to-cancel-detail'),
    path('take/', take_list, name='take-list'),
    path('take/<int:pk>/', take_detail, name='take-detail'),
    path('time_interval/', time_interval_list, name='time-interval-list'),
    path('time_interval/<int:pk>/', time_interval_detail, name='time-interval-detail'),
    path('filtered_foods/', views.filtered_foods, name='filtered_foods'),
    path('filtered_drinks/', views.filtered_drinks, name='filtered_drinks'),
    path('filtered_desserts/', views.filtered_desserts, name='filtered_desserts'),
    path('filtered_all/', views.filtered_all, name='filtered_all'),

    # testing petk uni:

    # path('add_fave_food', views.add_fave_food, name='add-fave-food'),
    # path('remove_fave_food', views.remove_fave_food, name='remove-fave-food'),
# <<<<<<< HEAD
    # path('create_plate', views.create_plate, name='create-plate'),
# =======
# >>>>>>> 42705e4f5c377539f565ca1b218a3bd32246934d

    # chi sksvac:


]

urlpatterns = format_suffix_patterns(urlpatterns)
