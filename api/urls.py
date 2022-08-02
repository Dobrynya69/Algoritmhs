from django.urls import path
from .views import *

urlpatterns = [
    path('alg_list/', AlgListAPIView.as_view()),
    path('<pk>/', DetailAPIView.as_view()),
]
