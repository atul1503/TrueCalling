from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path,include

from .views import *

urlpatterns = [
    path('report/',ReportView.as_view(),name="reports"),
    path('search/name/',SearchByName.as_view(),name='name_search'), 
    path('search/phone/',SearchByPhone.as_view(),name="phone_search"),
    path('generate/testdata',Generate.as_view())
]
