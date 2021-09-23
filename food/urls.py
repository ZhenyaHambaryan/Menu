from django.urls import path
from rest_framework import urlpatterns, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodViewSet, FoodTypeViewSet, FoodCategoryViewSet, PlateSectionViewSet, PlateLayoutViewSet, PlateViewSet,\
                                IngredientsViewSet,SubscribeViewSet,SectionFoodViewSet,BoxViewSet,PlateDrinkViewSet
from food import views

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



section_food_list = SectionFoodViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

section_food_detail = SectionFoodViewSet.as_view({
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
    path('section_food/', section_food_list, name='section-food-list'),
    path('section_food/<int:pk>/', section_food_detail, name='section-food-detail'),
    path('box/', box_list, name='box-list'),
    path('box/<int:pk>/', box_detail, name='box-detail'),
    path('plate_drink/', plate_drink_list, name='plate_drink-list'),
    path('plate_drink/<int:pk>/', plate_drink_detail, name='plate_drink-detail'),

    # testing petk uni:

    path('add_fave_food', views.add_fave_food, name='add-fave-food'),
    path('remove_fave_food', views.remove_fave_food, name='remove-fave-food'),
# <<<<<<< HEAD
    # path('create_plate', views.create_plate, name='create-plate'),
# =======
# >>>>>>> 42705e4f5c377539f565ca1b218a3bd32246934d

    # chi sksvac:


]

urlpatterns = format_suffix_patterns(urlpatterns)
