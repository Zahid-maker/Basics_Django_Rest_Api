
from django.contrib import admin
from django.urls import path,include
from .views import any_View,PostList,PostCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-auth',include('rest_framework.urls')),

    path('list-create',PostList.as_view()),
    path('',any_View.as_view(),name = "any view"),
    path('api/token',obtain_auth_token,name = 'obtain_token'),
    path('admin/', admin.site.urls),


]
