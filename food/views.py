from user.models import UserDetail
from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from food.serializers import FoodSerializer, FoodTypeSerializer, FoodCategorySerializer, PlateSectionSerializer,TransactionSerializer,TakeSerializer, \
                              PlateLayoutSerializer, PlateSerializer,IngredientsSerializer,SubscribeSerializer,RequestToCancelSerializer,TimeIntervalSerializer,\
                              SectionLayoutSerializer,BoxSerializer,PlateDrinkSerializer,PlateDessertSerializer,PlateFoodSerializer,PlateDaysSerializer,SectionLayoutFullSerializer
from food.models import Food, FoodType, FoodCategory, PlateSection, PlateLayout, Plate,Ingredients,Subscribe,\
                        SectionLayout,Box,PlateDrink,PlateDessert,PlateFood,PlateDays,Transaction,RequestToCancel,Take,TimeInterval
# import django_filters
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum,F

class TimeIntervalViewSet(viewsets.ModelViewSet):
  queryset = TimeInterval.objects.all()
  serializer_class = TimeIntervalSerializer


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
    for i in request.data['plate']:
      sub=subscribe.plate.add(i)
    subscribe.price=subscribe.plate.aggregate(sum=Sum('price'))['sum']
    subscribe.save()
    return Response(SubscribeSerializer(subscribe).data)

  def get_queryset(self):
    from_date = self.request.query_params.get('from_date')
    to_date = self.request.query_params.get('to_date')
    queryset = Subscribe.objects.all()
    if from_date and to_date is not None:
      queryset = queryset.filter(plate__days_plate__day__gte=from_date,
                                 plate__days_plate__day__lte=to_date)
    return queryset


@api_view(['GET'])
def filtered_all(request):
  day = request.GET.get("day")
  plates=Plate.objects.filter(days_plate__day=day)
  result=[]
  choosed_foods=[]
  choosed_drinks=[]
  choosed_desserts=[]
  # ~~~~~~~~~~~~~~~~~~food~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  for plate in plates:
    takes_by_plate = Take.objects.filter(plate=plate.id)
    sections = []
    drinks=[]
    desserts=[]
    for food in plate.food_plate.all():
      section_layout_id=food.section_layout.id
      index=-1
      takes_by_section = takes_by_plate.filter(section_layout_id=section_layout_id)
      for i, section in enumerate(sections):
        if section_layout_id == section_layout_id:
          index=i
          break
      # plate_id = plate.id
      food_id = food.food.id
      tmp_food = PlateFoodSerializer(food).data
      takes = takes_by_section.filter(food_id=food_id)
      tmp_food['quantity'] = tmp_food['count']-takes.count()
      if index == -1:
        sections.append({"section_layout_id":section_layout_id, "foods":[tmp_food]})
      else:
        sections[index]['foods'].append(tmp_food)

    for section in sections:
      max_count=0
      for food in section['foods']:
        if max_count<food['quantity']:
          max_count=food['quantity']
      filtered_foods = []
      for food in section['foods']:
        if food['quantity'] == max_count:
          filtered_foods.append(food)
      if len(filtered_foods) == 1:
        choosed_foods.append(filtered_foods[0]['food']['id'])
      section['filtered_foods']=filtered_foods
# ~~~~~~~~~~~~~~~~~~~~~~~~drink~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for drink in plate.drink_plate.all():
      drink_id=drink.drink.id
      tmp_food = PlateDrinkSerializer(drink).data
      takes = takes_by_plate.filter(food_id=drink_id)
      tmp_food['quantity'] = tmp_food['count']-takes.count()
      drinks.append(tmp_food)

      max_count = 0
      for drink in drinks:
        if max_count < drink['quantity']:
          max_count = drink['quantity']
      filtered_drinks = []
      for drink in drinks:
        if drink['quantity'] == max_count:
          filtered_drinks.append(drink)
      if len(filtered_drinks) == 1:
        choosed_drinks.append(filtered_drinks[0]['drink'])
# ~~~~~~~~~~~~~~~~~~~~~~~~dessert~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for dessert in plate.dessert_plate.all():
      dessert_id = dessert.dessert.id
      tmp_food = PlateDessertSerializer(dessert).data
      takes = takes_by_plate.filter(food_id=dessert_id)
      tmp_food['quantity'] = tmp_food['count'] - takes.count()
      desserts.append(tmp_food)

      max_count = 0
      for dessert in desserts:
        if max_count < dessert['quantity']:
          max_count = dessert['quantity']
      filtered_desserts = []
      for dessert in desserts:
        if dessert['quantity'] == max_count:
          filtered_desserts.append(dessert)
      if len(filtered_desserts) == 1:
        choosed_desserts.append(filtered_desserts[0]['dessert'])

    result.append({"plate":{"id":plate.id},"filtered_foods":filtered_foods,"filtered_drinks":filtered_drinks,"filtered_desserts":filtered_desserts})

    for plate in result:
      # for section in plate['sections']:
        if len(section['filtered_foods']) >1:
          filtered_foods = []
          for food in section['filtered_foods']:
            if food['food']['id'] in choosed_foods:
              filtered_foods.append(food)
              break
          if len(filtered_foods)==0:
            filtered_foods.append(section['filtered_foods'][0])
            choosed_foods.append(filtered_foods[0]['food']['id'])
        section['filtered_foods'] = filtered_foods

    for drinks in result:
      if len(drinks["filtered_drinks"]) > 1:
        filtered_drinks = []
        for drink in drinks['filtered_drinks']:
          if drink['drink']['id'] in choosed_drinks:
            filtered_drinks.append(drink)
            break
        if len(filtered_drinks) == 0:
          filtered_drinks.append(drinks['filtered_drinks'][0])
          choosed_drinks.append(filtered_drinks[0]['drink']['id'])

    for desserts in result:
      if len(desserts["filtered_desserts"]) > 1:
        filtered_desserts = []
        for dessert in drinks['filtered_desserts']:
          if dessert['dessert']['id'] in choosed_desserts:
            filtered_desserts.append(drink)
            break
        if len(filtered_desserts) == 0:
          filtered_desserts.append(drinks['filtered_desserts'][0])
          choosed_desserts.append(filtered_desserts[0]['dessert']['id'])

  return Response(result)
# ~~~~~~~~~~~~~~~~~~~~~~~~dessert~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~








@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def filtered_foods(request):
  day=request.GET.get("day")
  # section_layout = SectionLayout.objects.filter(section_layout_plate_food__plate__days_plate__day=day)
  # return  Response(SectionLayoutFullSerializer(section_layout,many=True).data)
  plates=Plate.objects.filter(days_plate__day=day)
  result=[]
  choosed_foods=[]
  for plate in plates:
    takes_by_plate = Take.objects.filter(plate=plate.id)
    sections = []
    for food in plate.food_plate.all():
      section_layout_id=food.section_layout.id
      index=-1
      takes_by_section = takes_by_plate.filter(section_layout_id=section_layout_id)
      for i, section in enumerate(sections):
        if section_layout_id == section_layout_id:
          index=i
          break
      # plate_id = plate.id
      food_id = food.food.id
      tmp_food = PlateFoodSerializer(food).data
      takes = takes_by_section.filter(food_id=food_id)
      tmp_food['quantity'] = tmp_food['count']-takes.count()
      if index == -1:
        sections.append({"section_layout_id":section_layout_id, "foods":[tmp_food]})
      else:
        sections[index]['foods'].append(tmp_food)

    for section in sections:
      max_count=0
      for food in section['foods']:
        if max_count<food['quantity']:
          max_count=food['quantity']
      filtered_foods = []
      for food in section['foods']:
        if food['quantity'] == max_count:
          filtered_foods.append(food)
      if len(filtered_foods) == 1:
        choosed_foods.append(filtered_foods[0]['food']['id'])
      section['filtered_foods']=filtered_foods
    result.append({"plate":{"id":plate.id},"sections":sections})

    for plate in result:
      for section in plate['sections']:
        if len(section['filtered_foods']) >1:
          filtered_foods = []
          for food in section['filtered_foods']:
            if food['food']['id'] in choosed_foods:
              filtered_foods.append(food)
              break
          if len(filtered_foods)==0:
            filtered_foods.append(section['filtered_foods'][0])
            choosed_foods.append(filtered_foods[0]['food']['id'])
        section['filtered_foods'] = filtered_foods
  return Response(result)
  # return Response(TakeSerializer(takes).data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def filtered_drinks(request):
  day = request.GET.get("day")
  plates = Plate.objects.filter(days_plate__day=day)
  result = []
  choosed_drinks = []
  for plate in plates:
    takes_by_plate = Take.objects.filter(plate=plate.id)
    drinks=[]
    for drink in plate.drink_plate.all():
      drink_id=drink.drink.id
      tmp_food = PlateDrinkSerializer(drink).data
      takes = takes_by_plate.filter(food_id=drink_id)
      tmp_food['quantity'] = tmp_food['count']-takes.count()
      drinks.append(tmp_food)

      max_count = 0
      for drink in drinks:
        if max_count < drink['quantity']:
          max_count = drink['quantity']
      filtered_drinks = []
      for drink in drinks:
        if drink['quantity'] == max_count:
          filtered_drinks.append(drink)
      if len(filtered_drinks) == 1:
        choosed_drinks.append(filtered_drinks[0]['drink'])


    result.append({"plate":{"id":plate.id},"drinks":drinks,"filtered_drinks":filtered_drinks})
    for drinks in result:
        if len(drinks["filtered_drinks"]) > 1:
          filtered_drinks = []
          for drink in drinks['filtered_drinks']:
            if drink['drink']['id'] in choosed_drinks:
              filtered_drinks.append(drink)
              break
          if len(filtered_drinks) == 0:
            filtered_drinks.append(drinks['filtered_drinks'][0])
            choosed_drinks.append(filtered_drinks[0]['drink']['id'])
  return Response(result)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def filtered_desserts(request):
  day = request.GET.get("day")
  plates = Plate.objects.filter(days_plate__day=day)
  result = []
  choosed_desserts = []
  for plate in plates:
    takes_by_plate = Take.objects.filter(plate=plate.id)
    desserts=[]
    for dessert in plate.dessert_plate.all():
      dessert_id=dessert.dessert.id
      tmp_food = PlateDessertSerializer(dessert).data
      takes = takes_by_plate.filter(food_id=dessert_id)
      tmp_food['quantity'] = tmp_food['count']-takes.count()
      desserts.append(tmp_food)

      max_count = 0
      for dessert in desserts:
        if max_count < dessert['quantity']:
          max_count = dessert['quantity']
      filtered_desserts = []
      for dessert in desserts:
        if dessert['quantity'] == max_count:
          filtered_desserts.append(dessert)
      if len(filtered_desserts) == 1:
        choosed_desserts.append(filtered_desserts[0]['dessert'])


    result.append({"plate":{"id":plate.id},"desserts":desserts,"filtered_desserts":filtered_desserts})
    for desserts in result:
      if len(desserts["filtered_desserts"]) > 1:
        filtered_desserts = []
        for dessert in drinks['filtered_desserts']:
          if dessert['dessert']['id'] in choosed_desserts:
            filtered_desserts.append(drink)
            break
        if len(filtered_desserts) == 0:
          filtered_desserts.append(drinks['filtered_desserts'][0])
          choosed_desserts.append(filtered_desserts[0]['dessert']['id'])
  return Response(result)


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

# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def add_fave_food(request):
#   # request:
#   #   food_id:    int, primary key of Food to be favorited
#
#   try:
#     user_detail = UserDetail.objects.get(user=request.user)
#     food_id = request.data['food_id']
#     food = Food.objects.get(id=food_id)
#
#     if user_detail.fave_foods.filter(id=food_id).exists():
#       return Response({"message":"This food already favorited."}, status=status.HTTP_200_OK)
#
#     user_detail.fave_foods.add(food)
#     return Response({"message":"Succesfully favorited food."}, status=status.HTTP_200_OK)
#
#   except:
#     return Response({"message":"Unable to add favorite food."}, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def remove_fave_food(request):
#   # request:
#   #   food_id:    int, primary key of Food to be favorited
#
#   try:
#     user_detail = UserDetail.objects.get(user=request.user)
#     food_id = request.data['food_id']
#     food = Food.objects.get(id=food_id)
#
#     if not user_detail.fave_foods.filter(id=food_id).exists():
#       return Response({"message":"This food not favorited."}, status=status.HTTP_200_OK)
#
#     user_detail.fave_foods.remove(food)
#     return Response({"message":"Succesfully favorited food."}, status=status.HTTP_200_OK)
#
#   except:
#     return Response({"message":"Unable to add favorite food."}, status=status.HTTP_400_BAD_REQUEST)
#
