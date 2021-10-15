from django.db.models import fields
from food.models import Food, FoodType, FoodCategory, PlateSection, PlateLayout, Plate,Ingredients,Subscribe,\
                        SectionLayout,Box,PlateDrink,PlateDessert,PlateFood,PlateDays,Transaction
from user.serializers import UserDetailSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
import sys,json

class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = '__all__'


class FoodCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = FoodCategory
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(FoodCategorySerializer,self).to_representation(instance)
    try:
      representation['name'] = json.loads(instance.name)
    except:
      representation['name'] = None
    try:
      representation['description'] = json.loads(instance.description)
    except:
      representation['description'] = None
    return representation


class FoodTypeSerializer(serializers.ModelSerializer):
  # food_category = FoodCategorySerializer()
  class Meta:
    model = FoodType
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(FoodTypeSerializer,self).to_representation(instance)
    representation["food_category"] = FoodCategorySerializer(instance.food_category).data
    try:
      representation['name'] = json.loads(instance.name)
    except:
      representation['name'] = None
    try:
      representation['description'] = json.loads(instance.description)
    except:
      representation['description'] = None
    return representation


class IngredientsSerializer(serializers.ModelSerializer):
  # food = FoodSerializer(many=True)

  class Meta:
    model = Ingredients
    fields = '__all__'
  #
  def to_representation(self, instance):
    representation = super(IngredientsSerializer,self).to_representation(instance)
    representation["food"] = FoodSerializer(instance.food,many=True).data

    try:
      representation['name'] = json.loads(instance.name)
    except:
      representation['name'] = None
    # return representation
    try:
      representation['description'] = json.loads(instance.description)
    except:
      representation['description'] = None
    return representation



class FoodSerializer(serializers.ModelSerializer):
  # food_type = FoodTypeSerializer()
  class Meta:
    model = Food
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(FoodSerializer,self).to_representation(instance)
    # data['name'] = json.loads(instance.name)
    # data['description'] = json.loads(instance.description)
    representation["food_type"] = FoodTypeSerializer(instance.food_type).data
    try:
      representation['name'] = json.loads(instance.name)
    except:
      representation['name'] = None
    try:
      representation['description'] = json.loads(instance.description)
    except:
      representation['description'] = None
    return representation



class PlateSectionSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlateSection
    fields = '__all__'
  # category = FoodCategorySerializer(many=True)
  def to_representation(self, instance):
    representation = super(PlateSectionSerializer,self).to_representation(instance)
    # data['name'] = json.loads(instance.name)
    # data['description'] = json.loads(instance.description)
    representation["category"] = FoodCategorySerializer(instance.category,many=True).data
    try:
      representation['name'] = json.loads(instance.name)
    except:
      representation['name'] = None
    try:
      representation['description'] = json.loads(instance.description)
    except:
      representation['description'] = None
    return representation



class PlateLayoutSerializer(serializers.ModelSerializer):
  # sections = PlateSectionSerializer(many=True)
  # category = FoodCategorySerializer(many=False)
  class Meta:
    model = PlateLayout
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(PlateLayoutSerializer,self).to_representation(instance)
    try:
      representation['name'] = json.loads(instance.name)
    except:
      representation['name'] = None
    try:
      representation['description'] = json.loads(instance.description)
    except:
      representation['description'] = None
    return representation


class SectionLayoutSerializer(serializers.ModelSerializer):
  # sections = PlateSectionSerializer()
  # layout = PlateLayoutSerializer()
  class Meta:
    model = SectionLayout
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(SectionLayoutSerializer,self).to_representation(instance)
    representation["section"] = PlateSectionSerializer(instance.section).data
    representation["layout"] = PlateLayoutSerializer(instance.layout).data

    return representation


class PlateDrinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlateDrink
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(PlateDrinkSerializer,self).to_representation(instance)
    # representation["plate"] = PlateSerializer(instance.drink_plate).data
    representation["drink"] = FoodSerializer(instance.drink).data
    # representation["dessert"] = FoodSerializer(instance.dessert).data


    return representation

class PlateDessertSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlateDessert
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(PlateDessertSerializer,self).to_representation(instance)
    representation["dessert"] = FoodSerializer(instance.dessert).data

    return representation

class PlateFoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlateFood
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(PlateFoodSerializer,self).to_representation(instance)
    representation["food"] = FoodSerializer(instance.food).data
    representation["section_layout"] = SectionLayoutSerializer(instance.section_layout).data
    return representation

class PlateDaysSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlateDays
    fields = '__all__'


class PlateSerializer(serializers.ModelSerializer):
  # layout = PlateLayoutSerializer()
  # drink = PlateDrinkSerializer()
  # drink = FoodSerializer(many=True)
  class Meta:
    model = Plate
    fields = '__all__'

  def to_representation(self, instance):
    representation = super(PlateSerializer,self).to_representation(instance)
    representation["layout"] = PlateLayoutSerializer(instance.layout).data
    representation["drink"] = PlateDrinkSerializer(instance.drink_plate,many=True).data
    representation["dessert"] = PlateDessertSerializer(instance.dessert_plate,many=True).data
    representation["food"] = PlateFoodSerializer(instance.food_plate,many=True).data
    # representation["transaction"] = TransactionSerializer(instance.transacion_subscribe).data



    # try:
    #   representation['description'] = json.loads(instance.description)
    # except:
    #   representation['description'] = None
    return representation


class SubscribeSerializer(serializers.ModelSerializer):
  # plate = PlateSerializer()
  class Meta:
    model = Subscribe
    fields = '__all__'

  def to_representation(self, instance):
    representation = super(SubscribeSerializer,self).to_representation(instance)
    representation["plate"] = PlateSerializer(instance.plate,many=True).data

    return representation






class BoxSerializer(serializers.ModelSerializer):
  class Meta:
    model = Box
    fields = '__all__'

  def to_representation(self, instance):
    representation = super(BoxSerializer,self).to_representation(instance)
    representation["layout"] = PlateLayoutSerializer(instance.layout).data
    # representation["drink"] = FoodSerializer(instance.drink,many=True).data
    representation["dessert"] = FoodSerializer(instance.dessert,many=True).data
    try:
      representation['name'] = json.loads(instance.name)
    except:
      representation['name'] = None
    try:
      representation['description'] = json.loads(instance.description)
    except:
      representation['description'] = None
    return representation



