from django.urls import path
from .views import DoctorsList,DotorsDetail,UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',UserCreate.as_view(), name='create-user'),
    path('token/',TokenObtainPairView.as_view(), name='get-token'),
    path("doctors/",DoctorsList.as_view(), name="d-list"),
    path('doctors/<int:pk>/', DotorsDetail.as_view(), name="d-detail"),
    path('refresh/', TokenRefreshView.as_view(),name='refresh-token')
    
]
