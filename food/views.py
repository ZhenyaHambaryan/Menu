from user.models import UserDetail
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from food.serializers import FoodSerializer, FoodTypeSerializer, FoodCategorySerializer, PlateSectionSerializer,TransactionSerializer,TakeSerializer, \
                              PlateLayoutSerializer, PlateSerializer,IngredientsSerializer,SubscribeSerializer,RequestToCancelSerializer,\
                              SectionLayoutSerializer,BoxSerializer,PlateDrinkSerializer,PlateDessertSerializer,PlateFoodSerializer,PlateDaysSerializer
from food.models import Food, FoodType, FoodCategory, PlateSection, PlateLayout, Plate,Ingredients,Subscribe,\
                        SectionLayout,Box,PlateDrink,PlateDessert,PlateFood,PlateDays,Transaction,RequestToCancel,Take
# import django_filters
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum,F


class TakeViewSet(viewsets.ModelViewSet):
  queryset = Take.objects.all()
  serializer_class = TakeSerializer
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['date',]

class RequestToCancelViewSet(viewsets.ModelViewSet):
  queryset = RequestToCancel.objects.all()
  serializer_class = RequestToCancelSerializer


class TransactionViewSet(viewsets.ModelViewSet):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer

class PlateDaysViewSet(viewsets.ModelViewSet):
  queryset = PlateDays.objects.all()
  serializer_class = PlateDaysSerializer

class PlateFoodViewSet(viewsets.ModelViewSet):
  queryset = PlateFood.objects.all()
  serializer_class = PlateFoodSerializer


class PlateDrinkViewSet(viewsets.ModelViewSet):
  queryset = PlateDrink.objects.all()
  serializer_class = PlateDrinkSerializer

class PlateDessertViewSet(viewsets.ModelViewSet):
  queryset = PlateDessert.objects.all()
  serializer_class = PlateDessertSerializer

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

class SectionLayoutViewSet(viewsets.ModelViewSet):
  queryset = SectionLayout.objects.all()
  serializer_class = SectionLayoutSerializer




class PlateViewSet(viewsets.ModelViewSet):
  queryset = Plate.objects.all()
  serializer_class = PlateSerializer
  filter_backends = [filters.DjangoFilterBackend, SearchFilter]
  filter_fields = ['layout','days_plate__day',]

  def create(self, request, *args, **kwargs):
    plate = Plate(description=request.data['description'],created_at=request.data['created_at'],user_id=request.data['user_id'],
                  layout_id=request.data['layout_id'])
    plate.save()
    for drink in request.data['drink']:
      PlateDrink(plate_id=plate.id,count=drink['count'],drink_id=drink['id']).save()
    for dessert in request.data['dessert']:
      PlateDessert(plate_id=plate.id, count=dessert['count'], dessert_id=dessert['id']).save()
    for food in request.data['food']:
      PlateFood(plate_id=plate.id, count=food['count'], food_id=food['id'], section_layout_id=food['section_layout']).save()
    food1 = plate.drink_plate.aggregate(sum=Sum(F('drink__price') * F('count')))['sum']
    food2 = plate.dessert_plate.aggregate(sum=Sum(F('dessert__price') * F('count')))['sum']
    food3 = plate.food_plate.aggregate(sum=Sum(F('food__price') * F('count')))['sum']
    price = 0
    if food1 is not None:
      price = price+food1
    if food2 is not None:
      price = price +food2
    if food3 is not None:
      price = price+food3
    plate.price=price
    # sum hashvel
    plate.save()
    return Response(PlateSerializer(plate).data)

  def update(self,request,pk):
    plate_id=pk
    plate = Plate.objects.get(id=plate_id)
    food1 = plate.drink_plate.aggregate(sum=Sum(F('drink__price') * F('count')))['sum']
    food2 = plate.dessert_plate.aggregate(sum=Sum(F('dessert__price') * F('count')))['sum']
    food3 = plate.food_plate.aggregate(sum=Sum(F('food__price') * F('count')))['sum']
    price = 0
    if food1 is not None:
      price = price + food1
    if food2 is not None:
      price = price + food2
    if food3 is not None:
      price = price + food3
    plate.price = price
    plate.save()
    return Response(PlateSerializer(plate).data)

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

  def create(self, request, *args, **kwargs):
    subscribe = Subscribe(day_count=request.data['day_count'],address=request.data['address'],address_longitude=request.data['address_longitude'],
                          address_latitude=request.data['address_latitude'],comment=request.data['comment'])
    subscribe.save()
    for i in request.data['plate_id']:
      sub=subscribe.plate.add(i)
    subscribe.price=subscribe.plate.aggregate(sum=Sum('price'))['sum']
    subscribe.save()
    return Response(SubscribeSerializer(subscribe).data)


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

