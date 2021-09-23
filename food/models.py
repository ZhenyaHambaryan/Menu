# from user.views import delete_org
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.db.models import Sum




class FoodCategory(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(null=True, blank=True, max_length=1000)
  image =  models.ImageField(upload_to='uploads/',null=True, blank=True)



  def __str__(self):
    return self.name


class FoodType(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(null=True, blank=True, max_length=1000)
  image = models.ImageField(upload_to='uploads/', null=True, blank=True)
  food_category = models.ForeignKey(FoodCategory , on_delete=models.CASCADE, null=True,
                     blank=True, related_name="food_category")

  def __str__(self):
    return self.name


class Food(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(null=True,blank=True,max_length=1000)
  image =  models.ImageField(upload_to='uploads/',null=True, blank=True)
  price = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
  is_vegetarian = models.BooleanField(default=False)
  is_vegan = models.BooleanField(default=False)
  is_healthy = models.BooleanField(default=False)
  # ingredients = models.ManyToManyField(Ingredients,null=True, blank=True, related_name="food_ingridients")
  food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, null=True,
                     blank=True, related_name="foods")

  def __str__(self):
    return self.name



class Ingredients(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(null=True, blank=True, max_length=1000)
  image = models.ImageField(upload_to='uploads/', null=True, blank=True)
  calories = models.CharField(max_length=255, null=True, blank=True)
  weight =models.CharField(max_length=255, null=True, blank=True)
  food = models.ManyToManyField(Food, blank=True, related_name="food_ingridients")




class PlateSection(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(null=True, blank=True, max_length=1000)
  image = models.ImageField(upload_to='uploads/', null=True, blank=True)
  category = models.ManyToManyField(FoodCategory)

  def __str__(self):
    return self.name

class PlateLayout(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(null=True, blank=True, max_length=1000)
  image = models.ImageField(upload_to='uploads/', null=True, blank=True)
  sections = models.ManyToManyField(PlateSection, blank=True)
  # has_drink = models.BooleanField(default=False)
  # has_dessert = models.BooleanField(default=False)
  count = models.IntegerField(default=0)


  @property 
  def sections_count(self):
    return self.sections.all().count()

  def __str__(self):
    return self.name

class SectionFood(models.Model):
  section = models.ForeignKey(PlateSection, on_delete=models.CASCADE, null=True,
                     blank=True, related_name="section")
  food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True,
                     blank=True, related_name="foods")

class Plate(models.Model):
  # name = models.CharField(max_length=255)
  description = models.CharField(null=True, blank=True, max_length=1000)
  image = models.ImageField(upload_to='uploads/', null=True, blank=True)
  user = models.ForeignKey(User,null=True,blank=True,on_delete=CASCADE)
  layout = models.ForeignKey(PlateLayout, on_delete=models.CASCADE, null=True,
                     blank=True, related_name="layout_plate")#DEBUG: redundant?
  section_food = models.ManyToManyField(SectionFood, blank=True,related_name='plate_section_food')
  # drink =  models.ManyToManyField(Food, blank=True, related_name="food_drink")
  dessert =  models.ManyToManyField(Food, blank=True, related_name="food_dessert")

class PlateDrink(models.Model):
  plate = models.ForeignKey(Plate, on_delete=models.CASCADE, null=True,
                     blank=True, related_name="drink_plate")
  drink =  models.ManyToManyField(Food, blank=True, related_name="plate_drink")
  count = models.IntegerField(null=False, blank=False,default=0)

  # foods = models.ManyToManyField(Food, blank=True)
  # has_drink = models.BooleanField(default=True)
  # has_dessert = models.BooleanField(default=True)
  #NOTE: the number of sections in layout must equal number of foods
    # @property
  # def price(self):
    # price = 0
    # for f in self.foods.all():
    #   price += f.price
    # return price
    #
  def __str__(self):
    return "Plate #" + str(self.id) + ", User:" + str(self.user)

class Subscribe(models.Model):
  plate = models.ForeignKey(Plate, on_delete=models.CASCADE, null=True,
                     blank=True, related_name="subscribe_plate")
  day_count = models.IntegerField(default=0)
  day = models.CharField(max_length=255, null=True, blank=True)
  address = models.CharField(null=True,blank=True,max_length=1000)
  address_longitude = models.CharField(null=True,blank=True,max_length=255)
  address_latitude = models.CharField(null=True,blank=True,max_length=255)
  comment = models.CharField(null=True,blank=True,max_length=1000)
  # price = models.FloatField(null=True, blank=True, default=0.0)
  # @property
  # def price(self):
  #   food1 = self.plate.drink.all()
  #   food2 = self.plate.dessert.all()
  #   food3 = self.plate.section_food.all()
  #   n = self.day_count
  #   pr=0
  #   while n == 0:
  #     for i in food1:
  #       pr=pr+i.aggregate(sum=Sum('price'))['sum']
  #       n=n-1
  #   return pr
  #   while n==0:
  #     for i in food2:
  #       pr2=pr+i.aggregate(sum=Sum('price'))['sum']
  #       n=n-1
  #   while n==0:
  #     for i in food3:
  #       pr3=pr+i.aggregate(sum=Sum('food__price'))['sum']
  #       n=n-1
  #   return pr1+pr2+pr3
    # for i in food1:
    #   pr1 = i.aggregate(sum=Sum('price'))['sum'] * (self.day_count / self.plate.drink.count())
    # for i in food2:
    #   pr2 = i.aggregate(sum=Sum('price'))['sum'] * (self.day_count / self.plate.dessert.count())
    # for i in food3:
    #   pr3 = i.aggregate(sum=Sum('food__price'))['sum'] * (self.day_count / self.plate.section_food.food.count())
    # return pr1+pr2+pr3
    # food1 = self.plate.drink.aggregate(sum=Sum('price'))['sum']
    # food2 = self.plate.dessert.aggregate(sum=Sum('price'))['sum']
    # food3 = self.plate.section_food.all().aggregate(sum=Sum('food__price'))['sum']
    # pr = 0
    # # print(self.plate.drink.count())
    # if food1 is not None:
    #   pr = pr+food1
    # if food2 is not None:
    #   pr = pr +food2
    # if food3 is not None:
    #   pr = pr+food3
    # return pr*self.day_count

    # if food1 is None and food2 and food3 is not None :
    #   return (food2+food3)*self.day_count
    # if food2 is  None  and food1 and food3 is not  None:
    #   return (food1+food3)*self.day_count
    # if food3 is  None  and food1 and food2 is not None:
    #   return (food1+food2)*self.day_count
    # if food2 and food3 is None and food1 is not None:
    #   return food1*self.day_count
    # if food1 and food3 is None and food2 is not None:
    #   return food2*self.day_count
    # if food1 and food2 is  None and food3 is not None:
    #   return food3*self.day_count
    # if food1 and food2 and food3 is None:
    #   return 0


    # return foods
 # class PlateDrink(models.Model):
#   plate =  models.ForeignKey(Plate, on_delete=models.CASCADE, null=True,
#                      blank=True, related_name="plate_drink")
#   drink =  models.ForeignKey(Food,on_delete=models.CASCADE, blank=True, related_name="food_drink")
#   count = models.IntegerField(default=0)
#
# class PlateDessert(models.Model):
#   plate =  models.ForeignKey(Plate, on_delete=models.CASCADE, null=True,
#                      blank=True, related_name="plate_dessert")
#   dessert =  models.ForeignKey(Food,on_delete=models.CASCADE, blank=True, related_name="food_dessert")
#   count = models.IntegerField(default=0)
#
# class PlateSectionFood(models.Model):
#   plate =  models.ForeignKey(Plate, on_delete=models.CASCADE, null=True,
#                      blank=True, related_name="section_food_plate")
#   section_food = models.ForeignKey(SectionFood, on_delete=models.CASCADE, blank=True,related_name='plate_section_food')
#   count = models.IntegerField(default=0)

class Box(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(null=True, blank=True, max_length=1000)
  image = models.ImageField(upload_to='uploads/', null=True, blank=True)
  user = models.ForeignKey(User,null=True,blank=True,on_delete=CASCADE)
  layout = models.ForeignKey(PlateLayout, on_delete=models.CASCADE, null=True,
                     blank=True, related_name="layout_box")#DEBUG: redundant?
  section_food = models.ManyToManyField(SectionFood, blank=True)
  # foods = models.ManyToManyField(Food, blank=True)
  drink =  models.ManyToManyField(Food, blank=True, related_name="box_drink")
  dessert =  models.ManyToManyField(Food, blank=True, related_name="box_dessert")
  has_drink = models.BooleanField(default=True)
  has_dessert = models.BooleanField(default=True)