from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from django.urls import reverse_lazy
from django.views import generic
from user.serializers import  UserDetailSerializer,UserSerializer,ContactUsSerializer,TeamSerializer
from user.models import  UserDetail, ConfirmCode,User,ContactUs,Team
from datetime import datetime, timedelta
import random
import pytz
from rest_framework_simplejwt.tokens import RefreshToken

# class CityViewSet(viewsets.ModelViewSet):
#   queryset = City.objects.all()
#   serializer_class = CitySerializer


class ContactUsViewSet(viewsets.ModelViewSet):
  queryset = ContactUs.objects.all()
  serializer_class = ContactUsSerializer

class UserDetailViewSet(viewsets.ModelViewSet):
  queryset = UserDetail.objects.all()
  serializer_class = UserDetailSerializer

class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'users': reverse('user-list', request=request, format=format),
    'organizations': reverse('organization-list', request=request, format=format)
  })

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GLOBALS

# Period of time that a confirmation code remains valid:
conf_lifespan = timedelta(minutes=5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    return Response(UserDetailSerializer(UserDetail.objects.get(user_id=request.user.id)).data,
                                    status=status.HTTP_200_OK)


@api_view(['POST'])
def user_login(request):
  # request: 
  #   username: char[]
  #   password: char[]
  #   role_code: char[], either "MST" for master or "CL" for client
  # this method takes in username, password, and role code and returns a token and user model
  # if a user has two profiles, as master and client, insure you are using the proper role code

  username=request.data['username'].strip()
  password=request.data['password'].strip()
  role=request.data['role_code'].strip()

  if len(username)==0:
    return Response({"message":"No username provided."},status=status.HTTP_400_BAD_REQUEST)
  if len(password)==0:
    return Response({"message":"No password provided."}, status=status.HTTP_400_BAD_REQUEST)
  if len(role)==0:
    return Response({"message":"No role code provided."}, status=status.HTTP_400_BAD_REQUEST)
  if not (role == "MST" or role == "CL"):
    return Response({"message":"Invalid role code provided."}, status=status.HTTP_400_BAD_REQUEST)

  credentials = {
    get_user_model().USERNAME_FIELD: username,
    'password': password
  } 
  user = authenticate(**credentials)

  if user is None or not user.is_active:
    return Response({"message":"Incorrect username or password"}, status=status.HTTP_400_BAD_REQUEST)

  try:
    print(1)
    if role == "MST":
      userDetails = UserDetail.objects.get(user=user, is_master = True)
    else: #role == "CL"
      userDetails = UserDetail.objects.get(user=user, is_client = True)
    if not userDetails.user.is_active:
      return Response({"message":"User is removed."},status=status.HTTP_400_BAD_REQUEST)
    else:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        "user":UserDetailSerializer(userDetails).data
      },status=status.HTTP_200_OK)
  except:
    return Response({"message":"Incorrect username or password"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_conf_code(request):
  # request: 
  #   phone_number:       char[]
  #   email:              char[]

  # phone_number=request.data['phone_number'].strip()
  email=request.data['email'].strip()
  errors = []

  # Leave this if only using confirmation codes for registration
  # Remove this if using conf codes for Forgot/Change passwords 
  # v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v
  if User.objects.filter(email=email).exists():
    errors.append({"message":"Email already registered."})
  # if UserDetail.objects.filter(phone_number=phone_number).exists():
  #   errors.append({"message":"Phone number already registered."})
  # # #

  if len(errors) == 0:
    old_codes = ConfirmCode.objects.filter(email=email)
    if old_codes.count() > 0:
      old_codes.delete()
    while True:
      code = str(random.randint(100000,999999))
      # code = 111111
      code.zfill(6)
      if not ConfirmCode.objects.filter(code=code).exists():
        break
    new_code = ConfirmCode(code=code, email=email)
    new_code.save()
    return Response({"message":"Confirmation code created.",
                     "code": new_code.code,}, status = status.HTTP_201_CREATED)
    # return Response({"message":"Confirmation code created."}, status = status.HTTP_201_CREATED)
  else:
    return Response(errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_user(request):
  # request:
  #   username:           char[]
  #   password:           char[]
  #   confirm_password:   char[]
  #   phone_number:       char[]
  #   email:              char[]
  #   confirm_code:       char[]
  #   role_code:          char[]

  first_name=request.data['first_name'].strip()
  last_name=request.data['last_name'].strip()
  # username=request.data['email'].strip()
  password=request.data['password'].strip()
  confirm_password=request.data['confirm_password'].strip()
  # phone_number=request.data['phone_number']
  email=request.data['email'].strip()
  confirm_code=request.data['confirm_code'].strip()
  role_code=request.data['role_code'].strip()
  errors = []

  # if len(username)<6:
  #   errors.append({"message":"Username must be at least 6 characters."})
  if len(password)<6:
    errors.append({"message":"Password must be at least 6 characters."})
  if password != confirm_password:
    errors.append({"message":"Passwords do not match."})
  if User.objects.filter(username=email).exists():
    errors.append({"message":"Username is taken."})
  if User.objects.filter(email=email).exists():
    errors.append({"message":"Email already registered."})
  # if UserDetail.objects.filter(phone_number=phone_number).exists():
  #   errors.append({"message":"Phone number already registered."})
  if not (role_code == "MST" or role_code == "CL"):
    errors.append({"message":"Invalid role code provided."})
  if len(errors)==0:
    try:
      db_conf_code = ConfirmCode.objects.get(code=confirm_code)

      if (db_conf_code.created_at + conf_lifespan < datetime.now().replace(tzinfo=pytz.UTC)):
        return Response({'message':"Confirmation code has expired."},status=status.HTTP_400_BAD_REQUEST)

      new_user = User(username=email,
                      first_name=first_name,
                      last_name=last_name,
                      email=email,
                      is_superuser=False,
                      is_staff=False,
                      is_active=True)
      new_user.set_password(password)
      new_user.save()
      # token = Token.objects.create(user=new_user)
      try:
        new_user_detail = UserDetail(user=new_user)
        if role_code=="MST":
          new_user_detail.is_client=False
          new_user_detail.is_master=True
        else: #role_code=="CLI"
          new_user_detail.is_client=True
          new_user_detail.is_master=False
        new_user_detail.save()
        db_conf_code.delete()
        # send welcome email ***
        refresh = RefreshToken.for_user(new_user)
        return Response({
          'refresh': str(refresh),
          'access': str(refresh.access_token),
          "user": UserDetailSerializer(new_user_detail).data
        }, status=status.HTTP_201_CREATED)
      except:
        new_user.delete()
        return Response({'message':"Huh."},status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response({'message':"Confirmation code is incorrect."},status=status.HTTP_400_BAD_REQUEST)
  else:
    return Response(errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):
  # request: 
  #   *username:           char[]
  #   *first_name:         char[]
  #   *last_name:          char[]
  #   *email:              char[]
  #   *phone_number:       char[]
  #   *birth_date          char[], 'YYYY-MM-DD' e.g. '2006-10-25'
  #   *about:              char[]
  #   *zip_code:           char[]
  #   *city:               char[]
  #   *city_longitude:     char[]
  #   *city_latitude:      char[]
  #   *address:            char[]
  #   *address_longitude:  char[]
  #   *address_latitude:   char[]
  #
  # * = optional field
  # NOTE: this method does not check to see if email, phone number, 
  # and address are valid
  user = User.objects.get(id=request.user.id)
  user_detail = UserDetail.objects.get(user_id=request.user.id)
  errors = []

  username = request.data.get('username',user.username).strip()
  birth_date=request.data.get('birth_date', user_detail.birth_date).strip()
  email=request.data.get('email', user.email).strip()
  phone_number=request.data.get('phone_number', user_detail.phone_number).strip()


  if len(username.strip())<6:
    errors.append({"message":"Username should contain at least 6 characters."})
  if User.objects.filter(username = email).exclude(id=request.user.id).count()>0:
    errors.append({"message":"Username already in use."})
  if User.objects.filter(email=email).exists():
    errors.append({"message":"Email already registered."})
  if UserDetail.objects.filter(phone_number=phone_number).exists():
    errors.append({"message":"Phone number already registered."})
  try:
    testdate = datetime.strptime(birth_date, '%Y-%m-%d')
  except:
    errors.append({"message":"Invalid date."})

  if len(errors) == 0:
    try:
      user.username=email
      user.first_name=request.data.get('first_name',user.first_name).strip()
      user.last_name=request.data.get('last_name',user.last_name).strip()
      user.email=email
      user.save()
      user_detail.phone_number=phone_number
      user_detail.birth_date=birth_date
      user_detail.about=request.data.get('about',user_detail.about)
      user_detail.zip_code=request.data.get('zip_code',user_detail.zip_code)
      user_detail.city=request.data.get('city',user_detail.city)
      user_detail.city_longitude=request.data.get('city_longitude',user_detail.city_longitude)
      user_detail.city_latitude=request.data.get('city_latitude',user_detail.city_latitude)
      user_detail.address=request.data.get('address',user_detail.address)
      user_detail.address_longitude=request.data.get('address_longitude',user_detail.address_longitude)
      user_detail.address_latitude=request.data.get('address_latitude',user_detail.address_latitude)
      user_detail.save()
      return Response({"message":"Successfully updated user profile."},
       status=status.HTTP_200_OK)
    except:
      return Response({"message":"Unable to update user profile."},
       status=status.HTTP_400_BAD_REQUEST)
  else:
    return Response(errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def set_user_role(request):
  # request:
  #   role_code:  char[], either 'MST' or 'CL'

  role_code = request.data['role_code'].strip()
  user_detail = UserDetail.objects.get(user_id=request.user.id)

  if role_code == 'MST':
    user_detail.is_master = True
    user_detail.is_client = False
    user_detail.save()
    return Response({"message":"User role changed to Master"}, status=status.HTTP_200_OK)
  elif role_code == 'CL':
    user_detail.is_master = False
    user_detail.is_client = True
    user_detail.save()
    return Response({"message":"User role changed to Client"}, status=status.HTTP_200_OK)
  else:
    return Response({"message":"Invalid role code."}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def remove_profile(request):
  try:
    user = request.user
    user_detail = UserDetail.objects.get(user=user)
    user.is_active = False
    user.save()
    return Response({
      "message":"User successfully removed.",
      "user": UserDetailSerializer(user_detail).data}, status=status.HTTP_200_OK)
  except:
    return Response({"message":"Unable to remove user profile."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH']) 
def unremove_profile(request):
  # request:
  #   re_add_id:  int, the id of the user to be readded
  
  try:
    re_add_id = request.data['re_add_id']
    user = User.objects.get(id=re_add_id)
    user_detail = UserDetail.objects.get(user=user)

    if user.is_active == True:
      return Response({"message":"User is already active."}, status=status.HTTP_200_OK)
    
    user.is_active=True
    user.save()
    return Response({
      "message":"User successfully readded.",
      "user": UserDetailSerializer(user_detail).data}, status=status.HTTP_200_OK)
  except:
    return Response({"message":"Unable to readd user."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_org(request):
  # request:
  #   name:               char[]
  #   phone_number:       char[]
  #   about:              char[]
  #   zip_code:           char[]
  #   city:               char[]
  #   city_longitude:     char[]
  #   city_latitude:      char[]
  #   address:            char[]
  #   address_longitude:  char[]
  #   address_latitude:   char[]
  name = request.data['name'].strip()
  phone_number = request.data['phone_number'].strip()
  about = request.data['about']
  zip_code = request.data['zip_code'].strip()
  city = request.data['city'].strip()
  city_longitude = request.data['city_longitude'].strip()
  city_latitude = request.data['city_latitude'].strip()
  address = request.data['address'].strip()
  address_longitude = request.data['address_longitude'].strip()
  address_latitude = request.data['address_latitude'].strip()

  if Organization.objects.filter(phone_number=phone_number).exists():
    return Response({"message":"Phone number already registered."}, status=status.HTTP_400_BAD_REQUEST)

  try:
    org_leader = request.user
    new_org = Organization(name=name,
                           org_leader=org_leader,
                           phone_number=phone_number,
                           about=about,
                           zip_code=zip_code,
                           city=city,
                           city_longitude=city_longitude,
                           city_latitude=city_latitude,
                           address=address,
                           address_longitude=address_longitude,
                           address_latitude=address_latitude
                          )
    new_org.save()  
    return Response({
      "message" : "Successfully created organization.",
      "organization" : OrganizationSerializer(new_org).data
      }, status=status.HTTP_201_CREATED)
  except:
    return Response({"message":"Unable to create organization."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def join_org(request):
  # request:
  #   org_id:   int, primary key of Organization to join

  try:
    user_detail = UserDetail.objects.get(user=request.user)
    org_id = request.data['org_id']
    org = Organization.objects.get(id=org_id)

    if user_detail.organizations.filter(id=org_id).exists():
      return Response({"message":"User is already part of organization."}, status=status.HTTP_200_OK)
    
    user_detail.organizations.add(org)
    return Response({
      "message":"User successfully joined organization.",
      "user": UserDetailSerializer(user_detail).data
      }, status=status.HTTP_200_OK)
  except:
    return Response({"message":"Unable to join organization."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def leave_org(request):
  # request
  #   org_id:   int, primary key of Organization to leave

  
  try:
    user_detail = UserDetail.objects.get(user=request.user)
    org_id = request.data['org_id']
    org = Organization.objects.get(id=org_id)

    if not user_detail.organizations.filter(id=org_id).exists():
      return Response({"message":"User is not part of organization."}, status=status.HTTP_200_OK)
    
    user_detail.organizations.remove(org)
    return Response({
      "message":"User successfully left organization.",
      "user": UserDetailSerializer(user_detail).data
    }, status=status.HTTP_200_OK)
  except:
    return Response({"message":"Unable to leave organization."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def change_org_leader(request):
  # request:
  #   org_id:   int, primary key of Organization to join
  #   user_id:  int, primary key of User to become organization leader
  # NOTE: this method should be called by the current leader of the organization 
  # to change leadership

  

  try:
    org_id = request.data['org_id']
    user_id = request.data['user_id']
    org = Organization.objects.get(id=org_id)

    if (org.org_leader == request.user):
      org.org_leader = User.objects.get(id=user_id)
      org.save()
      return Response({
      "message":"Successfully changed organization leader.",
      "organization": OrganizationSerializer(org).data
      }, status=status.HTTP_200_OK)
    else:
      return Response({"message":"This user does not have permission to change organization leader."},
        status=status.HTTP_401_UNAUTHORIZED)
  except:
    return Response({"message":"Unable to change organization leader."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_org_info(request):
  # request:
  #   org_id:   int, primary key of Organization to update
  #   *name:               char[]
  #   *phone_number:       char[]
  #   *about:              char[]
  #   *zip_code:           char[]
  #   *city:               char[]
  #   *city_longitude:     char[]
  #   *city_latitude:      char[]
  #   *address:            char[]
  #   *address_longitude:  char[]
  #   *address_latitude:   char[]
  #
  # * = optional field
  
  try:
    org_id = request.data['org_id'] 
    org = Organization.objects.get(id=org_id)
    
    if (org.org_leader == request.user):
      org.name=request.data.get('name',org.name).strip()
      org.phone_number=request.data.get('phone_number', org.phone_number).strip()
      org.about=request.data.get('about', org.about).strip()
      org.zip_code=request.data.get('zip_code', org.zip_code).strip()
      org.city=request.data.get('city', org.city).strip()
      org.city_longitude=request.data.get('city_longitude', org.city_longitude).strip()
      org.city_latitude=request.data.get('city_latitude', org.city_latitude).strip()
      org.address=request.data.get('address', org.address).strip()
      org.address_longitude=request.data.get('address_longitude', org.address_longitude).strip()
      org.address_latitude=request.data.get('address_latitude', org.address_latitude).strip()
      org.save()
      return Response({
      "message":"Successfully updated organization info.",
      "organization": OrganizationSerializer(org).data
      }, status=status.HTTP_200_OK)
    else:
      return Response({"message":"This user does not have permission to update organization info."},
        status=status.HTTP_401_UNAUTHORIZED)
  except:
    return Response({"message":"Unable to update organization info."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_org(request):
  # request:
  #   org_id:   int, primary key of Organization to delete
  # NOTE: unlike removing a user profile, deleting an organization is 
  # permanent and cannot be undone

  try:
    org_id = request.data['org_id'] 
    org = Organization.objects.get(id=org_id)
    if (org.org_leader == request.user):
      org.delete()
      return Response({"message":"Successfully deleted organization."}, status=status.HTTP_200_OK)
    else:
      return Response({"message":"This user does not have permission to delete organization."},
        status=status.HTTP_401_UNAUTHORIZED)
  except:
    return Response({"message":"Unable to delete organization."}, status=status.HTTP_400_BAD_REQUEST)

