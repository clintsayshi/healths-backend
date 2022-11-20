
from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('', views.getRoutes),
    path('profiles/', views.getProfiles),
    path('users/register/', views.registerUser),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]