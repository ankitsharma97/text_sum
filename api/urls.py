from django.urls import path
from .views import RegisterUser, LoginUser, LogoutUser, UserDetail, FindUsers, SummarizeText

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="APIs",
        default_version='v1',
        description="APIs for user and text summarization",
        terms_of_service="",
        contact=openapi.Contact(email="ankit972125@gmail.com"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/', FindUsers.as_view(), name='find-users'),
    path('summarize/', SummarizeText.as_view(), name='summarize-text'),
]
