from user.models import UserDetail
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from food.serializers import FoodSerializer, FoodTypeSerializer, FoodCategorySerializer, PlateSectionSerializer, \
                                  PlateLayoutSerializer, PlateSerializer,IngredientsSerializer,SubscribeSerializer,SectionFoodSerializer,BoxSerializer,PlateDrinkSerializer
from food.models import Food, FoodType, FoodCategory, PlateSection, PlateLayout, Plate,Ingredients,Subscribe,SectionFood,Box,PlateDrink
# import django_filters
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination


class PlateDrinkViewSet(viewsets.ModelViewSet):
  queryset = PlateDrink.objects.all()
  serializer_class = PlateDrinkSerializer


class BoxViewSet(viewsets.ModelViewSet):
  queryset = Box.objects.all()
  serializer_class = BoxSerializer

class IngredientsViewSet(viewsets.ModelViewSet):
  queryset = Ingredients.objects.all()
  serializer_class = IngredientsSerializer
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['food',]

class FoodViewSet(viewsets.ModelViewSet):
  queryset = Food.objects.all()
  serializer_class = FoodSerializer
  # pagination_class = Food
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['food_type',]



class FoodTypeViewSet(viewsets.ModelViewSet):
  queryset = FoodType.objects.all()
  serializer_class = FoodTypeSerializer
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['food_category',]

class FoodCategoryViewSet(viewsets.ModelViewSet):
  queryset = FoodCategory.objects.all()
  serializer_class = FoodCategorySerializer

class PlateSectionViewSet(viewsets.ModelViewSet):
  queryset= PlateSection.objects.all()
  serializer_class = PlateSectionSerializer
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['category',]
  # def list(self, request, ):
  #   queryset = PlateSection.objects.all()
  #   paginator = PageNumberPagination()
  #   paginator.page_size = 10
  #   plate_section_id = request.GET.get("plate_section_id")
  #
  #   if plate_section_id is not None and plate_section_id != "":
  #     queryset = queryset.filter(plate_section_id=plate_section_id)
  #   sections = paginator.paginate_queryset(queryset, request)
  #   result = []
  #   for item in sections:
  #     data = PlateSectionSerializer(item).data
  #     data['sectionss'] = item.sections.filter(sections_id=request.sections.id).count() > 0
  #     result.append(data)
  #   return paginator.get_paginated_response(result)

class SectionFoodViewSet(viewsets.ModelViewSet):
  queryset = SectionFood.objects.all()
  serializer_class = SectionFoodSerializer


class PlateViewSet(viewsets.ModelViewSet):
  queryset = Plate.objects.all()
  serializer_class = PlateSerializer
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['layout','dessert',]


class PlateLayoutViewSet(viewsets.ModelViewSet):
  queryset = PlateLayout.objects.all()
  serializer_class = PlateLayoutSerializer
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['sections','sections__category']
  search_fields = ['name',]

class SubscribeViewSet(viewsets.ModelViewSet):
  queryset = Subscribe.objects.all()
  serializer_class = SubscribeSerializer
  permission_classes = [IsAuthenticated]
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['plate__user',]


  # def create(self, day_count, *args, **kwargs):
  #   serializer = SubscribeSerializer()
    # day_count = request.data['day_count']
    # drink = request.data['drink']
    # count = day_count//drink.count()
  #   if day_count%drink.count()==0:
  #     count = day_count/drink.count()
  #   else:
  #     for i in range(day_count%drink.count()):
  #       count = count + 1
  #   return Response(day_count, status=status.HTTP_201_CREATED)





@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'foods': reverse('food-list', request=request, format=format),
    'food_types': reverse('food-type-list', request=request, format=format),
    'food_categories': reverse('food-category-list', request=request, format=format),
    'plate_sections': reverse('plate-section-list', request=request, format=format),
    'plate_layouts': reverse('plate-layout-list', request=request, format=format),
    'plates': reverse('plate-list', request=request, format=format),
  })

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def add_fave_food(request):
  # request:
  #   food_id:    int, primary key of Food to be favorited

  try:
    user_detail = UserDetail.objects.get(user=request.user)
    food_id = request.data['food_id']
    food = Food.objects.get(id=food_id)

    if user_detail.fave_foods.filter(id=food_id).exists():
      return Response({"message":"This food already favorited."}, status=status.HTTP_200_OK)

    user_detail.fave_foods.add(food)
    return Response({"message":"Succesfully favorited food."}, status=status.HTTP_200_OK)
    
  except:
    return Response({"message":"Unable to add favorite food."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def remove_fave_food(request):
  # request:
  #   food_id:    int, primary key of Food to be favorited

  try:
    user_detail = UserDetail.objects.get(user=request.user)
    food_id = request.data['food_id']
    food = Food.objects.get(id=food_id)

    if not user_detail.fave_foods.filter(id=food_id).exists():
      return Response({"message":"This food not favorited."}, status=status.HTTP_200_OK)

    user_detail.fave_foods.remove(food)
    return Response({"message":"Succesfully favorited food."}, status=status.HTTP_200_OK)

  except:
    return Response({"message":"Unable to add favorite food."}, status=status.HTTP_400_BAD_REQUEST)

