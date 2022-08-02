from rest_framework import generics
from algorithms.models import *
from .serializers import *

class AlgListAPIView(generics.ListAPIView):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer

class DetailAPIView(generics.RetrieveAPIView):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer
