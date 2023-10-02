from tabulate import tabulate
from copy import deepcopy
from .algorithms.Distances import LevenshteinDistance, DamerauLevenshteinDistance, DamerauLevenshteinDistanceRecCache, DamerauLevenshteinDistanceRecursive


class StringDistanceCalculator:
    def __init__(self, String1 = "", String2 = ""):
        self._String1, self._String2 = ((String1.strip()).split(" "))[0], ((String2.strip()).split(" "))[0]
        self.rebuild()
        
    @property
    def String1(self):
        return self._String1

    @String1.setter
    def String1(self, value):
        if not isinstance(value, str):
            raise ValueError("String1 должен быть строкой")
        self._String1 = ((value.strip()).split(" "))[0]
        self.rebuild()

    @property
    def String2(self):
        return self._String2

    @String2.setter
    def String2(self, value):
        if not isinstance(value, str):
            raise ValueError("String2 должен быть строкой")
        self._String2 = ((value.strip()).split(" "))[0]
        self.rebuild()

    @property
    def lenStr1(self):
        return self._lenStr1
    
    @property
    def lenStr2(self):
        return self._lenStr2
    
    def rebuild(self):
        self._lenStr1, self._lenStr2 = len(self._String1), len(self._String2)
        self.matrix = [[0 for _ in range(self._lenStr2 + 1)] for _ in range(self._lenStr1 + 1)]
        
    def CalculateDistance(self, tp=True):
        if tp:
            return DamerauLevenshteinDistance(self._String1, self._String2)
        return LevenshteinDistance(self._String1, self._String2)
        
    def CalculateDistanceRecursive(self, cache=True):
        if cache:
            memo = {}
            return DamerauLevenshteinDistanceRecCache(self._String1, self._String2)
        return DamerauLevenshteinDistanceRecursive(self._String1, self._String2)
    
    def info(self):
        print(f"Первая строка: '{self.String1}', длина - {self.lenStr1}")
        print(f"Вторая стркоа: '{self.String2}',  длина - {self.lenStr2}")


