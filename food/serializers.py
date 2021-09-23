from django.db.models import fields
from food.models import Food, FoodType, FoodCategory, PlateSection, PlateLayout, Plate,Ingredients,Subscribe,SectionFood,Box,PlateDrink
from user.serializers import UserDetailSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

class PlateDrinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlateDrink
    fields = '__all__'


class FoodCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = FoodCategory
    fields = '__all__'

class FoodTypeSerializer(serializers.ModelSerializer):
  # food_category = FoodCategorySerializer()
  def to_representation(self, instance):
    representation = super(FoodTypeSerializer,self).to_representation(instance)
    representation["food_category"] = FoodCategorySerializer(instance.food_category).data
    return representation
  class Meta:
    model = FoodType
    fields = '__all__'

class IngredientsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredients
    fields = '__all__'



class FoodSerializer(serializers.ModelSerializer):
  # food_type = FoodTypeSerializer()
  def to_representation(self, instance):
    representation = super(FoodSerializer,self).to_representation(instance)
    representation["food_type"] = FoodTypeSerializer(instance.food_type).data
    return representation
  class Meta:
    model = Food
    fields = '__all__'


class PlateSectionSerializer(serializers.ModelSerializer):
  # category = FoodCategorySerializer(many=True)
  def to_representation(self, instance):
    representation = super(PlateSectionSerializer,self).to_representation(instance)
    representation["category"] = FoodCategorySerializer(instance.category,many=True).data
    return representation

  class Meta:
    model = PlateSection
    fields = '__all__'

class PlateLayoutSerializer(serializers.ModelSerializer):
  # sections = PlateSectionSerializer(many=True)
  # category = FoodCategorySerializer(many=False)

  def to_representation(self, instance):
    representation = super(PlateLayoutSerializer,self).to_representation(instance)
    representation["sections"] = PlateSectionSerializer(instance.sections,many=True).data

    return representation

  class Meta:
    model = PlateLayout
    fields = '__all__'

class SectionFoodSerializer(serializers.ModelSerializer):
  # sections = PlateSectionSerializer()
  # food = FoodSerializer()
  def to_representation(self, instance):
    representation = super(SectionFoodSerializer,self).to_representation(instance)
    representation["sections"] = PlateSectionSerializer(instance.sections).data
    representation["food"] = FoodSerializer(instance.food).data

    return representation

  class Meta:
    model = SectionFood
    fields = '__all__'


class PlateSerializer(serializers.ModelSerializer):
  # layout = PlateLayoutSerializer()
  # drink = PlateDrinkSerializer()
  # drink = FoodSerializer(many=True)
  def to_representation(self, instance):
    representation = super(PlateSerializer,self).to_representation(instance)
    representation["layout"] = PlateLayoutSerializer(instance.layout).data
    representation["drink"] = PlateDrinkSerializer(instance.drink_plate,many=True).data
    # representation["dessert"] = FoodSerializer(instance.dessert,many=True).data
    return representation

  class Meta:
    model = Plate
    fields = '__all__'

class BoxSerializer(serializers.ModelSerializer):
  def to_representation(self, instance):
    representation = super(BoxSerializer,self).to_representation(instance)
    representation["layout"] = PlateLayoutSerializer(instance.layout).data
    # representation["drink"] = FoodSerializer(instance.drink,many=True).data
    representation["dessert"] = FoodSerializer(instance.dessert,many=True).data
    return representation

  class Meta:
    model = Box
    fields = '__all__'



class SubscribeSerializer(serializers.ModelSerializer):
  # plate = PlateSerializer()
  def to_representation(self, instance):
    representation = super(SubscribeSerializer,self).to_representation(instance)
    representation["plate"] = PlateSerializer(instance.plate).data
    # representation["price"] = instance.price

    return representation

  class Meta:
    model = Subscribe
    fields = '__all__'