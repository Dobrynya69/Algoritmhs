from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('binary_search/', BinarySearchView.as_view(), name='binary_search'),
    path('search_uppercase/', SearchUppercaseView.as_view(), name='search_uppercase'),
]
