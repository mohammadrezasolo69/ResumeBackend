from django.urls import path, include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]
