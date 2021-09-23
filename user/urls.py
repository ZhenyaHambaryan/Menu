from django.urls import path
from user import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserDetailViewSet, OrganizationViewSet, SignUpView
from django.views.generic.base import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Here we create multiple views from each ViewSet by binding the http methods to the required action for each view.

user_list = UserDetailViewSet.as_view({
    'get': 'list',
#    'post': 'create'
})

user_detail = UserDetailViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

organization_list = OrganizationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

organization_detail = OrganizationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# URL Patterns

urlpatterns = [
    path('user/api', views.api_root),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('organizations/', organization_list, name='organization-list'),
    path('organizations/<int:pk>/', organization_detail, name='organization-detail'),
    
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # rest_framework_jwt built-in urls
    # doc: https://jpadilla.github.io/django-rest-framework-jwt/
    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),
    # path('api-token-verify/', verify_jwt_token),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # verchacrac yev test arac:
    path('user_login', views.user_login, name="user-login"),
    path('register_user', views.register_user, name="register-user"),
    path('create_conf_code', views.create_conf_code, name="create-conf-code"),
    path('update_profile', views.update_profile, name="update-profile"),
    path('set_user_role', views.set_user_role, name='set-user-role'),
    path('remove_profile', views.remove_profile, name="remove-profile"),
    path('unremove_profile', views.unremove_profile, name="unremove-profile"),
    path('create_org', views.create_org, name='create-org'),
    path('join_org', views.join_org, name='join-org'),
    path('leave_org', views.leave_org, name='leave-org'),
    path('change_org_leader', views.change_org_leader, name="change-org-leader"), 
    path('update_org_info', views.update_org_info, name="update-org-info"),
    path('delete_org', views.delete_org, name="delete-org"),
    path('get_me', views.get_me,name="get-me"),

    # chi sksvac:

    # path('send_conf_code', views.send_conf_code, name='send-conf-code'),
    # path('send_email', views.send_email, name="send-email"),
    # path('send_text', views.send_text, name="send-text"), 


]

urlpatterns = format_suffix_patterns(urlpatterns)
