from django.urls import path,include
from userAuth.views import *

from .views import *

urlpatterns = [
    path('token/', RegisterView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', RefreshView.as_view(), name='token_refresh'),    
]
