from array import array
import random
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *
from django.http import JsonResponse
import json


class HomeView(TemplateView):
    template_name = 'algorithms/home.html'
    extra_context = {'title': 'HOME'}


class BinarySearchView(TemplateView):
    template_name = 'algorithms/binary_search.html'
    extra_context = {'title': 'Binary search'}
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BinarySearchForm()
        context['array'] = self.array
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


class LowerBoundView(TemplateView):
    template_name = 'algorithms/lower_bound.html'
    extra_context = {'title': 'Search lower bound'}
    array = [1, 1, 1, 2, 2, 4, 4, 7, 7, 10, 10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LowerBoundForm()
        context['array'] = self.array
        return context


    def lower_bound(self, array, target, low, hight):
        if low > hight:
            try:
                true_target = array[low]
            except IndexError:
                return 'Not valid number'

            if true_target == target:
                return low
            else:
                return 'Not valid number'
        else:
            middle = (low + hight) // 2
            if target <= array[middle]:
                return self.lower_bound(array, target, low, middle - 1)
            elif target > array[middle]:
                return self.lower_bound(array, target, middle + 1, hight)


    def post(self, request, *args, **kwargs):
        target = int(request.POST['number'])
        low = 0
        hight = len(self.array) - 1
        return JsonResponse({'answer': {'index': self.lower_bound(self.array, target, low, hight)}}, status=200)


class UpperBoundView(TemplateView):
    template_name = 'algorithms/upper_bound.html'
    extra_context = {'title': 'Search upper bound'}
    array = [1, 1, 1, 2, 2, 4, 4, 7, 7, 10, 10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UpperBoundForm()
        context['array'] = self.array
        return context


    def upper_bound(self, array, target, low, hight):
        if low > hight:
            try:
                true_target = array[low - 1]
            except IndexError:
                return 'Not valid number'
                
            if true_target == target:
                return low - 1
            else:
                return 'Not valid number'
        else:
            middle = (low + hight) // 2
            if target < array[middle]:
                return self.upper_bound(array, target, low, middle - 1)
            elif target >= array[middle]:
                return self.upper_bound(array, target, middle + 1, hight)


    def post(self, request, *args, **kwargs):
        target = int(request.POST['number'])
        low = 0
        hight = len(self.array) - 1
        return JsonResponse({'answer': {'index': self.upper_bound(self.array, target, low, hight)}}, status=200)


def generate_big_array():
    big_array = []
    for i in range(0, 100):
        if i % 3 == 0:
            big_array.append(i - (i * 3))
        else:
            big_array.append(i + (i * 3))
    return big_array


class SelectionSortView(TemplateView):
    template_name = 'algorithms/selection_sort.html'
    extra_context = {'title': 'Selection sort'}
    array = generate_big_array()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['array'] = self.array
        return context
    

    def selection_sort(self, data_array):
        array = data_array.copy()
        for i in range(0, len(array)-1):
            min_value_index = i

            for j in range(i+1, len(array)):
                if array[j] < array[min_value_index]:
                    min_value_index = j
            
            if min_value_index != i:
                array[min_value_index], array[i] = array[i], array[min_value_index]

        return str(array)


    def post(self, request, *args, **kwargs):
        return JsonResponse({'answer': {'Array': self.selection_sort(self.array)}}, status=200)


class BubleSortView(TemplateView):
    template_name = 'algorithms/buble_sort.html'
    extra_context = {'title': 'Buble sort'}
    array = generate_big_array()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['array'] = self.array
        return context
    

    def buble_sort(self, data_array):
        array = data_array.copy()

        for i in range(len(array)-1, 0, -1):
            for j in range(i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

        return str(array)


    def post(self, request, *args, **kwargs):
        return JsonResponse({'answer': {'Array': self.buble_sort(self.array)}}, status=200)


class InsertionSortView(TemplateView):
    template_name = 'algorithms/insertion_sort.html'
    extra_context = {'title': 'Insertion sort'}
    array = generate_big_array()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['array'] = self.array
        return context
    

    def insertion_sort(self, data_array):
        array = data_array.copy()

        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1

        return str(array)


    def post(self, request, *args, **kwargs):
        return JsonResponse({'answer': {'Array': self.insertion_sort(self.array)}}, status=200)


class QuickSortView(TemplateView):
    template_name = 'algorithms/quick_sort.html'
    extra_context = {'title': 'Quick sort'}
    array = generate_big_array()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['array'] = self.array
        return context
    

    def quick_sort(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()

        greaters = []
        lowers = []

        for item in array:
            if item > pivot:
                greaters.append(item)
            else:
                lowers.append(item)

        return self.quick_sort(lowers) + [pivot] + self.quick_sort(greaters)


    def post(self, request, *args, **kwargs):
        array = self.array
        return JsonResponse({'answer': {'Array': str(self.quick_sort(array))}}, status=200)


class KMPView(TemplateView):
    template_name = 'algorithms/KMP.html'
    extra_context = {'title': 'KMP search'}
    array = ['Hello world!', '**** you world!', 'I`m hate this world!', 'T_T']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['array'] = self.array
        context['form'] = KMPForm()
        return context
    

    def KMP(self, heystack, needle):
        if needle == '':
            return False
        
        lps = [0] * len(needle)
        prevLps, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLps]:
                lps[i] = prevLps + 1
                prevLps += 1
                i += 1
            elif prevLps == 0:
                lps[i] = 0
                i += 1
            else:
                prevLps = lps[prevLps - 1]

        i, j = 0, 0
        while i < len(heystack):
            if heystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]

            if j == len(needle):
                return True

        return False


    def post(self, request, *args, **kwargs):
        strings = {}
        for heystack in self.array:
            if self.KMP(heystack, request.POST['needle']):
                strings[str(len(strings) + 1)] = heystack
        return JsonResponse({'answer': strings}, status=200)