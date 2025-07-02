from django.urls import path
from .views import DoctorsList,DotorsDetail,UserCreate,PerscriptionList,PatientList,PaymentList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',UserCreate.as_view(), name='create-user'),
    path('token/',TokenObtainPairView.as_view(), name='get-token'),
    path('refresh/', TokenRefreshView.as_view(),name='refresh-token'),
    path("doctors/",DoctorsList.as_view(), name="d-list"),
    path('doctors/<int:pk>/', DotorsDetail.as_view(), name="d-detail"),
    path('patient/',PatientList.as_view(),name='p-list'),
    path('prescription/', PerscriptionList.as_view(), name="presc-list"),
    path('payment/',PatientList.as_view(), name='pay-list'),
    
    
    
   
    
]
