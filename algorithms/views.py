from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *
from django.http import JsonResponse


class HomeView(TemplateView):
    template_name = 'algorithms/home.html'
    extra_context = {'title': 'HOME'}


class BinarySearchView(TemplateView):
    template_name = 'algorithms/binary_search.html'
    extra_context = {'title': 'Binary search'}
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BinarySearch()
        context["array"] = self.array
        return context


    def binary_search(self, array, target, low, hight):
        if low > hight:
            return False
        else:
            middle = (low + hight) // 2
            if target == array[middle]:
                return True
            elif target < array[middle]:
                return self.binary_search(array, target, low, middle - 1)
            elif target > array[middle]:
                return self.binary_search(array, target, middle + 1, hight)


    def post(self, request, *args, **kwargs):
        target = int(request.POST['number'])
        low = 0
        hight = len(self.array) - 1
        return JsonResponse({'answer': {'number': self.binary_search(self.array, target, low, hight)}}, status=200)


class SearchUppercaseView(TemplateView):
    template_name = 'algorithms/search_uppercase.html'
    extra_context = {'title': 'Search uppercase'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchUppercase()
        return context

    
    def search_uppercase(self, string, id=0):
        if string[id].isupper():
            return string[id]
        
        if id == len(string)-1:
            return '0 uppercase words'

        return self.search_uppercase(string, id+1)


    def post(self, request, *args, **kwargs):
        uppercase = self.search_uppercase(request.POST['string'])
        return JsonResponse({'answer': {'Uppercase word': uppercase}}, status=200)