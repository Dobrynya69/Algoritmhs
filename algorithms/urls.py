from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('binary_search/', BinarySearchView.as_view(), name='binary_search'),
    path('lower_bound/', LowerBoundView.as_view(), name='lower_bound'),
    path('upper_bound/', UpperBoundView.as_view(), name='upper_bound'),
    path('selection_sort/', SelectionSortView.as_view(), name='selection_sort'),
    path('buble_sort/', BubleSortView.as_view(), name='buble_sort'),
    path('insertion_sort/', InsertionSortView.as_view(), name='insertion_sort'),
    path('quick_sort/', QuickSortView.as_view(), name='quick_sort'),
    path('kmp/', KMPView.as_view(), name='KMP'),
]
